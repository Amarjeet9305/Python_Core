def diamond_pattern(n):
    if n < 3 or n % 2 == 0:
        print("Enter odd number n > 3:")
        return
    size = 2*n - 1
    for i in range(size):
        for j in range(size):
            # Border
            
            if i == 0 or i == size-1 or j == 0 or j == size -1:
                print("*", end=" ")
            elif abs(i - (n-1)) + abs(j - (n-1)) == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
# Function calling
diamond_pattern(5)                        