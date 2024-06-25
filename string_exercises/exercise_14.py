"""
Exercise 14: Remove empty strings from a list of strings

Given:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

Expected Output

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
"""

# I will start by creating a function that takes in a list and returns a list. I will remove the elements that
# are None values or are empty strings by using a conditional that checks the length of the string. if the length
# of the string is 0, then it will be removed


def no_empty_str(str_list: list) -> list[str]:
    # creating empty list
    new_list = []
    # iterating through the given list
    for string in str_list:
        # checking if the element's length is at least one
        if len(string) >= 1:
            # populating new list without empty strings
            new_list.append(string)
    # returning list without empty strings
    return new_list

