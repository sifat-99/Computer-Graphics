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
def filled_circle():
    p, q = 0, 0
    r = 20

    x = 0
    y = r
    d = 3 - (2 * r)

    fill_x = []
    fill_y = []

    def add_fill_lines(p, q, x, y):
        for val_x in range(p - x, p + x + 1):
            fill_x.append(val_x); fill_y.append(q + y)
            fill_x.append(val_x); fill_y.append(q - y)

        for val_x in range(p - y, p + y + 1):
            fill_x.append(val_x); fill_y.append(q + x)
            fill_x.append(val_x); fill_y.append(q - x)

    while x <= y:
        add_fill_lines(p, q, x, y)
        if d < 0:
            d = d + (4 * x) + 6
        else:
            d = d + 4 * (x - y) + 10
            y = y - 1
        x = x + 1

    plt.figure(figsize=(6, 6))
    plt.scatter(fill_x, fill_y, s=15, marker='s', color='green')
    plt.title("Task 5: Filled Circle")
    plt.gca().set_aspect('equal')
    plt.show()

filled_circle()
