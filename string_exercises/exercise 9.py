"""
Exercise 9: Calculate thr sim and average of the digits present in a string

Given a string s1, write a program to return the sum and average of the digits that appear in the
string, ignoring all other characters.

Given:
str1 = "PYnative29@#8496"

Expected Outcome
Sum is: 38 Average is 6.333333333333
"""

# staring with making a function that takes in one parameter that is a string, and printing out the sum and
# average of the numbers present in the string. I will find the numbers by iterating through the string to get the
# numbers using the isnumeric() method. After I get the numbers, I will then print out their sum and average


def numbers_only(s1: str):
    # creating an empty list
    num = []
    # iterating through the string
    for s in s1:
        # checking to see if the current element is a number
        if s.isnumeric():
            # appending the numbers found into the empty list and converting them to numbers
            num.append(int(s))
    # printing out the sum
    print(f"Sum is: {sum(num)}")
    # printing out the average
    print(f"Average is: {sum(num) / len(num)}")


numbers_only("PYnative29@#8496")
