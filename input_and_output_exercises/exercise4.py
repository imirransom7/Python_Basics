"""
Exercise 4: Display float number with 2 decimal places using print()

Given:
num = 458.541315

Expected Output
458.54
"""

# I am going to make a function that takes in a float as a parameter and print that float
# with only two decimal places. To do this, I wil b e using the round function


def round_to_two(num: float):
    print(round(num, 2))


round_to_two(458.541315)


# Here is another solution using formatting

number = 458.541315
print('%.2f' % number)
