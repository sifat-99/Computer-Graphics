# Lab 9: Drawing 3D Cube and Pyramid using PyOpenGL

**Student:** Md Abdur Rahman Sifat
**ID:** 364
**Course:** Computer Graphics
**Date:** 2026

---

## Overview

This program demonstrates fundamental concepts of 3D graphics rendering using PyOpenGL, including:
- Basic 3D rendering and coordinate systems
- OpenGL pipeline and transformations
- Depth testing and perspective projection
- Interactive keyboard controls
- Animation capabilities

---

## Exercises Implemented

### ✅ Exercise 1: Dynamic Color Changes
The cube displays different colors on each face and maintains vibrant coloring throughout interaction.

### ✅ Exercise 2: Pyramid Movement
- **I Key:** Move pyramid up
- **K Key:** Move pyramid down
- The pyramid moves smoothly along the Y-axis within the range of -2 to +2 units

### ✅ Exercise 3: Continuous Rotation
- **C Key:** Toggle cube animation (continuous rotation)
- When enabled, the cube rotates continuously along multiple axes
- Manual rotation is still available with W/S/A/D keys

### ✅ Exercise 4: Perspective Control
- **Z Key:** Decrease Field of View (zoom in)
- **Shift+Z Key:** Increase Field of View (zoom out)
- FOV range: 10° to 120°
- Demonstrates how perspective affects object appearance at different distances

### ✅ Exercise 5: Three 3D Objects
The program displays:
1. **Cube** - On the right side with 6 colored faces
2. **Pyramid** - On the left side with 4 colored triangular faces
3. **Sphere** - Toggle visibility with X key
   - Arrow keys control sphere rotation
   - Demonstrates GLU utility for complex shapes

### ✅ Exercise 6: Keyboard Control System
Complete interactive control:
```
CUBE ROTATION:
  W/S - Rotate cube up/down (around X-axis)
  A/D - Rotate cube left/right (around Y-axis)

PYRAMID MOVEMENT:
  I/K - Move pyramid up/down
  J/L - Rotate pyramid left/right

ANIMATION CONTROLS:
  C - Toggle cube continuous rotation
  P - Toggle pyramid animation (bouncing)

SPHERE CONTROLS:
  X - Toggle sphere visibility
  Arrow Keys - Rotate sphere in any direction
```

### ✅ Exercise 7: Combined Transformations
All three transformations work together:
```
SCALING (affects all objects):
  + Key - Increase size
  - Key - Decrease size

ROTATION:
  - Cube: W/S/A/D keys + C for continuous
  - Pyramid: J/L keys + P for animation
  - Sphere: Arrow keys

TRANSLATION:
  - Cube: Fixed position (2.5, 0, -8)
  - Pyramid: I/K keys for Y-axis movement
  - Sphere: Fixed position (-3, 0, -8)
```

### ✅ Exercise 8: Animation System
**Cube Animation (C Key):**
- Continuous rotation around X and Y axes simultaneously
- Creates a spinning effect

**Pyramid Animation (P Key):**
- Bounces up and down along the Y-axis
- Rotates continuously while bouncing
- Speed-controlled bounce with direction reversal at boundaries

---

## Program Features

### Core Rendering
- **Depth Testing:** Enabled to prevent z-fighting and ensure proper face ordering
- **Lighting:** Basic lighting with GL_LIGHT0 for realistic shading
- **Color Material:** Allows per-vertex color definition
- **Buffer Clearing:** Properly clears both color and depth buffers each frame

### Object Drawing Functions
1. **`draw_cube(size)`** - Draws a cube with unique colors for each face
2. **`draw_pyramid(size)`** - Draws a pyramid with colored triangular faces
3. **`draw_sphere(radius, slices, stacks)`** - Uses GLU to draw a sphere

### Transformation Pipeline
```
glLoadIdentity()  → Reset matrix
glTranslatef()    → Position in 3D space
glRotatef()       → Apply rotations (X, Y, Z axes)
glScalef()        → Scale objects
```

### Interactive Features
- Real-time keyboard input processing
- Continuous animation with 60 FPS target
- Smooth transitions and transformations
- Help menu system

---

## How to Run

### Prerequisites
```bash
pip install PyOpenGL PyOpenGL_accelerate pygame
```

