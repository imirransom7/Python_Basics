"""

Exercise 1B: Create a string made of the middle three characters

Write a program to create a new string made of the middle three characters of an input string

Given:

Case 1                                                          Case 2:

str1 = "JohnDipPeta"                                            str2 = "JaSonAy"

Output:                                                         Output:

Dip                                                             Son
"""

# I will start by making a function with one parameter being a string and returning a string
# Then, inside the function, I will get the middle letter by using length and dividing it by two.
# After that is done, I can the next two middle letters by subtracting one to the middle index, and then adding 1
# to the middle index


def middle_three(string: str) -> str:
    # Getting the middle character by diving the length by two, then adding one more, and
    # then subtracting one more to get the third middle character
    # declaring the middle index since I will be using more than once; subtracting by one to get middle letter
    middle = int(len(string) // 2)
    # subtracting the first one from the middle to add it to the middle number and then the one right after the middle
    return string[middle-1] + string[middle] + string[middle+1]


# testing out that my function is working
print(middle_three("JhonDipPeta"))
print(middle_three("JaSonAy"))
