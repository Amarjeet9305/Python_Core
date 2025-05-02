# Write a program calculate sum of all number from 1 to a given number
# let auppose we have 1 to 10 number is calculate all number and expected output is 55.
# Approac is First we are using accept  input form user python and second is
# calculate sum and average in python

# Drive code

# Store all sum value is s

s = 0

# take user input 1 to a
a = int(input("Enter the element:"))

# Using for loop and range function: run loop n times and n+1

for i in range(1,a+1,1):
    
    # add current number sum of element
    s += i
print("\n")
print("sum is:",s)    


