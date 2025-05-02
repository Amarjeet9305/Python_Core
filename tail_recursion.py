# Write a program to implement tail recursion to sum list of integers without using loops.
# Define the function

import numbers
import tarfile


def tail_recursion_sum(lst,acc=0):
    if not lst:  # if lst is empty then return acc
        return acc
    return tail_recursion_sum(lst[1:],acc + lst[0])  # Recursive call with update sum

# Driver code

numbers = [1,2,3,5,4]

# Function calling recursivel output

print(tail_recursion_sum(numbers))
        
        
    