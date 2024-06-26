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
# of the string is 0 or there is a None value, then it will be removed

# the list with some empty strings
s_list = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']


def no_empty_str(str_list: list) -> list[str]:
    # creating empty list
    new_list = []
    # iterating through the given list
    for string in str_list:
        # checking for None values
        if string is None:
            continue
        # checking if the element's length is at least one
        elif len(string) >= 1:
            # populating new list without empty strings
            new_list.append(string)
    # returning list without empty strings
    return new_list


print("Original list of strings\n", s_list, "\n\nAfter removing empty strings\n", no_empty_str(s_list))

# Found other solutions

res_list = []
# checks if the element is True, meaning if the element is an empty string or None value it#
# will not be added to the new list
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)


# using built-in function filter to filter empty value, passing in None as an arguement will result in
# filter out any None values and empty strings
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)


