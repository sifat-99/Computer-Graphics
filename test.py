# --- CELL 1: Environment Setup ---
!pip install -q pandas numpy matplotlib seaborn scikit-learn lifelines xgboost mlxtend missingno imbalanced-learn plotly shap umap-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
from imblearn.over_sampling import SMOTE

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import shap

from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test
from mlxtend.frequent_patterns import association_rules, fpgrowth

import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 120})

# --- CELL 2: Data Ingestion and Aggregation ---
def ingest_and_aggregate_tcga_data(file_paths_dict):
    print("Initiating TCGA-COAD Data Ingestion and Aggregation Pipeline...")
    raw_clinical = pd.read_csv(file_paths_dict['clinical'], sep='\t', low_memory=False)
    missing_indicators =
    raw_clinical.replace(missing_indicators, np.nan, inplace=True)

    baseline_cols = [
        'cases.case_id', 'demographic.vital_status', 'demographic.age_at_index',
        'demographic.gender', 'demographic.days_to_death',
        'diagnoses.ajcc_pathologic_stage', 'diagnoses.primary_diagnosis',
        'diagnoses.days_to_last_follow_up', 'diagnoses.prior_malignancy'
    ]

    clinical_baseline = raw_clinical[[c for c in baseline_cols if c in raw_clinical.columns]].copy()
    patient_df = clinical_baseline.groupby('cases.case_id').first().reset_index()

    if 'treatments.treatment_type' in raw_clinical.columns:
        treatment_subset = raw_clinical[['cases.case_id', 'treatments.treatment_type']].dropna()
        treatment_counts = treatment_subset.groupby('cases.case_id').size().reset_index(name='total_treatments_received')
        treatment_counts['had_treatment'] = (treatment_counts['total_treatments_received'] > 0).astype(int)
        patient_df = pd.merge(patient_df, treatment_counts, on='cases.case_id', how='left')
        patient_df['had_treatment'].fillna(0, inplace=True)
        patient_df['total_treatments_received'].fillna(0, inplace=True)

    print(f"Aggregation Complete. Final Cohort Size: {patient_df.shape} unique patients.")
    return patient_df

# --- CELL 3: Feature Engineering ---
def engineer_clinical_features(df):
    print("Executing Feature Engineering Transformations...")
    engineered_df = df.copy()

    if 'demographic.vital_status' in engineered_df.columns:
        engineered_df['target_death'] = engineered_df['demographic.vital_status'].map({'Alive': 0, 'Dead': 1})
        engineered_df.dropna(subset=['target_death'], inplace=True)

    engineered_df['demographic.days_to_death'] = pd.to_numeric(engineered_df['demographic.days_to_death'], errors='coerce')
    engineered_df['diagnoses.days_to_last_follow_up'] = pd.to_numeric(engineered_df['diagnoses.days_to_last_follow_up'], errors='coerce')

    engineered_df['survival_days'] = np.where(
        engineered_df['target_death'] == 1,
        engineered_df['demographic.days_to_death'],
        engineered_df['diagnoses.days_to_last_follow_up']
    )
    engineered_df['survival_months'] = engineered_df['survival_days'] / 30.44

    def parse_ajcc_stage(stage_str):
        if pd.isna(stage_str): return np.nan
        stage_str = str(stage_str).upper()
        if 'IV' in stage_str: return 4
        elif 'III' in stage_str: return 3
        elif 'II' in stage_str: return 2
        elif 'I' in stage_str: return 1
        return np.nan

    if 'diagnoses.ajcc_pathologic_stage' in engineered_df.columns:
        engineered_df['stage_numeric'] = engineered_df['diagnoses.ajcc_pathologic_stage'].apply(parse_ajcc_stage)
        engineered_df['is_advanced_stage'] = (engineered_df['stage_numeric'] >= 3).astype(float)

    if 'demographic.age_at_index' in engineered_df.columns:
        engineered_df['demographic.age_at_index'] = pd.to_numeric(engineered_df['demographic.age_at_index'], errors='coerce')

    return engineered_df

