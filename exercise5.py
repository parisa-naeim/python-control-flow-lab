# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    print("Enter the month of the year (Jan - Dec):")
    month = input()
    print("Enter the day of the month:")
    try:
        day = int(input())
    except:
        print("day should be a number")
        
    if (month == 'Dec' and day >= 21) or (month in ['Jan', 'Feb']) or (month == 'Mar' and day <= 19):
        season = "Winter"
    elif (month == 'Mar' and day >= 20) or (month in ['Apr', 'May']) or (month == 'Jun' and day <= 20):
        season = "Spring"
    elif (month == 'Jun' and day >= 21) or (month in ['Jul', 'Aug']) or (month == 'Sep' and day <= 21):
        season = "Summer"
    elif (month == 'Sep' and day >= 22) or (month in ['Oct', 'Nov']) or (month == 'Dec' and day <= 20):
        season = "Fall"
    
    print(f"{month} {day} is in {season}.")



    # Your control flow logic goes here

# Call the function
determine_season()
