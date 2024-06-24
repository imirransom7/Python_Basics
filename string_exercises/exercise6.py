"""
Exercise 6: Create a mixed string using the following rules

Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
then the last char of s2 Next, the second char of s1 and second last char of s2, and so on. Any
leftover chars go at the end of the result

Given:
s1 = "Abc"
s2 = "Xyz"

Expected Output:
AzbycX
"""

# Going to make a function that takes in a string as a parameter that returns a string
# when that is done, I will combine the two strings as instructed by using the zip function
# I will use s1 normally but have s2 reverse when applied in the zip function
# Next, I will iterate over the zip to then add s1 and s2 together


def mixed(s1: str, s2: str) -> str:
    pass
