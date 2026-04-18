# 🎮 Computer Graphics — CSE 364 Lab Portfolio

> A comprehensive collection of **Computer Graphics** implementations — from foundational rasterization algorithms to a fully playable OpenGL Flappy Bird game and an interactive chess engine. Built with Python.

---

## 📁 Project Structure

```
Graphics/
│
├── 📄 dda_line.py              ← DDA Line Drawing Algorithm (standalone)
├── 📄 dda_triangle.py          ← DDA Triangle using 3 line segments
├── 📄 Chease.py                ← Full Chess Game (Python Turtle)
│
├── 📂 Lab 2/                   ← Bresenham's Line Drawing Algorithm
│   ├── Id-364-task_1.py        ← Bresenham – All 8 Octants
│   ├── Id-364-task_2.py        ← DDA vs Bresenham Comparison
│   ├── Id-364-task_3.py        ← Pixel Count Verification
│   └── Id-364-task_4.py        ← Polygon Drawing via Bresenham
│
├── 📂 Lab 3/                   ← Bresenham's Circle Drawing Algorithm
│   ├── _364_task1.py           ← Circles with Different Radii
│   ├── _364_task2.py           ← Concentric Circles
│   ├── _364_task3.py           ← Shifted Circle Center
│   ├── _364_task4.py           ← Circle in Each Quadrant
│   ├── _364_task5.py           ← Filled Circle
│   └── _364_task6.py           ← (Extended Tasks)
│
└── 📂 Mithu-Urea/              ← 🐦 OpenGL Flappy Bird Game
    ├── main.py                 ← Full game source code
    ├── requirements.txt        ← Python dependencies
    ├── run_game.bat            ← Windows launcher
    ├── run_game.ps1            ← PowerShell launcher
    └── assets/
        ├── Texture/            ← Bird & background textures
        └── Sound/              ← Jump, coin & ambient audio
```

---

## 🧪 Lab Implementations

### Lab 1 — DDA Line & Triangle Drawing

> **Digital Differential Analyzer (DDA)** is a scan-conversion algorithm that uses floating-point arithmetic to rasterize lines by incrementally stepping in the dominant direction.

| File | Description |
|------|-------------|
| `dda_line.py` | Core DDA implementation. Takes `(x1, y1)` → `(x2, y2)`, calculates step increments, and plots the rasterized line with Matplotlib. Includes console step-by-step output. |
| `dda_triangle.py` | Draws a triangle by applying `dda_line` to all three edges (AB, BC, CA) and rendering them with distinct colors. |

**Run:**
```bash
python dda_line.py
# Enter: x1, y1, x2, y2 when prompted

python dda_triangle.py
# Enter: 3 vertex coordinates when prompted
```

**Algorithm Overview:**
```
steps = max(|dx|, |dy|)
x_inc = dx / steps
y_inc = dy / steps

for i in range(steps+1):
    plot(round(x), round(y))
    x += x_inc;  y += y_inc
```

---

### Lab 2 — Bresenham's Line Drawing Algorithm

> **Bresenham's algorithm** improves upon DDA by using only **integer arithmetic** and a decision variable `d` to determine the next pixel — making it significantly faster for hardware rasterization.

| File | Task |
|------|------|
| `Id-364-task_1.py` | Implements the **general Bresenham algorithm** covering all **8 octants**. Tests lines across all slope combinations and plots them in one figure. |
| `Id-364-task_2.py` | **Side-by-side comparison** of DDA and Bresenham outputs for the same line `(2,3) → (12,8)`. Prints pixel coordinates for both. |
| `Id-364-task_3.py` | **Pixel count verification** — asserts that `count == max(|dx|, |dy|) + 1` for mathematical correctness. |
| `Id-364-task_4.py` | Generalized **polygon drawing** using Bresenham. Connects `n` vertices cyclically, demonstrated with a triangle. |

**Run any task:**
```bash
cd "Lab 2"
python Id-364-task_1.py
python Id-364-task_2.py
# etc.
```

**Decision Variable Logic:**
```
d = 2·dy − dx          # Initial decision value
if d < 0:  d += 2·dy   # Move straight → (South)
else:      d += 2·(dy − dx);  y++   # Move diagonal (Transverse)
```

---

### Lab 3 — Bresenham's Circle Drawing Algorithm

> **Bresenham's Circle Algorithm** uses the **8-way symmetry** of a circle. Only one octant is computed; the remaining 7 points are derived by reflection — requiring only `⌈r/√2⌉` iterations for a circle of radius `r`.

| File | Task |
|------|------|
| `_364_task1.py` | Draws circles of **different radii** (5, 8, 12, 20) all centered at the origin. |
| `_364_task2.py` | Draws **concentric circles** (radii 5, 10, 15) — classic bulls-eye pattern. |
| `_364_task3.py` | Circle with a **shifted center** at `(30, 40)` with radius 20, demonstrating translation. |
| `_364_task4.py` | Draws a circle in **each quadrant** (Q1–Q4) using center positions `(±30, ±30)`. |
| `_364_task5.py` | Draws a **filled circle** (solid disk) of radius 20 by scanning horizontal spans between symmetric boundary points. |

