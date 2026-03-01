import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    x_points = [round(x)]
    y_points = [round(y)]

    for _ in range(steps):
        x += x_inc
        y += y_inc
        x_points.append(round(x))
        y_points.append(round(y))

    return x_points, y_points

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

if __name__ == "__main__":
    # Test Line
    x1, y1 = 2, 3
    x2, y2 = 12, 8

    dda_x, dda_y = dda_line(x1, y1, x2, y2)
    bre_x, bre_y = bresenham_general(x1, y1, x2, y2)

    print("DDA Points:       ", list(zip(dda_x, dda_y)))
    print("Bresenham Points: ", list(zip(bre_x, bre_y)))

    if list(zip(dda_x, dda_y)) == list(zip(bre_x, bre_y)):
        print("\nResult: Both algorithms produced the SAME pixels.")
    else:
        print("\nResult: Algorithms produced DIFFERENT pixels.")

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(dda_x, dda_y, 'b-o', label='DDA')
    plt.title("DDA Algorithm")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(bre_x, bre_y, 'r-o', label='Bresenham')
    plt.title("Bresenham Algorithm")
    plt.grid(True)

    plt.show()
