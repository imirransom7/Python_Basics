"""
Exercise 3: Create a new string made of the first, middle, and last
characters of each input string

Given two strings s1 and s2, write a program to return a new string made of s1 and s2's first,
middle, and last characters

Given

s1 = "America"
s2 = "Japan

Expected Output
AJrpan
"""

# Starting with creating my function that will take in two strings as parameters that returns a string
# Next will be taking s1 and s2's first letter by using [0] and adding them together. Then I will get
# the middle character by dividing the length of the string by two and flooring it, then add them together.
# After that, I will get the last letters from both by using [-1] and then add them


# creating my function to take in two strings
def first_mid_last(s1: str, s2: str) -> str:
    # getting the middle character for s1
    s1_mid = len(s1) // 2
    # getting the middle character for s2
    s2_mid = len(s2) // 2
    # adding the first, middle, and last characters from both s1 and s2
    return s1[0]+s2[0] + s1[s1_mid]+s2[s2_mid] + s1[-1]+s2[-1]


