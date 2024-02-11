''' Question '''

# The volume of a cylinder can be computed by multiplying the area of its circular base by ots height.
# Write a program that reads theradius of the cylinder, along with its height, from the user and computes its volume.
# Display the result to one decimal place

''' Algorithm '''

# Start
# Declear variable radius
# Read the radius of the cylinder as float valu from the user
# Calculate the area of the circular base using the formula area A = π x r² and assign to the variable radius
# Declear variable height
# Read the height of the cylinder as float valu from the user
# calculate the volume of the cylinder using the formula volume V = A x h and assign to the variable volume
# Display the result to one decimal place
# Stop

''' Flowchart '''

# (Start) --> [Declare variable radius] --> o
# o --> [Read radius from the user] --> o
# o --> [Calculate area A = π x r²] --> o
# o --> [Declare variable height] --> o
# o --> [Read height from the user] --> o
# o --> [Calculate volume V = A x h] --> o
# o --> [Display result] --> (Stop)


''' Source code '''

import math

print("To calculate the Volume of a Cylinder,\nWe Start by calculating the area of the cylinder by using the formular: \n\n    A = π x r²\n")

# declear variable and read input
radius = float(input("Please provide the radius (r) of the cylinder: "))

area = math.pi * radius ** 2 # calculate circular base

print("\nNow that we have the area of the circular base,\nWe calculate the volue of the cylinder by using the formular: \n\n    V = A x h\n")

height = float(input("Please provide the height (h) of the cylinder: "))

# Calculate the volume of the cylinder
volume = area * height

# Printing the result
print(f"\nThe volume of the cylinder is: {volume:.1f}")