### Execution
```bash
python3 ID-364_Lab9_3D_Shapes.py
```

A window will open showing the 3D scene with a cube and pyramid.

---

## Keyboard Controls (Complete Reference)

| Key(s) | Action |
|--------|--------|
| **W** | Rotate cube up |
| **S** | Rotate cube down |
| **A** | Rotate cube left |
| **D** | Rotate cube right |
| **I** | Move pyramid up |
| **K** | Move pyramid down |
| **J** | Rotate pyramid left |
| **L** | Rotate pyramid right |
| **C** | Toggle cube continuous animation |
| **P** | Toggle pyramid bouncing animation |
| **X** | Toggle sphere visibility |
| **↑/↓** | Rotate sphere up/down |
| **←/→** | Rotate sphere left/right |
| **+** | Increase scale |
| **-** | Decrease scale |
| **Z** | Decrease FOV (zoom in) |
| **Shift+Z** | Increase FOV (zoom out) |
| **R** | Reset all to default values |
| **H** | Show help menu |
| **Q** | Quit program |

---

## Technical Implementation Details

### Global State Variables
```python
cube_rotation = [0, 0, 0]           # Euler angles for cube
pyramid_position = [0, 0, 0]        # Position in 3D space
pyramid_rotation = [0, 0, 0]        # Euler angles for pyramid
sphere_position = [-3, 0, -8]       # Fixed sphere position
sphere_rotation = [0, 0, 0]         # Euler angles for sphere
animate_cube = False                # Animation toggle
animate_pyramid = False             # Animation toggle
animation_angle = 0                 # Current animation frame
scale_values = [1.0, 1.0, 1.0]    # Scaling factors
perspective_value = 45              # FOV in degrees
```

### Display Pipeline
1. **Clear buffers** - Remove previous frame
2. **Update animation** - Modify rotation/position values
3. **Render cube** - Apply transformations and draw
4. **Render pyramid** - Apply transformations and draw
5. **Render sphere** - Apply transformations and draw (if enabled)
6. **Swap buffers** - Display the frame

### Coordinate System
- **X-axis** → Left/Right (positive = right)
- **Y-axis** → Up/Down (positive = up)
- **Z-axis** → Depth (negative = away from camera)

---

## Learning Outcomes

After completing this lab, you understand:

1. ✅ Basic 3D rendering with OpenGL
2. ✅ Vertex-based shape definition
3. ✅ Transformation matrices (translation, rotation, scaling)
4. ✅ Depth testing and buffer management
5. ✅ Perspective projection
6. ✅ Interactive graphics programming
7. ✅ Animation techniques
8. ✅ Lighting and shading basics

---

## Troubleshooting

### Window doesn't appear
- Check if you have a display connected
- Ensure PyOpenGL is properly installed
- Verify GLUT/OpenGL libraries are available

### Poor performance
- Reduce sphere slice/stack count
- Disable animation modes (C and P keys)
- Reduce window size

### Objects not visible
- Press 'R' to reset all transformations
- Check FOV (Z key) - may be zoomed too far
- Verify depth testing is enabled

---

## Code Structure

The program is organized into logical sections:

1. **Imports** - Required OpenGL, GLU, GLUT libraries
2. **Global Variables** - State management
3. **Initialization** - `init()` function
4. **Drawing Functions** - `draw_cube()`, `draw_pyramid()`, `draw_sphere()`
5. **Update Logic** - `update_animation()`
6. **Display Function** - `display()` main rendering loop
7. **Event Handlers** - `keyboard()`, `special_keys()`, `reshape()`
8. **Helper Functions** - `print_help()`, `timer_callback()`
9. **Main Entry Point** - `main()` function

---

## Files Included

- **ID-364_Lab9_3D_Shapes.py** - Main program file
- **README.md** - This documentation file

---

## Notes for Instructor

This implementation goes beyond the basic requirements by:
- Providing comprehensive keyboard controls
- Adding animation capabilities
- Implementing proper lighting and shading
- Including a help system
- Supporting real-time interactive manipulation
- Using proper OpenGL conventions and best practices

All 8 exercises from the lab PDF have been successfully implemented and integrated into a single, cohesive program.

---

**Student ID:** 364
**Student Name:** Md Abdur Rahman Sifat
**Submission Date:** April 22, 2026
