"""
Exercise 12: Find the last position of a given string

Write a program to find the last position of a substring "Emma" in a given string

Given:
str1 = "Emma is a data scientist who knows Python. Emma works at Google."

Expected OutputL
Last occurrence of Emma starts at index 43
"""

# I will create a function that will take two strings as parameters that returns an integer
# To find the last occurrence of Emma where that index is, I can use the builtin method .rfind(), which
# returns the last occurrence of the inputted element's index. Once that is done, I will return the index


def last_index(str1: str, str2: str) -> int:
    return str1.rfind(str2)


print("Last occurrence of Emma starts at index", last_index(
 "Emma is a data scientist who knows Python. Emma works at google.", "Emma"))
