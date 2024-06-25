"""
Exercise 11: Reverse the given string

Given:
str1 = "PYnative"

Expected Output:
evitanYP
"""

# I will create a function that takes in a string as a parameter that returns a string
# to reverse the string, I will use slicing to have the start, stop, and step go in reverse


def reverse(str1: str) -> str:
    return str1[::-1]


print(reverse("PYnative"))

# Another solution to this problem


# def reverses(str1: str) -> str:
#     # creating an empty string
#     str2 = ""
#     # iterating through the given string using its length as the range; iterating backwards
#     for i in range(len(str1) - 1, 0, -1):
#         # adding each letter the empty string
#         str2 += str1[i]
#     # returning the reversed string
#     return str2


def reversing(str1: str) -> str:
    # using the join() method with the reverse function to reverse the given string
    return "".join(reversed(str1))


print(reversing("PYnative"))
