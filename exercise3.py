'''
EXERCISE 3: Print character from a string that are present at a even index number

Write a program to accept a string from the user and display characters that are present at an even
index number

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
'''

# I will create a function that will take in any string
# Then, I will loop through the length of the string and only print letters at an even index

# Creating a function that will take in string
def even_only_indexes(word: str) -> str:
    # Creating a range the will start from 0 and end at the length of the string
