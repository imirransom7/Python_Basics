"""
Exercise 5: Count all letters, digits, and special symbols from a given
string

Given
str = "P@#yn26at^&i5ve"

Expected Outcome:
Total counts of chars, digits, and symbols

Chars = 8
Digits = 3
Symbol = 4
"""

# Starting with creating a function that takes in one string as a parameter that prints out three counters
# I will have three separate counters for the numbers, letters, and symbols. Next, I will then
# iterate through the string so that I can then count the numbers and such. After that, the function will
# print out the counters for the letters, numbers, and symbols


def let_num_sym(string: str):
    # declaring three separate counters
    letters, digits, symbols = 0, 0, 0
    # iterating through the string
    for s in string:
        # checking if element is a letter
        if s.islower():
            # adding to counter
            letters += 1
        # checking for numbers:
        elif s.isnumeric():
            # adding to counter
            digits += 1
        # if it is not a number or letter, then it is a symbol
        else:
            symbols += 1

        print(f"Letters = {letters}", f"\nDigits = {digits}", f"\nSymbols = {symbols}")



