"""
Exercise 1: Accept numbers from a user

Write a program to accept two numbers from the user and calculate multiplication
"""

# saving number inputs to two variables
number1, number2 = int(input("Type in your first number ")), int(input("Now, type in your second number "))


# writing a function that will take in two integers as parameters
def multiplication(num1: int, num2: int):
    print(f'\nYour inputted numbers multiplied together is {num1 * num2}')


multiplication(number1, number2)
