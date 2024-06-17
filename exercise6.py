"""
Exercise 6: Display numbers divisible by 5 from a list

Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

# I will create a function that will take in a list of numbers as a parameter that prints out
# the numbers divisible by 5
# I will then create a control flow that will iterate through the given list
# Then, pass a condition that will make sure the only numbers printed from the list are divisible by 5


def div_by_5(lis: list[int]):
    # creating a for loop to iterate and print out the numbers in the list
    for l in lis:
        # making a conditional that will only print out the numbers divisible by 5 by using the modoulus operator
        if l % 5 == 0:
            print(l)


div_by_5([10, 20, 33, 46, 55])
