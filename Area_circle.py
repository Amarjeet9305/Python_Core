# Write a program an calclute the area of circle
# We know that area of circle formula A = πr2 

# # Taking a variable on area of radius

# r = float(input("Enter the area of radius in cm:"))

# # Taking second variable on putting formula we know that Pi value 3.14

# a = 3.14*(r*r)

# # Print the output of area of circle

# print("Calcluate the area of circle:",a)


# Write a program using def function

def area_circle(pi,radius):
    return pi*radius

# Taking user input on radius of circle

p = float(input("Enter the pi vlaue:"))

r = float(input("Enter the value of radius in cm:"))

# Calling the function provide user value

circ = area_circle(p,r*r)

# Print the output

print("Calclute the circle area:",circ)