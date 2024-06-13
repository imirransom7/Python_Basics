"""
Exercise 10: Create a new list from two list using the following condition

Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list
should contain odd numbers from the first list and even numbers from the second list.
"""

# I will create a function that will take in two list as parameters, and return a list
# Then, I will iterate through both lists and only retrieve even numbers from one, and odd from the other
# Then, I will append all of that to a new list and return that list

def even_and_odd1(list1: List[int], list2: List[int]) -> List[int]:
  new_list = [list1[x], list2 for x in range(0, len(list1), 2) for y in range(1, len(list2)), 2]
    return new_list


even_and_odd([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])
