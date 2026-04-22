# Lab 9 Exercises Completion Summary

## All Exercises Implemented ✅

### Exercise 1: Dynamic Color Changes
**Requirement:** Change cube color dynamically
**Implementation:** ✅ COMPLETE
- Each face of the cube has a unique color
- Colors are: Green (top), Orange (bottom), Red (front), Yellow (back), Magenta (right), Cyan (left)
- Colors are applied via `glColor3f()` before drawing each face

**Code Location:** `draw_cube()` function, lines defining face colors
**How to see:** Run the program and observe the multi-colored cube on the right side

---

### Exercise 2: Move Pyramid Up and Down
**Requirement:** Move pyramid up and down
**Implementation:** ✅ COMPLETE
- Use **I Key** to move pyramid UP
- Use **K Key** to move pyramid DOWN
- Movement range: -2 to +2 units along Y-axis
- Real-time smooth movement

**Code Location:** `keyboard()` function, lines with `pyramid_position[1]`
**Global Variable:** `pyramid_position = [0, 0, 0]`

---

### Exercise 3: Add Rotation - Rotate Cube Continuously
**Requirement:** Add rotation with `glRotatef(angle, 1,1,0)` - rotate cube continuously
**Implementation:** ✅ COMPLETE

**Manual Rotation (Always Available):**
- **W Key** - Rotate cube up (around X-axis)
- **S Key** - Rotate cube down (around X-axis)
- **A Key** - Rotate cube left (around Y-axis)
- **D Key** - Rotate cube right (around Y-axis)

**Continuous Rotation (Animation Mode):**
- **C Key** - Toggle cube continuous animation
- When enabled, cube automatically rotates around X and Y axes
- Combined with manual controls for full flexibility

**Code Location:** `update_animation()` function for continuous, `display()` for manual
**Global Variables:** `cube_rotation = [0, 0, 0]`, `animate_cube = False`

---

### Exercise 4: Change Perspective - gluPerspective() Values
**Requirement:** Try different gluPerspective() values
**Implementation:** ✅ COMPLETE
- **Z Key** - Decrease FOV (zoom in, max 120°)
- **Shift+Z Key** - Increase FOV (zoom out, min 10°)
- Default FOV: 45° (standard perspective angle)
- Real-time perspective adjustment

**Code Location:** `reshape()` function uses `perspective_value`
**Global Variable:** `perspective_value = 45`
**Formula:** `gluPerspective(perspective_value, w/h, 0.1, 100)`

---

### Exercise 5: Draw 3 Objects - Cube, Pyramid, Sphere
**Requirement:** Draw cube, pyramid, and sphere using gluSphere()
**Implementation:** ✅ COMPLETE

**Object 1 - Cube:**
- Position: Right side (2.5, 0, -8)
- Color: Multi-colored faces
- Function: `draw_cube(0.8)`

**Object 2 - Pyramid:**
- Position: Left side (-2.5, 0, -7)
- Color: Red, Green, Blue, Yellow faces
- Function: `draw_pyramid(0.8)`

**Object 3 - Sphere:**
- Position: Center (0, 0, -9)
- Color: Orange
- Function: `draw_sphere(radius=0.8, slices=20, stacks=20)`
- Toggle visibility: **X Key**

**Code Location:** `draw_sphere()` function, `display()` shows all three objects
**Implementation Details:** Uses `gluNewQuadric()` and `gluSphere()` from OpenGL.GLU

---

### Exercise 6: Create Keyboard Control
**Requirement:** Press key → rotate object, Press key → move object
**Implementation:** ✅ COMPLETE

**Cube Control:**
```
W - Rotate around X-axis (up)
S - Rotate around X-axis (down)
A - Rotate around Y-axis (left)
D - Rotate around Y-axis (right)
```

**Pyramid Control:**
```
I - Move up (Y-axis)
K - Move down (Y-axis)
J - Rotate left
L - Rotate right
```

**Sphere Control:**
```
X - Toggle visibility
Arrow Keys - Rotate in any direction
↑ - Rotate around X-axis
↓ - Rotate around X-axis
← - Rotate around Y-axis
→ - Rotate around Y-axis
```

**Additional Controls:**
```
C - Toggle cube animation
P - Toggle pyramid animation
+/- - Scale all objects
Z - Adjust FOV
R - Reset all values
H - Show help menu
Q - Quit
```

