
def castle(n):
    for i in range(n-1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(i + 1):
            print("* ", end="")
        
        for j in range(n * 5 - 2 * i - 1):
            print(" ", end="")
        
        for j in range(i + 1):
            print("* ", end="")
        print()

    for i in range(n + 2):
        row = " " * (n+1)
        
        if i < n+1:
            row += "e" + " " * (n-3)
        else:
            row += " ".join("e" for _ in range(n))

        row += " " * n

        if i < 2:
            row += " " * (2*n-1)
        else:
            k = i - 2
            if k == 0 or k == n-1:
                row += " ".join("e" for _ in range(n))
            else:
                row += "e" + " " * (2*n-3) + "e"

        row += " " * n

        if i < n+1:
            row += "e" + " " * (n-1)

        print(row)


# sample runs
castle(3)
print()
castle(5)
print()

castle

 
                        