def hill_climbing_pattern(n):
    if n < 3 or n % 2 == 0:
        print("Enter an odd number >= 3")
        return

    for i in range(n):  # rows
        # spaces before stars
        for j in range(n - i - 1):
            print(" ", end=" ")
        # stars
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()

# Test runs
hill_climbing_pattern(3)
print()
hill_climbing_pattern(5)
