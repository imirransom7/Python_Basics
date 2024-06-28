"""
Exercise 15: Remove special symbols / punctuation from a string

Given
str1 = "/*Jon is @developer & musician"

Expected Output
Jon is developer musician"
"""

# To start, I will create a function that will take in a string as a parameter and return a string
# Then, I will convert the string into a list using the split method splitting by the spaces found in 
# the string. Then I will use a condition while the list is being iterated through to check if elements
# are letters or symbols. Then I will use the join() method to convert the list back into a string


def no_symbols(str1: str):
    # using split method to convert string to list; creating empyt list
    new_list, non_str = str1.split(" "), []
    # iterating through newly created list
    for word in new_list:
        # iterating within the list
        for letter in word:
            # checking if element is not a letter
            if not letter.isalpha():
                # deleting element if it is not a letter
                del letter
    print("".join(new_list))


no_symbols("/*Jon is @developer & musician")
