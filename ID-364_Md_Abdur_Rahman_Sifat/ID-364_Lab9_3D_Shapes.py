"""
Lab 9: Drawing 3D Cube and Pyramid using PyOpenGL
Student: Md Abdur Rahman Sifat
ID: 364

This program demonstrates:
1. Basic 3D rendering with PyOpenGL
2. Drawing cube and pyramid using vertices
3. Depth testing and perspective projection
4. Transformations (translate, rotate, scale)
5. Keyboard controls for interactive manipulation
6. Animation of objects
7. Drawing multiple 3D shapes (cube, pyramid, sphere)
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

# Global variables for transformations and animation
cube_rotation = [0, 0, 0]
pyramid_position = [0, 0, 0]
pyramid_rotation = [0, 0, 0]
sphere_position = [-3, 0, -8]
sphere_rotation = [0, 0, 0]

# Animation variables
animate_cube = False
animate_pyramid = False
animation_angle = 0
pyramid_bounce_direction = 1
pyramid_bounce_speed = 0.05

# Color variables for dynamic color changes
cube_color = [1.0, 0.0, 0.0]  # Red
color_cycle = 0

# Display mode variables
perspective_value = 45  # FOV angle
show_sphere = False

# Scaling
scale_values = [1.0, 1.0, 1.0]


def init():
    """Initialize OpenGL settings"""
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Dark gray background
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_DIFFUSE)

    # Set up lighting
    light_position = [5, 5, 5, 0]
    glLight(GL_LIGHT0, GL_POSITION, light_position)
    glLight(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLight(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])


def draw_cube(size=1.0):
    """Draw a cube with dynamic colors"""
    glBegin(GL_QUADS)

    # Top face - Green
    glColor3f(0, 1, 0)
    glVertex3f(size, size, -size)
    glVertex3f(-size, size, -size)
    glVertex3f(-size, size, size)
    glVertex3f(size, size, size)

    # Bottom face - Orange
    glColor3f(1, 0.5, 0)
    glVertex3f(size, -size, size)
    glVertex3f(-size, -size, size)
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)

    # Front face - Red
    glColor3f(1, 0, 0)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)

    # Back face - Yellow
    glColor3f(1, 1, 0)
    glVertex3f(size, -size, -size)
    glVertex3f(-size, -size, -size)
    glVertex3f(-size, size, -size)
    glVertex3f(size, size, -size)

    # Right face - Magenta
    glColor3f(1, 0, 1)
    glVertex3f(size, size, size)
    glVertex3f(size, size, -size)
    glVertex3f(size, -size, -size)
    glVertex3f(size, -size, size)

    # Left face - Cyan
    glColor3f(0, 1, 1)
    glVertex3f(-size, size, size)
    glVertex3f(-size, size, -size)
    glVertex3f(-size, -size, -size)
    glVertex3f(-size, -size, size)

    glEnd()


def draw_pyramid(size=1.0):
    """Draw a pyramid with colored faces"""
    glBegin(GL_TRIANGLES)

    # Front face - Red
    glColor3f(1, 0, 0)
    glVertex3f(0, size, 0)
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)

    # Right face - Green
    glColor3f(0, 1, 0)
    glVertex3f(0, size, 0)
    glVertex3f(size, -size, size)
    glVertex3f(size, -size, -size)

    # Back face - Blue
    glColor3f(0, 0, 1)
    glVertex3f(0, size, 0)
    glVertex3f(size, -size, -size)
    glVertex3f(-size, -size, -size)

    # Left face - Yellow
    glColor3f(1, 1, 0)
    glVertex3f(0, size, 0)
    glVertex3f(-size, -size, -size)
    glVertex3f(-size, -size, size)

    glEnd()


def draw_sphere(radius=1.0, slices=20, stacks=20):
    """Draw a sphere using GLU utilities"""
    quad = gluNewQuadric()
    glColor3f(1, 0.5, 0)  # Orange
    gluSphere(quad, radius, slices, stacks)


def update_animation():
    """Update animation variables"""
    global animation_angle, pyramid_bounce_direction, pyramid_position, pyramid_bounce_speed

    animation_angle += 2
    if animation_angle > 360:
        animation_angle = 0

    # Animate cube rotation
    if animate_cube:
        cube_rotation[0] += 2
        cube_rotation[1] += 2

    # Animate pyramid bouncing
    if animate_pyramid:
        pyramid_position[1] += pyramid_bounce_direction * pyramid_bounce_speed
        if pyramid_position[1] > 2 or pyramid_position[1] < -2:
            pyramid_bounce_direction *= -1
        pyramid_rotation[1] += 1


def display():
    """Main display function"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    update_animation()

    # ===== CUBE =====
    glLoadIdentity()
    glTranslatef(2.5, 0, -8)
    glRotatef(cube_rotation[0], 1, 0, 0)
    glRotatef(cube_rotation[1], 0, 1, 0)
    glRotatef(cube_rotation[2], 0, 0, 1)
    glScalef(scale_values[0], scale_values[1], scale_values[2])
    draw_cube(0.8)

    # ===== PYRAMID =====
    glLoadIdentity()
    glTranslatef(-2.5, pyramid_position[1], -7)
    glRotatef(pyramid_rotation[0], 1, 0, 0)
    glRotatef(pyramid_rotation[1], 0, 1, 0)
    glRotatef(pyramid_rotation[2], 0, 0, 1)
    draw_pyramid(0.8)

    # ===== SPHERE (optional) =====
    if show_sphere:
        glLoadIdentity()
        glTranslatef(0, 0, -9)
        glRotatef(sphere_rotation[1], 0, 1, 0)
        draw_sphere(0.8)

    glutSwapBuffers()


