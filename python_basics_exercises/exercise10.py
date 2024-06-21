"""
Exercise 10: Create a new list from two list using the following condition

Create a new list from two list using the following condition

Given two list of numbers, write a program to create a new list such that the new list
should contain odd numbers from the first list and even numbers from the second list.
"""

# I will create a function that will take in two list as parameters, and return a list
# Then, I will iterate through both lists and only retrieve even numbers from one, and odd from the
# other, Then I will append all of that to a new list and return that list


def even_and_odd1(list1: list[int], list2: list[int]) -> list[int]:
    # I am creating two comprehension lists. The first one will get the odd numbers from the first list and
    # the second one will get the even numbers from the list. I am then adding them together within the sorted function
    # so that they will combine to make one list that has the numbers sorted inside
    return sorted([x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0])


print(even_and_odd1([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))
