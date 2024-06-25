"""
Exercise 13: Split a string on hyphens

Write a program to split a given string on hyphens and display the substring.

Given:
str1 = "Emma-is-a-data-scientist"

Expected Output:

Displaying each substring

Emma
is
a
data
scientist
"""

# I am going to create a function that takes in a string that will print it out divided without
# its hyphens. To do this, I will turn the given string into a list using the split() method, splitting
# the string up into a list by the hyphens present in the string. I will then iterate through the
# newly created list and print it out by each element


def no_hyphens(str1: str):
    print("Displaying each substring\n")
    # iterating though a list split from the hyphens present in the string
    for word in str1.split("-"):
        # printing out elements
        print(word)


no_hyphens("Emma-is-a-data-scientist")
