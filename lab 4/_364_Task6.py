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


def midpoint_circle_skipped(xc, yc, r):
    x = 0
    y = r
    d = 1 - r

    # Iteration 0 (Even)
    plot_circle_points(xc, yc, x, y)

    iteration = 1
    while x < y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            y -= 1
            d = d + 2 * (x - y) + 1

        # Plot only if iteration is even [cite: 47]
        if iteration % 2 == 0:
            plot_circle_points(xc, yc, x, y)
        iteration += 1


plt.figure(figsize=(6, 6))
midpoint_circle_skipped(10, 10, 6)
plt.title("Exercise 6: Even Iterations Only")
plt.gca().set_aspect("equal")
plt.grid(True)
plt.show()
