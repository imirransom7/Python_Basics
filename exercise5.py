"""
Exercise 5: Check if the first and last number of a list is the same

Write a function to return True if the first and last number of a given list is same. If numbers are
different then return False.
"""

# I will begin by writing in a function that takes in tone list and returns a boolean
# Then, I will compare the first and last index to see if they are equal
# To make it short and concise, I will just return the two substrings with the equals operator between them

def first_and_last1(lis, List[int]) -> boolean:
  return lis[0] == lis[-1]

print(first_and_last1([10, 20, 30, 40, 10]))
print(first_and_last1([75, 65, 35, 75, 30]))
