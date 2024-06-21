"""
EXERCISE 3: Print character from a string that are present at a even index number

Write a program to accept a string from the user and display characters that are present at an even
index number

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""

# I will create a function that will take in any string
# Then, I will loop through the length of the string and only print letters at an even index


# Creating a function that will take in string
def even_only_indexes1(word: str):
    print(f"Original string is {word}")
    print("Printing only even index characters")

    # Creating a range that will start from 0 and end at the length of the string, but only incrementing
    # by two so that we only get even index outputs; no need for a conditional
    for i in range(0, len(word), 2):
        print(word[i])


even_only_indexes1('pynative')


# creating function for new solution
def even_only_indexes2(word: str):
    print(f'Original String: {word}')

    # slicing with starting at the first index and stepping by 2, and stopping at the end, that's why the middle,
    # or the stop, is empty
    for i in word[0::2]:
        print(i)


even_only_indexes2('pynative')


