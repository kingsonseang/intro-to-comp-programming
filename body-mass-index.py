''' Question '''

# Write a program that computes the body mass index (BMI) of an individual. 
# You program should begin by reading a height and weight from the user. 
# Then it shou use one of the following two formulas to compute the BMI before displaying it. 
# you read the height in inches and the weight in pounds then body mass index computed using the following formula:
#
#   BMI =  weight / height* height *703.
#

''' Algorithm ''' # not complete as full question is not provided here

# Start
# Declare variables: height (in inches), weight (in pounds), BMI
# Read the height (in inches) from the user
# Read the weight (in pounds) from the user
# Calculate the BMI using the formula: BMI = weight / (height * height) * 703
# Display the calculated BMI to the user
# Stop


''' Flowchart '''

# (Start) --> 
# [Declare variables] --> 
# /Read height (in inches) from the user/ --> 
# /Read weight (in pounds) from the user/ --> 
# [Calculate BMI using the formula] --> 
# [Display calculated BMI to the user] --> 
# (Stop)

''' Source code '''


# Read height (in inches) from the user
height = float(input("Enter your height (in inches): "))
    
# Read weight (in pounds) from the user
weight = float(input("Enter your weight (in pounds): "))
    
# Calculate the BMI using the formula
bmi = (weight / (height * height)) * 703
    
# Display the calculated BMI to the user
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
    