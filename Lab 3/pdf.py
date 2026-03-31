import numpy as np
import matplotlib.pyplot as plt

def translate(points, tx, ty):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0,  1]])
    return (T @ points.T).T

def scale(points, sx, sy):
    S = np.array([[sx,  0, 0],
                  [ 0, sy, 0],
                  [ 0,  0, 1]])
    return (S @ points.T).T

def rotate(points, angle):
    rad = np.radians(angle)
    R = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad),  np.cos(rad), 0],
        [          0,            0, 1]
    ])
    return (R @ points.T).T

def shear(points, shx=0, shy=0):
    Sh = np.array([[  1, shx, 0],
                   [shy,   1, 0],
                   [  0,   0, 1]])
    return (Sh @ points.T).T

# Square points (closed loop)
square = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
])

# Perform transformations
translated = translate(square, 2, 1)
scaled = scale(square, 2, 1.5)
rotated = rotate(square, 45)
sheared = shear(square, 1, 0)

# Create the plot
plt.figure(figsize=(7, 7))

# Plot all transformations matching the exact colors and styles
plt.plot(square[:, 0], square[:, 1], color='blue', linestyle='-', label='Original')
plt.plot(translated[:, 0], translated[:, 1], color='red', linestyle='--', label='Translated')
plt.plot(scaled[:, 0], scaled[:, 1], color='green', linestyle='--', label='Scaled')
plt.plot(rotated[:, 0], rotated[:, 1], color='m', linestyle='--', label='Rotated')
plt.plot(sheared[:, 0], sheared[:, 1], color='c', linestyle='--', label='Sheared')

# Styling the plot
plt.title('Basic 2D Transformations on a Square')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='upper right')
plt.grid(True)
plt.axis('equal')  # To ensure squares look like squares and not rectangles
plt.xlim(-0.8, 3.2)
plt.ylim(-1, 3.2)

plt.show()
