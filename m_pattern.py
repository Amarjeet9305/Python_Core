def dynamic_m(n):
    # validation
    if n < 3 or n % 2 == 0:
        print("❌ Enter only odd numbers >= 3")
        return
    
    size = 2 * n + 1   # total columns
    mid = size // 2    # middle index
    
    # Loop for each row
    for i in range(n):
        row = []
        for j in range(size):
            # Top row → print e and *
            if i == 0:
                if j <= n or j >= size - n - 1:   # edges → 'e'
                    row.append("e")
                else:                             # middle → '*'
                    row.append("*")
            
            # Other rows → V-shape stars and borders
            else:
                if j == 0 or j == size - 1:       # side stars
                    row.append("*")
                elif j == mid - i or j == mid + i: # diagonal stars
                    row.append("*")
                else:
                    row.append(" ")
        print(" ".join(row))


# Test
dynamic_m(3)
print()
dynamic_m(5)
