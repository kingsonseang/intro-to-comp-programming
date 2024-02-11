''' Question '''

# create a program that reads the duration from the user as number of days, hours, minutes, and seconds. 
# Compute and display the total number of seconds represemnted by its duration.

''' Algorithm '''

# Start
# Declare variables: days, hours, minutes, seconds
# Read the number of days from the user
# Read the number of hours from the user
# Read the number of minutes from the user
# Read the number of seconds from the user
# Convert days, hours, minutes to seconds and add to seconds variable
# Add seconds entered by the user to seconds variable
# Display the total number of seconds
# Stop

''' Flowchart '''
# (Start) --> 
# [Declare variables] --> 
# /Read days from the user/ --> 
# /Read hours from the user/ --> 
# /Read minutes from the user/ --> 
# /Read seconds from the user/ --> 
# [Convert days, hours, minutes to seconds and add to seconds variable] --> 
# [Add seconds entered by the user to seconds variable] --> 
# [Display total number of seconds] --> (Stop)


''' Source code '''

# Read the number of days, hours, minutes, and seconds from the user
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

# Convert days, hours, minutes to seconds and add to seconds variable
total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

# Display the total number of seconds
print(f"The total number of seconds represented by the duration is: {total_seconds} seconds.")