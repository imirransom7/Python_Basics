"""
Exercise 4: Remove first 'n' characters from a string

Write a program to remove characters from a string starting from zero up to n and return a new
string

For Example:
remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.

remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.

Note: n must be less than the length of the string.
"""

# I will create a function that will take in a string
# I will use the slicing method to remove letters from the strings since
# there only needs to be a range of letters being dropped and not specific ones


# Creating a function with two parameters; the word, and the range being taken out of word
def remove_letters(word: str, n: int) -> str:
    return word[n:]


print(remove_letters('pynative', 4))
print(remove_letters('pynative', 2))