# --- CELL 4: Exploratory Data Analysis (EDA) ---
def perform_eda_profiling(df):
    print("Generating EDA Visualizations...")
    features_of_interest = ['demographic.age_at_index', 'demographic.gender', 'stage_numeric', 'survival_months', 'target_death']
    eda_df = df[[c for c in features_of_interest if c in df.columns]].copy()

    plt.figure(figsize=(10, 6))
    msno.matrix(eda_df, sparkline=False, color=(0.25, 0.45, 0.6))
    plt.title("Missing Data Topological Profile", fontsize=16)
    plt.show()

    plt.figure(figsize=(7, 5))
    sns.countplot(data=eda_df, x='target_death', palette=['#2ca02c', '#d62728'])
    plt.title('Cohort Distribution by Mortality Status (0=Alive, 1=Dead)', fontsize=14)
    plt.show()

    plt.figure(figsize=(9, 6))
    sns.histplot(data=eda_df, x='survival_months', hue='target_death', kde=True, bins=40, palette=['#2ca02c', '#d62728'], element='step')
    plt.title('Survival Time Distribution Stratified by Mortality', fontsize=14)
    plt.show()

# --- CELL 5: Preprocessing and Class Balancing ---
def preprocess_for_machine_learning(df):
    print("Initiating Algorithmic Preprocessing and SMOTE Balancing...")
    features = ['demographic.age_at_index', 'demographic.gender', 'stage_numeric', 'diagnoses.prior_malignancy', 'had_treatment', 'is_advanced_stage']
    valid_features = [f for f in features if f in df.columns]
    X_raw = df[valid_features].copy()
    y = df['target_death'].values

    num_cols = [c for c in ['demographic.age_at_index', 'stage_numeric', 'is_advanced_stage', 'had_treatment'] if c in valid_features]
    cat_cols = [c for c in ['demographic.gender', 'diagnoses.prior_malignancy'] if c in valid_features]

    X_raw[num_cols] = SimpleImputer(strategy='median').fit_transform(X_raw[num_cols])
    if cat_cols:
        X_raw[cat_cols] = SimpleImputer(strategy='most_frequent').fit_transform(X_raw[cat_cols])
        X_encoded = pd.get_dummies(X_raw, columns=cat_cols, drop_first=True)
    else:
        X_encoded = X_raw

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_encoded.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_encoded.columns)

    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

    return X_train_resampled, X_test_scaled, y_train_resampled, y_test, X_encoded.columns

# --- CELL 6: Model Training and Evaluation ---
def train_and_evaluate_classifiers(X_train, y_train, X_test, y_test):
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42),
        'Decision Tree': DecisionTreeClassifier(max_depth=6, class_weight='balanced', random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42),
        'XGBoost': xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', learning_rate=0.1, max_depth=5, random_state=42)
    }

    results_list =
    trained_models = {}
    plt.figure(figsize=(10, 8))

    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        auc = roc_auc_score(y_test, y_prob)
        results_list.append({
            'Model': name, 'Accuracy': f"{accuracy_score(y_test, y_pred):.2%}",
            'F1-Score': f"{f1_score(y_test, y_pred):.2f}", 'AUC-ROC': f"{auc:.3f}"
        })
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        plt.plot(fpr, tpr, lw=2, label=f'{name} (AUC = {auc:.3f})')

    plt.plot(, , color='navy', lw=2, linestyle='--')
    plt.legend(loc="lower right")
    plt.title('ROC Curve Comparison')
    plt.show()
    return pd.DataFrame(results_list).sort_values(by='AUC-ROC', ascending=False), trained_models

