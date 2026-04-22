def midpoint_circle_with_logs(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    print(f"Iteration 0: x={x}, y={y}, d={d}")

    iteration = 1
    while x < y:
        x += 1
        if d < 0:
            d = d + 2 * x + 1
        else:
            y -= 1
            d = d + 2 * (x - y) + 1
        print(f"Iteration {iteration}: x={x}, y={y}, d={d}")
        iteration += 1


midpoint_circle_with_logs(10, 10, 6)
