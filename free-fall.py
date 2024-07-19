''' Question '''

# Create a program that determines how quickly an object is traveling when it hits the ground.
# The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0m/s.
# Assume that the acceleration due to gravity is 9.8m/s².
# You can use the formula vf = SQR ( Vi² + 2ad) to compute the final speed, vf, when the initial speed, vi, acceleration, a, distance, d, are known.

''' Algorithm '''

# (Start) -->
# [Declare variables] -->
# /Read height from the user/ -->
# [Set initial_speed to 0] -->
# [Set acceleration to 9.8] -->
# [Calculate distance fallen] -->
# [Calculate final speed] -->
# [Display final speed] -->
# (Stop)

''' Source code '''

import math

# Read height from the user
height = float(input("Enter the height from which the object is dropped (in meters): "))

# Set initial speed to 0 m/s
initial_speed = 0

# Set acceleration due to gravity
acceleration = 9.8  # m/s^2

# Calculate the distance fallen
distance_fallen = 0.5 * acceleration * height

# Calculate the final speed using the formula vf = sqrt(Vi² + 2ad)
# Vi is the initial speed (0 m/s in this case)
# a is the acceleration due to gravity (9.8 m/s²)
# d is the height from which the object is dropped
final_speed = math.sqrt((initial_speed ** 2) + (2 * acceleration * height))

# Display the final speed to the user
print(f"The final speed of the object when it hits the ground is approximately {final_speed:.2f} m/s.")
