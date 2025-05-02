# Question: Write a python program to recursively compute the sum of number in a list using 
# slicing
# Defining the function 

def recursive_sum(lst):
    # Weather checking lst is empty
    
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[0:-1])

# Taking a lst 

numbers =[10,20,30,40,50]

# Function calling compute the sum of number

print(recursive_sum(numbers))