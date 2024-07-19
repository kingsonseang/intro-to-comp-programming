''' Question '''

# Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
# The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
# Include appropriate headings on your columns. The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the internet.

''' Algorithm '''

# Start
# Print table heading with column labels for Celsius and Fahrenheit
# Loop over temperatures from 0 to 100 degrees Celsius in steps of 10
#   Convert each temperature from Celsius to Fahrenheit using the conversion formula
#   Display the temperature in Celsius and Fahrenheit in a formatted manner
# Stop

''' Flowchart '''

# (Start) --> [Print table heading] --> [Generate temperature conversion table] --> [Print table footer] --> (Stop)

''' Source code '''

# using a forloop to generate table structure

def celsius_to_fahrenheit(celsius):
    """Function to convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

# Print table heading with styling
print("+----------+-------------+")
print("| Celsius  | Fahrenheit  |")
print("+----------+-------------+")

# Generate and print temperature conversion table with styling
for celsius in range(0, 101, 10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"| {celsius:<8} | {fahrenheit:<11.2f} |")

# Print table footer with styling
print("+----------+-------------+")


''' Another method '''

# before using these methods install rich

    # install rich globally - not recommStoped
        # python -m pip install rich

    # or use a virtal environment

        # using venv
            # python -m venv venv
            # source venv/bin/activate
            # pip install rich

        # or using virtualenv
            # virtualenv venv
            # source venv/bin/activate
            # pip install rich

        # or using conda
            # conda create -n rich
            # conda activate rich
            # pip install rich

        # to deactivate use
            #  deactivate

# # using rich
# from rich.console import Console
# from rich.table import Table

# table = Table(title="Temperature Conversion Table",)

# columns = ["Celsius", "Fahrenheit"]

# # Add columns to the table
# for column in columns:
#     table.add_column(column)

# # Generate temperature conversion table rows
# for celsius in range(0, 101, 10):
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     table.add_row(str(celsius), f"{fahrenheit:.2f}", style='bright_green')

# # Create console instance
# console = Console()

# Print the table
console.print(table)
