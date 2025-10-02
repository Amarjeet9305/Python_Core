def webkul_pattern(n):
    if n < 3 or n % 2 == 0:
        print("Input must be an odd number >= 3")
        return
    size = 2 * n + 1
    
    for i in range(n):
        for j in range(size):
            if j == 0 or j == size - 1:
                print("*", end=" ")
            elif i == 0:
                print("e", end=" ")
            elif j == i or j == size - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
# Function calling
webkul_pattern(3)     
print()      
webkul_pattern(5)         
                
                        