"""
Exercise 2: Append new string in the middle of a given string

Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the
middle of s1
"""

# I will start of with making a function that takes in two parameters that are strings
# Then I will subtract the length of the first string, s1, by two to get the middle so that I can use slicing
# to fit the s2 in the middle of s1, and then add on the last parts s1 right after s2

# creating my function


def put_in_middle(s1: str, s2: str) -> str:
    # saving the middle index sonce it will be used again
    s1_middle = len(s1) // 2
    # returning s2 in the middle od s1 using slicing
    return s1[:s1_middle] + s2 + s1[s1_middle:]


