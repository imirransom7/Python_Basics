"""
EXERCISE 1: Calculate the multiplication and sum of two numbers

Given two integer numbers, return their product only if the product is equal to or lower than 1000.
Otherwise, return their sum
"""


# Creating a function that will take in two integers
def calculate(num1: int, num2: int) -> int:
    # saving the product of num1 and num2
    num3 = num1 * num2
    # returning the product if the product is equal to or under 1000
    if num3 <= 1000:
        return num3
    # if the product is not equal to or lower than 1000, returning the sum
    else:
        return num1 + num2


print(calculate(20, 30))
print(calculate(40, 30))
