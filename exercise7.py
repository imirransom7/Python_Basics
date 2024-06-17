"""
Exercise 7: Return the count of a given substring from a string

Write a program to find how many times substring “Emma” appears in the given string.
"""

# I will create a function that will take in a string and returns a number
# I will create a variable that will hold counter to count the amount of times 'Emma' shows up
# To find how many times 'Emma' is in a substring, I will convert the string into a list
#  with a delimiter of spaces, to then iterate though it and see which elements, substrings, have
# Emma as a substring. Next, is to increment the counter everytime Emma is a substring and then return
# that counter


# creating a function that takes in a string and returns a number
def substring(sentence: str) -> int:
    # creating counter to keep track of substrings with 'Emma'
    counter = 0

    # converting string into a list with spaces as the delimiter
    new_list = sentence.split(" ")
    # I am now creating a for loop that will iterate through my newly created list
    for new in new_list:
        # making a conditional, comparing the current element with the string/word 'Emma'
        if new == 'Emma':
            # incrementing the counter once this condition is met
            counter += 1

    # returning the counter since it will have the amount of 'Emma' substrings
    return counter


# calling in my function
print(substring("Emma is a good developer. Emma is a writer"))

# There is another solution that is a lot more concise by using the '.count' method


# creating my function that will take in a string and return a number
def sub(sentence: str) -> int:
    return sentence.count('Emma')

  
print(sub('Emma is a good developer. Emma is a writer'))