**Run any task:**
```bash
cd "Lab 3"
python _364_task1.py
```

**Core Algorithm:**
```python
x, y = 0, r
d = 3 - 2*r            # Initial decision parameter

while x <= y:
    plot_8_symmetric_points(cx, cy, x, y)
    if d < 0:
        d += 4*x + 6   # Move East
    else:
        d += 4*(x-y) + 10
        y -= 1         # Move South-East
    x += 1
```

---

## 🎮 Projects

### 🐦 Flappy Bird — OpenGL Edition (`Mithu-Urea/`)

A complete, polished **Flappy Bird** clone built from scratch with **PyOpenGL** and **pygame**. Every visual element is drawn using raw OpenGL primitives — no sprite engine involved.

**Features:**
- 🐦 **Animated Bird** — 4-frame wing-flap animation via texture cycling
- 🌄 **Dynamic Backgrounds** — 5 AI-generated backgrounds with smooth GPU crossfade every 15 seconds
- 🟢 **Procedural Pipes** — Gradient-shaded pipes with node decorations, spawning at random Y offsets
- 💰 **Coin System** — Shiny dollar coins spawn in pipe gaps (60% chance); collected on collision, triggers sound effect
- ❤️ **Lives System** — Start with 3 lives; lose one per pipe collision; game over when all lost
- 🎵 **Audio** — Jump sound, ambient jungle music, collectible coin chime (via pygame mixer)
- 🔄 **Restart** — Press `R` to reset the game at any time

**Controls:**

| Key | Action |
|-----|--------|
| `SPACE` | Flap / Jump |
| `R` | Restart game |
| `Q` | Quit |

**Setup & Run:**

```bash
# Navigate to game directory
cd Mithu-Urea

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# OR
.venv\Scripts\Activate.ps1       # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

> **Windows shortcut:** Double-click `run_game.bat` or run `run_game.ps1`

**Dependencies:**
```
PyOpenGL
PyOpenGL-accelerate
Pillow
pygame
```

**Architecture Highlights:**
- `init()` — Loads textures from `assets/Texture/`, initializes pygame mixer, picks random starting BG
- `display()` — GLUT display callback: draws BG → bird → pipes → coins → HUD
- `update(value)` — Timer-driven game loop at ~60 FPS: physics, collision, coin spawning, BG crossfade state machine
- `keyboard()` — Handles `SPACE`, `R`, `Q` keypresses
- `draw_coin()` — Renders a multi-layered gold disk with a `$` dollar sign drawn with GL line primitives

---

### ♟️ Chess (`Chease.py`)

A fully playable **two-player chess game** using Python's `turtle` graphics library.

**Features:**
- ✅ All standard chess pieces: Pawn, Knight, Bishop, Rook, Queen, King
- ✅ Full legal move validation for all 6 piece types
- ✅ **Castling** — both kingside and queenside
- ✅ **En Passant** — correctly tracked and executed
- ✅ **Check detection** — visual flashing highlight on the king in check
- ✅ **Board flip** — board automatically flips after each move (alternating perspective)
- ✅ Custom piece shapes registered with the Turtle shape system

**Run:**
```bash
python Chease.py
```

> Click a piece to select it (highlighted in pink), then click the destination square to move. Illegal moves are ignored.

---

## 🛠️ Requirements

### Root-Level Scripts
```bash
pip install matplotlib
```

### Flappy Bird Game
```bash
pip install PyOpenGL PyOpenGL-accelerate Pillow pygame
```

### Chess Game
```bash
# No external libraries — only Python standard library (turtle)
```

---

## 📚 Concepts Covered

| Topic | Implementation |
|-------|---------------|
| DDA Line Algorithm | `dda_line.py`, `Lab 2/task_2` |
| Bresenham Line Algorithm | `Lab 2/task_1–4` |
| Bresenham Circle Algorithm | `Lab 3/task_1–5` |
| 8-way Circle Symmetry | `Lab 3/task_1–4` |
| Circle Filling (Scan-line) | `Lab 3/task_5` |
| OpenGL Texture Mapping | `Mithu-Urea/main.py` |
| OpenGL Blending & Alpha | `Mithu-Urea/main.py` (crossfade) |
| Game Loop Architecture | `Mithu-Urea/main.py` |
| AABB Collision Detection | `Mithu-Urea/main.py` |
| Rule-based Game AI Logic | `Chease.py` |
| Turtle Graphics | `Chease.py` |

---

## 👤 Author

**Sifat** — CSE 364 • Computer Graphics Lab
Department of Computer Science & Engineering

---

*Built with Python 🐍 • OpenGL 🖥️ • Matplotlib 📊 • Turtle 🐢*
