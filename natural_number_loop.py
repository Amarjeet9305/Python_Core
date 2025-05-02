# Write a program  print first number using while loop

# i=1
# while i<=10:
#     i += 1
#     print(i)

# Write a program in pattern using loop
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5   

# Solution are first we know total row is 5
# So we have to run the outer loop 5 using for loop and range function.
# Run inner loop 1+i time using for loop and range function.


# total number of row is 6

total_row = 6

# Define the outer loop using for loop and range function

for i in range(1,total_row+1,1):
    # Define inner using for loop and range()
    for j in range(1,i+1):
        print(j,end='')
    # Empty line after each row
    print("")
    
       