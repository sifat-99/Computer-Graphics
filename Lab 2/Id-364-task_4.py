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

def draw_polygon(vertices):
    # vertices: list of (x, y) tuples
    # Connect v[i] to v[i+1], and last to first

    all_x = []
    all_y = []

    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n] # Wrap around to first point

        xs, ys = bresenham_general(x1, y1, x2, y2)
        all_x.extend(xs)
        all_y.extend(ys)

        # Plot each line segment immediately to keep color consistent or logic simple
        # plt.plot(xs, ys, 'b-')

    plt.plot(all_x, all_y, 'bo', markersize=2)
    plt.title(f"Multiple Lines (Polygon with {n} vertices)")
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    # Define a Triangle
    triangle = [(2, 2), (8, 2), (5, 8)]
    print("Drawing Triangle...")
    draw_polygon(triangle)

    # Define a Square
    # square = [(10, 10), (10, 20), (20, 20), (20, 10)]
    # draw_polygon(square)
