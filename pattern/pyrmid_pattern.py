def pyrmid_patter(n):
    for i in range(n):
        # Print space
        for j in range(n-i-1):
            print(" ",end="")
        # Print Stars
        for j in range(2*i+1):
            print("*",end="")
        print()        
# Driver code
pyrmid_patter(3)           
