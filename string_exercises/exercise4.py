"""
Exercise 4: Arrange the string characters such that lowercase letters
should come first

Given string contains a combination of the lower and upper case letters. Write a program ro
arrange the characters of a string so that lowercase letters should come first
"""

# I will start by making a function that takes in a string as a parameter that returns a string
# Then I will check for the string's lowercase letters and save it to a variable, and do the same
# for the uppercase letters to a different variable. After that is done, all that is needed is to concatenate
# them both together, making sure the lowercase letters are first


def lower_and_upper(string: str) -> str:
    # creating an empty string variable for the lowercase letters
    s1 = ""
    # now doing the same for the uppercase letters
    s2 = ""
    # iterating through the string
    for s in string:
        # checking if element is lowercase
        if s.islower():
            s1 += s
        # if it is not lowercase, then it must be uppercase
        else:
            s2 += s
    return s1 + s2


