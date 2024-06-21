"""
Exercise 5: Accept a list of float numbers as an input from the user

Expected Output

[78.6, 78.6, 85.3, 1.2, 3.5]
"""

# First thing I will do is create an empty list, so it can be populated with numbers
# After that, I will make a range to 5 and loop through it and each loop will prompt
# the user to enter a number
# When the user inputs their numbers, those numbers will be appended to the empty list made in the beginning


# Declaring an empty list
numbers = []

# creating the range of 5
for i in range(1, 6):
    # prompting the user to enter a number and casting float over it so that it will be a float and not a string
    # using the current index, i, to let the user know what number of inputs they are currently at
    user_input = float(input(f"Five numbers are needed. You are at number {i}, please type in a number "))
    # saving the user's inputs into the list created above using the append method, also using the function round()
    # to only set it a the first decimal place
    numbers.append(round(user_input, 1))

# printing out the list of numbers inputted by the user
print(f'\n{numbers}')
