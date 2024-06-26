"""
Exercise 14: Print a downward Half-Pyramid Pattern of Star
(asterisk)
* * * * *
* * * *
* * *
* *
*
"""

# I will create a function that will take in a number and print out a down Half-Pyramid Patter of Star
# I will then create a for loop that decrements the number given until it reaches 0.
# To get the star pattern, I will multiply the current number with a string asterisk: "*" so that
# I that the same number of stars will print out


def half_pyramid(num: int):
    # creating a for loop with the range of the given number
    for i in range(num, 0, -1):
        # printing the amount of asterisks by the current index
        print(i * "* ")


half_pyramid(5)
