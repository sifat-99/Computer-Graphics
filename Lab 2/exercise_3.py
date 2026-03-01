import matplotlib.pyplot as plt

def bresenham_line_negative_slope(x1, y1, x2, y2):
    # This function handles lines where |slope| < 1, including negative slopes.
    # It does NOT handle steep lines (|slope| > 1) - that is for Home Task 1.

    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine direction
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Check if slope is gentle (|m| <= 1)
    if dy > dx:
        print("This specific specific implementation is for gentle slopes (|m| <= 1).")
        print("For steep slopes, see Home Task 1.")
        return

    # Constants
    dS = 2 * dy
    dT = 2 * (dy - dx)
    d = 2 * dy - dx

    x_points = [x]
    y_points = [y]

    # We loop dx times.
    # Note: Using a raw counter or comparing x != x2

    print(f"Drawing from ({x1},{y1}) to ({x2},{y2})")
    print(f"dx={dx}, dy={dy}, sx={sx}, sy={sy}")

    # To handle the loop correctly with direction sx
    # We iterate x from x1 to x2 (inclusive of start, exclusive of end in a simple rance, but we need to supply end)
    # The condition x != x2 might be risky if we overshoot, but with integer steps it's fine.

    i = 0
    while i < dx:
        x += sx
        if d < 0:
            d = d + dS
        else:
            d = d + dT
            y += sy

        x_points.append(x)
        y_points.append(y)
        i += 1

    plt.plot(x_points, y_points, marker='o')
    plt.title(f"Bresenham's Line (Negative Slope Support) ({x1},{y1}) to ({x2},{y2})")
    plt.grid(True)
    plt.gca().invert_yaxis() # Optional, but standard coordinate system y is up. In computer graphics screen usually y is down.
                             # But matplotlib is cartesian (y up). I'll stick to variable values.
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if __name__ == "__main__":
    # Test with negative slope |m| < 1
    # Example: (0, 0) to (8, -4) -> slope -0.5
    bresenham_line_negative_slope(0, 0, 8, -4)
