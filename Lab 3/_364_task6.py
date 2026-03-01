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
def olympic_rings():
    r = 45
    rings = [
        (-100, 0, 'blue'),
        (0, 0, 'black'),
        (100, 0, 'red'),
        (-50, -50, 'orange'),
        (50, -50, 'green')
    ]

    plt.figure(figsize=(10, 6))

    for p, q, color in rings:
        x_vals, y_vals = bresenham_circle_points(p, q, r)
        # s=40 creates thick points to mimic ring thickness
        plt.scatter(x_vals, y_vals, s=40, color=color, label=color)

    plt.title("Task 6: Olympic Rings Logo")
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.show()

olympic_rings()
