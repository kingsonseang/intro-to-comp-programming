''' Question '''

# Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number. 
# For example, if the user enters 3141 then your program should display 3 + 1 + 4 + 1 = 9'

''' Algorithm '''

# Start
# Declare variables: num (four-digit integer), sum_digits
# Read a four-digit integer (num) from the user
# Check if the number has exactly four digits
#   If not, display an error message and stop
# Extract each digit from the number and add them to sum_digits
# Display the sum of the digits to the user
# Stop

''' Flowchart '''

# (Start) --> 
# [Declare variables] --> 
# /Read a four-digit integer from the user/ --> 
# [Check if the number has exactly four digits]
#    |
#    | No
#    v
#  [Display error message and stop]
#    |
#    | Yes
#    v
#  [Extract each digit and add to sum_digits] --> 
# [Display sum of digits to the user] --> 
# (Stop)

''' Source code '''

# Read a four-digit integer from the user
num = int(input("Enter a four-digit integer: "))
    
# Check if the number has exactly four digits
if 1000 <= num <= 9999:
    # Extract each digit and add to sum_digits
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
        
    # Display the sum of the digits to the user
    print("The sum of the digits in the number is:", sum_digits)
else:
    print("Please enter a valid four-digit integer.")

