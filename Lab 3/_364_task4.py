import matplotlib.pyplot as plt

def drawCircle(p, q, x, y, x_points, y_points):
    x_points.extend([p + x, p - x, p + x, p - x])
    y_points.extend([q + y, q + y, q - y, q - y])

    x_points.extend([p + y, p - y, p + y, p - y])
    y_points.extend([q + x, q + x, q - x, q - x])

def bresenham_circle_points(p, q, r):
    x = 0
    y = r
    d = 3 - (2 * r)

    x_plot = []
    y_plot = []

    while x <= y:
        drawCircle(p, q, x, y, x_plot, y_plot)

        if d < 0:
            d = d + (4 * x) + 6
        else:
            d = d + 4 * (x - y) + 10
            y = y - 1

        x = x + 1

    return x_plot, y_plot
def quadrants():
    r = 15
    centers = [(30, 30), (-30, 30), (-30, -30), (30, -30)]

    plt.figure(figsize=(6, 6))

    for i, (p, q) in enumerate(centers):
        x_vals, y_vals = bresenham_circle_points(p, q, r)
        plt.scatter(x_vals, y_vals, s=5, label=f'Quadrant {i+1}')

    plt.title("Task 4: Circle in Each Quadrant")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True)
    plt.gca().set_aspect('equal')
    plt.show()

quadrants()
