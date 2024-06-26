"""
Exercise 7: Find all occurrences of a substring in a given string by
ignoring the case

Write a program to find all occurrences of "USA" in a given string ignoring the case

Given:
str1 = "Welcome to the USA. The usa awesome, isn't it?"

Expected Outcome
The USA count is: 2
"""
# Going to create a function that takes in a string as a parameter and returns an integer
# to find how many substrings there are of "USA" ignoring the case, I will turn the string into
# a list that is separated by the spaces in the string. I will also have a counter inplace to count
# the occurrence of the substring. All that's left is to return the counter


def occurrences(string: str) -> int:
    # declaring the counter
    counter = 0

    # converting to list using the list function
    st = list(string)
    # removing the punctuation
    st.remove(".")
    st. remove(",")
    # converting back to string
    sti = "".join(st)
    # converting the string into a list and iterating through it
    for s in sti.split(" "):
        # checking code
        # print(s.upper())
        # checking if element matched the substring while ignoring the case
        if s.upper() == 'USA':
            # incrementing the counter for the amount of occurrences
            counter += 1

    return counter


print("The USA count is:", occurrences("Welcome to the USA. The usa is awesome, isn't it?"))


# A more optimal way to solve this problem
# creating a function with a string as it's parameter that returns an integer
def occurrence(string: str) -> int:
    # making all characters to upper to ignore the case
    upper_str = string.upper()
    return upper_str.count("USA")


print("The USA count is:", occurrence("Welcome to the USA. The usa is awesome, isn't it?"))
