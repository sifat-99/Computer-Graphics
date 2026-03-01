import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    dS = 2 * dy
    dT = 2 * (dy - dx)
    d = 2 * dy - dx

    x_points = [x]
    y_points = [y]

    while x < x2:
        x += 1
        if d < 0:
            d = d + dS
        else:
            d = d + dT
            y += 1
        x_points.append(x)
        y_points.append(y)

    plt.plot(x_points, y_points, marker='o')
    plt.title(f"Bresenham's Line ({x1},{y1}) to ({x2},{y2})")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if __name__ == "__main__":
    try:
        print("Enter coordinates for the line:")
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))

        # NOTE: This basic implementation assumes x1 < x2 and 0 < slope < 1
        # For a robust version, see later exercises.
        if x1 > x2:
            print("Warning: This basic implementation expects x1 < x2.")
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        bresenham_line(x1, y1, x2, y2)
    except ValueError:
        print("Please enter valid integers.")
