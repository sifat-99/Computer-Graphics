import matplotlib.pyplot as plt


def midpoint_circle_input():
    try:
        xc = int(input("Enter center xc: "))
        yc = int(input("Enter center yc: "))
        r = int(input("Enter radius r: "))

        x, y = 0, r
        d = 1 - r

        plt.figure(figsize=(6, 6))
        plot_symmetric(xc, yc, x, y)

        while x < y:
            x += 1
            if d < 0:
                d = d + 2 * x + 1
            else:
                y -= 1
                d = d + 2 * (x - y) + 1
            plot_symmetric(xc, yc, x, y)

        plt.gca().set_aspect("equal")
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Please enter valid integers.")


def plot_symmetric(xc, yc, x, y):
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
        plt.scatter(px, py, color="red")


midpoint_circle_input()
