"""
Exercise 10: Write a program to count occurrences of all characters
within a string

Given:
str1: "Apple"

Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""

# starting with writing a function that takes in a string as a parameter that returns a dictionary
# Then I will iterate through the string and count the amount of times a letter occurs. I will place the
# letter as the key and their occurrences as the value


def occurrences(str1: str) -> dict:
    # creating an empty dictionary
    new_dict = {}
    # iterating through the given string
    for s in str1:
        # checking to see if the letter has already been put in the dictionary
        if s in new_dict:
            # if letter is in the dictionary, then increment the value by one
            new_dict[s] += 1
        # if the letter is not in the dictionary, then it will be added with a value starting at one
        else:
            new_dict[s] = 1
    return new_dict


# printing dictionary for the string provided
print(occurrences("Apple"))


# Here is another solution to the problem
def occurrence(str1: str) -> dict:
    # creating empty dictionary
    letter_dict = {}
    # iterating through given string
    for s in str1:
        # add or update the count of the character using the count method
        # this will add the letter as the key and the occurrences of the letter as the value
        letter_dict[s] = str1.count(s)
    return letter_dict


print(occurrence("Apple"))
