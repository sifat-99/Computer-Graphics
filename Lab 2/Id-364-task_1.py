import matplotlib.pyplot as plt

def bresenham_general(x1, y1, x2, y2):
    # Setup for verification/plotting
    x_points = []
    y_points = []

    x, y = x1, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Check if the line is steep or gentle
    if dy > dx:
        # Steep line (Drive by Y)
        # We effectively swap dx and dy usage for the error calculation

        d = 2 * dx - dy
        dS = 2 * dx
        dT = 2 * (dx - dy)

        x_points.append(x)
        y_points.append(y)

        # Loop dy times
        for _ in range(dy):
            y += sy
            if d < 0:
                d += dS
            else:
                x += sx
                d += dT
            x_points.append(x)
            y_points.append(y)

    else:
        # Gentle line (Drive by X)
        d = 2 * dy - dx
        dS = 2 * dy
        dT = 2 * (dy - dx)

        x_points.append(x)
        y_points.append(y)

        # Loop dx times
        for _ in range(dx):
            x += sx
            if d < 0:
                d += dS
            else:
                y += sy
                d += dT
            x_points.append(x)
            y_points.append(y)

    return x_points, y_points

if __name__ == "__main__":
    # Test cases covering generic octants
    # 1. Gentle Positive: (0,0) -> (8, 4)
    # 2. Steep Positive: (0,0) -> (4, 8)
    # 3. Steep Negative: (0,0) -> (4, -8)
    # 4. Gentle Negative: (0,0) -> (8, -4)
    # And reverses...

    test_lines = [
        (0, 0, 8, 4),    # Octant 1 (Gentle +)
        (0, 0, 4, 8),    # Octant 2 (Steep +)
        (0, 0, -4, 8),   # Octant 3 (Steep -)
        (0, 0, -8, 4),   # Octant 4 (Gentle -)
        (0, 0, -8, -4),  # Octant 5 (Gentle + reversed logic)
        (0, 0, -4, -8),  # Octant 6 (Steep + reversed logic)
        (0, 0, 4, -8),   # Octant 7 (Steep - reversed logic)
        (0, 0, 8, -4)    # Octant 8 (Gentle - reversed logic)
    ]

    plt.figure(figsize=(10, 10))

    for (x1, y1, x2, y2) in test_lines:
        xs, ys = bresenham_general(x1, y1, x2, y2)
        plt.plot(xs, ys, marker='o', label=f"({x1},{y1})->({x2},{y2})")

    plt.title("Bresenham General (All 8 Octants)")
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
