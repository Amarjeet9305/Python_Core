# Write a program area of rectangle in python
# We know that area of rectangle formula is a : A =l*b
# Approach take two variable on user input then putting formula with third variable


# l = int(input("Enter the length of area in cm:"))

# b = int(input("Enter the breadth of area in cm:"))

# # takig third variable

# a = l * b

# # Show the output

# print("Calculate the area:",a)

# Write area of program using def function
# Taking input user

def calculate_area(length,breadth):
    return length*breadth  # Return the l*b recursive

# Define variable taking input user

l = float(input("Enter the number of lenth in cm:"))

b = float(input("Enter the number of breadth in cm"))

# Call the function with user provide value

area = calculate_area(l,b)

# Print the calculate the area

print("Calculate the area:",area)


