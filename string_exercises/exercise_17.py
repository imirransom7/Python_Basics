"""
Exercise 17: Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.

Given:

str1 = "Emma25 is Data scientist50 and AI Expert"
Expected Output:

Emma25
scientist50
"""


# making a function that takes in a string and returns a string
def string_and_numbers(str1: str) -> str:
    # iterating through a list that is the string split up by spaces
    for element in str1.split(" "):
        # checking if the element string contains both a number and a string
        if element.isnumeric() and element.isalpha():
            # printing out the elements that meet the condition
            print(element)


string_and_numbers("Emma25 is Data scientist50 and AI Expert")
