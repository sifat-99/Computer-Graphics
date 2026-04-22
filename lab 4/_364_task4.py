import matplotlib.pyplot as plt


def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    ]
    for px, py in points:
        plt.scatter(px, py, color="blue")


def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            y -= 1
            d = d + 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)


plt.figure(figsize=(6, 6))
midpoint_circle(20, 25, 6)
plt.title("Exercise 4: Shifted Center (20, 25)")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.show()
