def grid_pattern(n):
    if n < 3 or n % 2 == 0:
        print("Invalid input! Please enter an odd number >= 3")
        return

    # dimensions
    tri_height = (n + 1) // 2
    rows = 1 + n + tri_height
    cols = (n + 2) + 3 + n     # make it wide enough

    # initialize grid with spaces
    grid = [[" " for _ in range(cols)] for _ in range(rows)]

    # 1. Top horizontal (n+2 'e'), offset by 2
    top_start = 2
    top_end = top_start + (n + 2)
    for c in range(top_start, top_end):
        grid[0][c] = "e"

    # 2. Vertical legs
    left_col = 0
    right_col = top_end - 1
    for r in range(1, n + 1):
        grid[r][left_col] = "e"
        grid[r][right_col] = "e"

    # 3. Inverted triangle of stars under right leg
    base_row = 1 + n
    for k in range(tri_height):
        width = n - 2 * k
        left = right_col - (width - 1) // 2
        for c in range(left, left + width):
            grid[base_row + k][c] = "*"

    # Print the grid
    for row in grid:
        print(" ".join(row).rstrip())


# Example runs
print("n = 3\n")
grid_pattern(3)

# print("\nn = 5\n")
# grid_pattern(5)
