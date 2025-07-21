#mini exercise
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year

print(f"Hello {name}, you are {age}.")

#better version
from datetime import date

name = input("Enter your name: ").strip() #.strip() is a string method that removes leading and trailing whitespace (spaces, tabs, newlines) from a string.
                                            # name = input("Enter your name: ")  # user types "  Alice  \n"
                                            # name == "  Alice  \n"
                                            #clean_name = name.strip()
                                        # clean_name == "Alice"

try:
    birth_year = int(input("Enter your birth year: "))
    # int(...) converts (parses) the text that input() returns into an integer (a whole number).
# input() always gives you a string (e.g. "1980").
# int("1980") turns that string into the number 1980.
# You need the number so you can subtract it from 2025 to compute the age.
# If the user types something that is not a valid whole number (e.g. "abc" or "19.5"),
# int(...) raises a ValueError, which is why we later add a try/except block.
except ValueError:
    print("That doesn’t look like a valid year.")
else:
    age = date.today().year - birth_year
    print(f"Hello {name}! You are {age} years old.")

