"""
Exercise 5: Check if the first and last number of a list is the same

Write a function to return True if the first and last number of a given list is same. If numbers are
different then return False.
"""

# I will begin by writing in a function that takes in tone list and returns a boolean
# Then, I will compare the first and last index to see if they are equal
# To make it short and concise, I will just return the two substrings, first element and last element, of the list with the equals operator between them

def first_and_last1(lis, List[int]) -> bool:
  return lis[0] == lis[-1]


# Printing out solutions
print(first_and_last1([10, 20, 30, 40, 10]))
print(first_and_last1([75, 65, 35, 75, 30]))


# Another solution is using conditionals, though it requires more code, its still a good soultion

# I will again make another function that takes in one list and returns a boolean
# Then I will again compare the first and last elements in the list by making them substings of the list
# I will then use a conditional to see if the elements are equal; if so, return True, otherwise return False
def first_and_last2(lis: List[int]) -> bool:
  # saving the first and last element in variables since I will use them more than once
  first = list[0]
  last = lis[-1]

  # making the conditionals to check whether that elements meet True or False
  if first == last:
    return True
  else:
    return False


# printing out solutions
print(first_and_last2([10, 20, 30, 40, 10]))
print(first_and_last2([75, 65, 35, 75, 30]))


  
