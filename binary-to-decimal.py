''' Question '''
#write a program that converts a binary (base 2) number to decimal (base 10). 
# Your program should begin by reading the binary number from the user as a string. 
# Then program should compute the equivalent decimal number by processing each digit in the binary number. 
# Finally, your program should display the equivalent decimal number with an appropriate message

''' Algorithm '''

# Start
# Define a function binary_to_decimal(binary) to convert binary to decimal:
#   Initialize decimal to 0
#   Initialize power to the length of binary - 1
#   Loop through each digit in binary:
#       If the digit is '1':
#           Add 2 raised to the power to decimal
#       Decrement power
#   Return decimal
# Read a binary number from the user as a string
# Call binary_to_decimal(binary) with the binary number as input and store the result
# Display the equivalent decimal number with an appropriate message
# Stop


''' Flowchart '''

# (Start) --> 
# [Read binary number] --> 
# [Call binary_to_decimal(binary)] --> 
# [Display equivalent decimal number] --> 
# (Stop)

''' Source code '''

def binary_to_decimal(binary):
    """Function to convert a binary number to a decimal number."""
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        power -= 1
    return decimal

# Read binary number from the user
binary = input("Enter a binary number: ")

# Convert binary to decimal
decimal = binary_to_decimal(binary)

# Display the equivalent decimal number
print(f"The decimal equivalent of {binary} base 2 is {decimal}.")


