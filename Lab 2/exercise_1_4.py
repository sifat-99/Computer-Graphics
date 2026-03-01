import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2})")

    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    # Constants
    dS = 2 * dy
    dT = 2 * (dy - dx)
    d = 2 * dy - dx

    x_points = [x]
    y_points = [y]

    print(f"{'k':<5} {'d':<10} {'(x, y)':<15}")
    print("-" * 30)
    k = 0
    print(f"{k:<5} {'-':<10} ({x}, {y})")

    while x < x2:
        x += 1
        if d < 0:
            d = d + dS
        else:
            d = d + dT
            y += 1

        x_points.append(x)
        y_points.append(y)
        k += 1
        print(f"{k:<5} {d:<10} ({x}, {y})")

    plt.plot(x_points, y_points, marker='o')
    plt.title("Bresenham's Line Drawing (Ex 1 & 4)")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# Exercise 1: Draw a line from (0, 0) to (8, 5)
if __name__ == "__main__":
    bresenham_line(0, 0, 8, 5)