def reshape(w, h):
    """Handle window reshape"""
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(perspective_value, w / h, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    """Handle keyboard input"""
    global cube_rotation, pyramid_position, pyramid_rotation, animate_cube, animate_pyramid
    global show_sphere, perspective_value, scale_values, sphere_rotation

    if key == b'q' or key == b'Q':
        print("Exiting program...")
        sys.exit()

    # Cube rotation controls
    elif key == b'w':  # Rotate cube up
        cube_rotation[0] += 5
    elif key == b's':  # Rotate cube down
        cube_rotation[0] -= 5
    elif key == b'a':  # Rotate cube left
        cube_rotation[1] -= 5
    elif key == b'd':  # Rotate cube right
        cube_rotation[1] += 5

    # Pyramid movement controls
    elif key == b'i':  # Move pyramid up
        pyramid_position[1] += 0.2
    elif key == b'k':  # Move pyramid down
        pyramid_position[1] -= 0.2
    elif key == b'j':  # Rotate pyramid left
        pyramid_rotation[1] -= 5
    elif key == b'l':  # Rotate pyramid right
        pyramid_rotation[1] += 5

    # Animation toggles
    elif key == b'c':  # Toggle cube animation
        animate_cube = not animate_cube
        print(f"Cube animation: {'ON' if animate_cube else 'OFF'}")
    elif key == b'p':  # Toggle pyramid animation
        animate_pyramid = not animate_pyramid
        print(f"Pyramid animation: {'ON' if animate_pyramid else 'OFF'}")

    # Sphere visibility toggle
    elif key == b'x':
        show_sphere = not show_sphere
        print(f"Sphere display: {'ON' if show_sphere else 'OFF'}")

    # Scaling controls
    elif key == b'+':
        for i in range(3):
            scale_values[i] += 0.1
        print(f"Scale: {scale_values[0]:.2f}")
    elif key == b'-':
        for i in range(3):
            scale_values[i] -= 0.1
        print(f"Scale: {scale_values[0]:.2f}")

    # Perspective controls
    elif key == b'z':  # Decrease FOV
        perspective_value -= 5
        if perspective_value < 10:
            perspective_value = 10
        print(f"FOV: {perspective_value}")
    elif key == b'Z':  # Increase FOV
        perspective_value += 5
        if perspective_value > 120:
            perspective_value = 120
        print(f"FOV: {perspective_value}")

    # Reset all
    elif key == b'r':
        cube_rotation = [0, 0, 0]
        pyramid_position = [0, 0, 0]
        pyramid_rotation = [0, 0, 0]
        sphere_rotation = [0, 0, 0]
        scale_values = [1.0, 1.0, 1.0]
        animate_cube = False
        animate_pyramid = False
        perspective_value = 45
        print("All values reset to default")

    # Help
    elif key == b'h':
        print_help()

    glutPostRedisplay()


def special_keys(key, x, y):
    """Handle special keys (arrow keys)"""
    global sphere_rotation

    if key == GLUT_KEY_UP:
        sphere_rotation[0] += 5
    elif key == GLUT_KEY_DOWN:
        sphere_rotation[0] -= 5
    elif key == GLUT_KEY_LEFT:
        sphere_rotation[1] -= 5
    elif key == GLUT_KEY_RIGHT:
        sphere_rotation[1] += 5

    glutPostRedisplay()


def print_help():
    """Print keyboard controls"""
    print("\n" + "="*50)
    print("KEYBOARD CONTROLS - Lab 9: 3D Shapes with PyOpenGL")
    print("="*50)
    print("\nCUBE ROTATION:")
    print("  W/S - Rotate up/down")
    print("  A/D - Rotate left/right")
    print("\nPYRAMID MOVEMENT:")
    print("  I/K - Move up/down")
    print("  J/L - Rotate left/right")
    print("\nANIMATION:")
    print("  C   - Toggle cube animation")
    print("  P   - Toggle pyramid animation")
    print("\nSPHERE (Exercise 5):")
    print("  X   - Toggle sphere display")
    print("  ↑/↓ - Rotate sphere up/down")
    print("  ←/→ - Rotate sphere left/right")
    print("\nSCALING (Exercise 7):")
    print("  +/- - Scale objects larger/smaller")
    print("\nPERSPECTIVE (Exercise 4):")
    print("  Z/Z(Shift) - Change FOV")
    print("\nOTHER:")
    print("  R   - Reset all to default")
    print("  H   - Show this help menu")
    print("  Q   - Quit program")
    print("="*50 + "\n")


def timer_callback(value):
    """Timer callback for continuous refresh"""
    glutPostRedisplay()
    glutTimerFunc(16, timer_callback, 0)  # ~60 FPS


def main():
    """Main function"""
    print("\n" + "="*50)
    print("Lab 9: Drawing 3D Cube and Pyramid using PyOpenGL")
    print("Student: Md Abdur Rahman Sifat")
    print("ID: 364")
    print("="*50)

    # Initialize GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutCreateWindow(b"3D Shapes - PyOpenGL (ID-364)")

    # Initialize OpenGL
    init()

    # Set callback functions
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutTimerFunc(0, timer_callback, 0)

    print_help()

    # Start the main loop
    glutMainLoop()


if __name__ == "__main__":
    main()
