"""
Exercise 16: Removal of all characters from a string except integers

Given:
str1 = 'I am 25 years and 10 months old'

Expected Output:
2510
"""

# I am going to create a function that will take in a string as a parameter and return a number from all
# the numbers combined from the string. I will iterate through the string and extract the numbers using the
# isnumeric() method. Then, I will return the string number while casting int() over it so that it is converted
# into an integer


def only_numbers(str1: str) -> int:
    # creating an empty string
    nums = ""
    # searching for the numbers in the string
    for number in str1:
        if number.isnumeric():
            nums += number
    return int(nums)


print(only_numbers('I am 25 years and 10 months old'))
