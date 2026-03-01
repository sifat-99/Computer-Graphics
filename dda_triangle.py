import matplotlib.pyplot as plt
from dda_line import dda_line

def plot_triangle(x1, y1, x2, y2, x3, y3):
    print("\nCalculating Edge AB:")
    x_ab, y_ab = dda_line(x1, y1, x2, y2)
    print("\nCalculating Edge BC:")
    x_bc, y_bc = dda_line(x2, y2, x3, y3)

    print("\nCalculating Edge CA:")
    x_ca, y_ca = dda_line(x3, y3, x1, y1)

    plt.figure(figsize=(8, 6))

    # Plot each edge
    # We strip the markers slightly to avoid cluttering if points are dense, or keep them if needed.
    # Keeping them as user requested DDA which is point based.
    plt.plot(x_ab, y_ab, marker='o', color='b', label='Edge AB')
    plt.plot(x_bc, y_bc, marker='o', color='g', label='Edge BC')
    plt.plot(x_ca, y_ca, marker='o', color='r', label='Edge CA')

    # Annotate vertices
    plt.text(x1, y1, f'A ({x1}, {y1})', fontsize=10, fontweight='bold', color='black')
    plt.text(x2, y2, f'B ({x2}, {y2})', fontsize=10, fontweight='bold', color='black')
    plt.text(x3, y3, f'C ({x3}, {y3})', fontsize=10, fontweight='bold', color='black')

    plt.title("DDA Triangle Drawing")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    try:
        print("Enter coordinates for Vertex A:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))

        print("Enter coordinates for Vertex B:")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        print("Enter coordinates for Vertex C:")
        x3 = float(input("x3: "))
        y3 = float(input("y3: "))

        plot_triangle(x1, y1, x2, y2, x3, y3)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except KeyboardInterrupt:
        print("\nExiting program.")
