''' Question '''

# A polygon is regular if its sides are all the same length and the angles between all of the adjacent sides are equal. 
# The area of a regular polygon can be computed using the following formula, 
# where s is the length of a side and n is the number of sides area= n*s^2 / 4*tan(pi/n) 
# Write a program that reads s and n from the user and then displays the area of a regular polygon constructed from these values.

''' Algorithm '''

# Start
# Declare variables: s (length of a side), n (number of sides)
# Read the length of a side (s) from the user
# Read the number of sides (n) from the user
# Calculate the area of the regular polygon using the formula:
# area = (n * s^2) / (4 * tan(pi/n))
# Display the calculated area to the user
# Stop

''' Flowchart '''

#  (Start) --> 
# [Declare variables] --> 
# /Read length of a side (s) from the user/ --> 
# /Read number of sides (n) from the user/ --> 
# [Calculate area of regular polygon] --> 
# [Display calculated area] --> 
# (Stop)

''' Source code '''

import math

# Read length of a side (s) from the user
s = float(input("Enter the length of a side of the regular polygon: "))
    
# Read number of sides (n) from the user
n = int(input("Enter the number of sides of the regular polygon: "))
    
# Calculate the area of the regular polygon using the formula
area = (n * (s ** 2)) / (4 * math.tan(math.pi / n))
    
# Display the calculated area to the user
print(f"The area of the regular polygon is: {area:.2f}")