# --- CELL 7: SHAP Interpretability ---
def generate_shap_explanations(best_model, X_test_scaled, feature_names):
    explainer = shap.TreeExplainer(best_model)
    shap_values = explainer.shap_values(X_test_scaled)
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, X_test_scaled, feature_names=feature_names, show=False)
    plt.title("SHAP Summary Plot")
    plt.show()

# --- CELL 8: Survival Analysis ---
def run_survival_analysis(df):
    surv_df = df.dropna(subset=['survival_months', 'target_death', 'is_advanced_stage']).copy()
    T, E = surv_df['survival_months'], surv_df['target_death'].astype(int)
    mask_advanced = surv_df['is_advanced_stage'] == 1

    kmf_early, kmf_late = KaplanMeierFitter(), KaplanMeierFitter()
    plt.figure(figsize=(10, 6))
    kmf_early.fit(T[~mask_advanced], event_observed=E[~mask_advanced], label="Early Stage (I & II)")
    kmf_early.plot_survival_function(ci_show=True, color='blue', lw=2)
    kmf_late.fit(T[mask_advanced], event_observed=E[mask_advanced], label="Advanced Stage (III & IV)")
    kmf_late.plot_survival_function(ci_show=True, color='red', lw=2)

    results = logrank_test(T[~mask_advanced], T[mask_advanced], event_observed_A=E[~mask_advanced], event_observed_B=E[mask_advanced])
    plt.title(f"Kaplan-Meier Survival Estimation (Log-rank p-value: {results.p_value:.4e})")
    plt.show()

    cox_cols = ['survival_months', 'target_death', 'demographic.age_at_index', 'stage_numeric', 'had_treatment']
    cox_df = df[[c for c in cox_cols if c in df.columns]].dropna().copy()
    cph = CoxPHFitter(penalizer=0.01)
    cph.fit(cox_df, duration_col='survival_months', event_col='target_death')
    cph.plot()
    plt.title("Cox Proportional Hazards Forest Plot")
    plt.show()

# --- CELL 9: Association Rule Mining ---
def mine_clinical_association_rules(df):
    print("Initiating Association Rule Mining...")
    arm_df = pd.DataFrame()
    if 'stage_numeric' in df.columns:
        arm_df = df['stage_numeric'].map({1.0: 'Early', 2.0: 'Early', 3.0: 'Late', 4.0: 'Late'})
    if 'target_death' in df.columns:
        arm_df['Mortality'] = df['target_death'].map({1: 'Dead', 0: 'Alive'})

    boolean_matrix = pd.get_dummies(arm_df.dropna()).astype(bool)
    frequent_itemsets = fpgrowth(boolean_matrix, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5, num_itemsets=2)
    print("\n--- Top Clinical Association Rules ---")
    print(rules.sort_values(by='lift', ascending=False)[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(5))

# --- CELL 10: Pipeline Execution ---
# NOTE: Upload your TCGA `clinical.tsv` file to the Colab files section before running this block.
file_paths = {'clinical': 'clinical.tsv'}

# 1. Ingestion & Feature Engineering
tcga_aggregated_df = ingest_and_aggregate_tcga_data(file_paths)
tcga_engineered_df = engineer_clinical_features(tcga_aggregated_df)

# 2. EDA
perform_eda_profiling(tcga_engineered_df)

# 3. Machine Learning Preprocessing
X_train_bal, X_test_scl, y_train_bal, y_test_raw, feature_cols = preprocess_for_machine_learning(tcga_engineered_df)

# 4. Model Training & Evaluation
metrics_df, models_dict = train_and_evaluate_classifiers(X_train_bal, y_train_bal, X_test_scl, y_test_raw)
print("\n--- Model Performance Metrics ---")
print(metrics_df)

# 5. Interpretability Analysis
generate_shap_explanations(models_dict, X_test_scl, feature_cols)

# 6. Biostatistical Survival Analysis
run_survival_analysis(tcga_engineered_df)

# 7. Association Rules
mine_clinical_association_rules(tcga_engineered_df)
