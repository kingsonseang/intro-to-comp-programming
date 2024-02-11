''' Question '''

# The length of a month varies from 28 to 31 days. 
# In this exercise you will create a program that reads the name of a month from the user as a string. 
# Then your program should display the number of days in that month. Display "28 or 29 days" for February so that leap years are addressed.

''' Algorithm '''

# Start
# Declare a dictionary to store the number of days in each month
# Read the name of the month from the user
# Check if the entered month is February
#   If yes, check if it's a leap year
#       If yes, display "29 days"
#       If no, display "28 days"
#   If no, look up the number of days in the dictionary for the entered month
#       Display the number of days in the entered month
# Stop

''' Flowchart '''
# (Start) --> [Declare dictionary for month days] --> [Read name of month from user] --> [Is the entered month February?]
#    |
#    | Yes
#    |
#    v
#  [Is it a leap year?]
#    |
#    | Yes
#    | 
#    v
#  [Display "29 days"]
#    |
#    | No
#    |
#    v
#  [Display "28 days"]
#    |
#    |
#    v
# [Look up number of days in dictionary for entered month] --> 
# [Display number of days in entered month] --> 
# (Stop)

''' Source code '''

# Declare a dictionary to store the number of days in each month
month_days = {
    "january": 31,
    "february": "28 or 29",
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

# Read the name of the month from the user
month = input("Enter the name of a month: ")

# Check if the entered month is February
if month.lower() == "february":
    leap_year = input("Is it a leap year? (yes/no): ")
    if leap_year.lower() == "yes":
        print("29 days")
    else:
        print("28 days")
else:
    # Look up the number of days in the dictionary for the entered month
    days = month_days.get(month.lower(), "Invalid month")
    if days != "Invalid month":
        print(f"{days} days")
    else:
        print("Invalid month entered.")

