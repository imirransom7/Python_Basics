"""
Exercise 6: Write all content of a given file into a new file by
skipping line number 5

Create a test,txt file and add the below content to it

Given test.txt file:                                 Expected Output: new_file.txt

line 1                                                line 1
line 2                                                line 2
line 3                                                line 3
line 4                                                line 4
line 5                                                line 6
line 6                                                line 7
line 7
"""

# I will start by creating a new file called test.txt using the open() function
# then I will write 7 new lines by using a for loop with a range of 7
# when writing in a new line so that it will be 'line 1', I will use the current index of the loop
# to put in the number where the line is at

# creating the test.txt file
with open('test.txt', 'w') as file:
    # creating the for loop to create the lines for the new file
    for i in range(1, 8):
        # every loop, a new line will be written in with the number being the current place of the index
        file.write(f'line {i}')

with open('test.txt', 'r') as file:
    file.read()
