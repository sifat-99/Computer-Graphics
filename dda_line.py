import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    # Calculate differences
    dx = x2 - x1
    dy = y2 - y1

    # Calculate steps
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    # Calculate increments
    x_inc = dx / steps
    y_inc = dy / steps

    # Initialize starting points
    x = x1
    y = y1

    # Store points for plotting
    x_coords = []
    y_coords = []

    print(f"Starting DDA from ({x1}, {y1}) to ({x2}, {y2})")
    print(f"Steps: {steps}, X Increment: {x_inc:.2f}, Y Increment: {y_inc:.2f}")
    print("-" * 30)
    print("Coordinates:")

    # Main loop
    for i in range(int(steps) + 1):
        x_plot = round(x)
        y_plot = round(y)
        x_coords.append(x_plot)
        y_coords.append(y_plot)

        print(f"Step {i}: ({x_plot}, {y_plot})")

        x += x_inc
        y += y_inc

    return x_coords, y_coords

def plot_line(x_coords, y_coords):
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, marker='o', color='b', linestyle='-')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)

    # Annotate start and end points
    if x_coords:
        plt.text(x_coords[0], y_coords[0], f'Start ({x_coords[0]}, {y_coords[0]})', fontsize=9, verticalalignment='bottom')
        plt.text(x_coords[-1], y_coords[-1], f'End ({x_coords[-1]}, {y_coords[-1]})', fontsize=9, verticalalignment='bottom')

    plt.show()

if __name__ == "__main__":
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        x_points, y_points = dda_line(x1, y1, x2, y2)
        plot_line(x_points, y_points)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except KeyboardInterrupt:
        print("\nExiting program.")

