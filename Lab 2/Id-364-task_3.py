def bresenham_general(x1, y1, x2, y2):
    x_points = []
    y_points = []
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    if dy > dx:
        d = 2 * dx - dy
        dS = 2 * dx
        dT = 2 * (dx - dy)
        x_points.append(x)
        y_points.append(y)
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
        d = 2 * dy - dx
        dS = 2 * dy
        dT = 2 * (dy - dx)
        x_points.append(x)
        y_points.append(y)
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

def count_pixels(x1, y1, x2, y2):
    xs, ys = bresenham_general(x1, y1, x2, y2)
    return len(xs)

if __name__ == "__main__":
    # Diagonal Line (slope = 1)
    x1, y1 = 0, 0
    x2, y2 = 5, 6

    count = count_pixels(x1, y1, x2, y2)
    print(f"Line from ({x1},{y1}) to ({x2},{y2})")
    print(f"Number of pixels drawn: {count}")

    # Mathematical expectation: max(|dx|, |dy|) + 1
    expected = max(abs(x2-x1), abs(y2-y1)) + 1
    print(f"Expected count: {expected}")

    assert count == expected
    print("Assertion Passed!")