**Code Location:** `keyboard()` and `special_keys()` functions
**Implementation:** Uses `glutKeyboardFunc()` and `glutSpecialFunc()`

---

### Exercise 7: Scaling + Rotation + Translation Together
**Requirement:** Implement scaling + rotation + translation together
**Implementation:** ✅ COMPLETE

**All Three Transformations Combined:**
```
glLoadIdentity()              # Start fresh
glTranslatef(x, y, z)        # Translation (position)
glRotatef(angle, x, y, z)    # Rotation (around axes)
glScalef(sx, sy, sz)         # Scaling (size)
draw_object()                # Draw with transformations applied
```

**Demonstration in Program:**
- **Cube:** Translates to (2.5, 0, -8) → Rotates (manual + auto) → Scales with +/- keys
- **Pyramid:** Translates to (-2.5, position_y, -7) → Rotates (manual + auto) → Scales with +/- keys
- **Sphere:** Translates to (0, 0, -9) → Rotates (arrow keys) → Scales with +/- keys

**User Controls:**
- **+Key:** Increase scale factor (1.1x each press)
- **-Key:** Decrease scale factor (0.9x each press)

**Code Location:** `display()` function, lines showing transformation sequence
**Global Variable:** `scale_values = [1.0, 1.0, 1.0]`
**Matrix Order:** Translation → Rotation → Scaling (critical for correct results)

---

### Exercise 8: Animation - Cube Rotating + Pyramid Bouncing
**Requirement:** Animate cube rotating + pyramid bouncing
**Implementation:** ✅ COMPLETE

**Cube Animation:**
- Press **C Key** to toggle
- Rotates continuously around X and Y axes
- Angle increments by 2° per frame
- Speed: ~120°/sec at 60 FPS

**Pyramid Animation:**
- Press **P Key** to toggle
- Bounces up and down along Y-axis
- Range: -2 to +2 units
- Rotates while bouncing (1° per frame)
- Direction reverses at boundaries

**Both Can Run Simultaneously:**
- Enable both with C and P keys together
- Creates complex, realistic 3D animation
- Manual controls still work while animations run

**Code Location:** `update_animation()` function
**Global Variables:**
```
animate_cube = False
animate_pyramid = False
animation_angle = 0
pyramid_bounce_direction = 1
pyramid_bounce_speed = 0.05
```

---

## Summary Table

| Exercise | Requirement | Status | Key Controls | Code Function |
|----------|-------------|--------|--------------|----------------|
| 1 | Dynamic colors | ✅ | Visual only | `draw_cube()` |
| 2 | Pyramid movement | ✅ | I/K | `keyboard()` |
| 3 | Cube rotation | ✅ | W/S/A/D, C | `keyboard()`, `display()` |
| 4 | Perspective control | ✅ | Z/Shift+Z | `reshape()` |
| 5 | Three 3D objects | ✅ | X, Arrows | `draw_sphere()`, `display()` |
| 6 | Keyboard control | ✅ | Multiple keys | `keyboard()`, `special_keys()` |
| 7 | Transform together | ✅ | +/-, W/S/A/D/I/K | `display()` |
| 8 | Animation | ✅ | C, P | `update_animation()` |

---

## How to Verify Each Exercise

1. **Run the program:**
   ```bash
   python3 ID-364_Lab9_3D_Shapes.py
   ```

2. **Press H to see help menu** with all controls

3. **Test each exercise in order:**
   - Exercise 1: Observe colored cube
   - Exercise 2: Press I and K to move pyramid
   - Exercise 3: Press C to auto-rotate cube
   - Exercise 4: Press Z and Shift+Z to zoom
   - Exercise 5: Press X to show sphere
   - Exercise 6: Try all keyboard controls
   - Exercise 7: Press + to scale, then rotate/move
   - Exercise 8: Press C and P to see animations

---

## Program Statistics

- **Total Lines of Code:** ~580
- **Functions Implemented:** 11
- **Global Variables:** 13
- **Keyboard Shortcuts:** 20+
- **3D Objects:** 3 (Cube, Pyramid, Sphere)
- **Transformations:** Translation, Rotation, Scaling
- **Animation Modes:** 2 (Cube rotation, Pyramid bounce)
- **Target Frame Rate:** 60 FPS

---

**All exercises completed successfully!** ✅

The program is fully functional and ready for submission.

Student ID: 364
Student Name: Md Abdur Rahman Sifat
