"""
Exercise 1A: Create a string made of the first, middle, and last
character

Write a program to create a new string made of an input string's first, middle, and last character

Given:

str1 = "James"

Expected Output:
Jms
"""

# Starting with initializing the function that will hold one parameter that is a string
# After that, I will get the first index of the string, then the middle, and then the last.
# Then I will concatenate them together by adding them together


def first_middle_last(name: str) -> str:
    # taking the first index and adding to the middle index, then adding the last index
    return name[0] + name[len(name) // 2] + name[-1]


print(first_middle_last("James"))
print(first_middle_last('Tyler'))
