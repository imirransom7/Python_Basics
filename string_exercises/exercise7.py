"""
Exercise 7: String characters balance Test

Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if
all the characters in the s1 and s2. The character's position doesn't matter

Given:

Case 1:                                                     Case 2:
s1 = "Yn"                                                   s1 = "Ynf"
s2 = "PYnative"                                             s2 = "PYnative"

Expected Output:                                            Expected Output:
True                                                        False
"""

# Going to make a function that takes in two strings and returns a boolean.
# I will compare the strings by seeing if the letters from s1 are in s2 by using the "in"
# Then, the function will give the boolean


def balance(s1: str, s2: str) -> bool:
    return s1 in s2
