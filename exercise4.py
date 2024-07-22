# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    print("Is it cold?")
    cold = input() == "yes"
    print("Is it raining?")
    raining = input() == "yes"
    if cold and raining:
        print("Wear a waterproof coat.")
    elif cold and not raining:
        print("Wear a warm coat.")
    elif not cold and raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

    # Your control flow logic goes here

# Call the function
weather_advice()
