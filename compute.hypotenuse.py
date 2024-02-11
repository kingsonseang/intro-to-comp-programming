''' Question '''
# Write a function that takes the lengths of the two shorter sides of a right triangle as its parameters. 
# Return the hypotenuse of the triangle, computed using Pythagorean theorem, as the function's result. 
# Include a main program that reads the lengths of the shorter sides of a right triangle from the user, uses your function to compute the length of the hypotenuse, and displays the result

''' Algorithm '''

# Start
# Define a function calculate_hypotenuse(side1, side2):
#   Calculate the hypotenuse using the Pythagorean theorem: hypotenuse = sqrt(side1^2 + side2^2)
#   Return the calculated hypotenuse
# Define a main function to interact with the user:
#   Read the lengths of the two shorter sides of the right triangle from the user
#   Call calculate_hypotenuse function with the two shorter side lengths as arguments
#   Display the calculated hypotenuse
# Stop

''' Flowchart '''

# (start) --> 
# [Read shorter side lengths from user] --> 
# [Call calculate_hypotenuse function] --> 
# [Display calculated hypotenuse] --> 
# (end)

''' Source code '''

def calculate_hypotenuse(side1, side2):
    """Function to calculate the hypotenuse of a right triangle."""
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    return hypotenuse

def main():
    # Read the lengths of the shorter sides of the right triangle from the user
    side1 = float(input("Enter the length of the first shorter side: "))
    side2 = float(input("Enter the length of the second shorter side: "))

    # Calculate the hypotenuse using the function
    hypotenuse = calculate_hypotenuse(side1, side2)

    # Display the result
    print(f"The length of the hypotenuse is: {hypotenuse}")

if __name__ == "__main__":
    main()



