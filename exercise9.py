"""
Exercise 9: Check Palindrome Number

Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is
the palindrome numbers
"""

# Writing a function that will take in a number and print out if the number is a palindrome
# I will check the number to see if it is a palindrome by casting str() over the number and using slicing
# I will use slicing to reverse the number and check to see if it is the same compared with the number without reverese

def palindrome_number(nums: int):
  # casting str() over the nums parameter to conver to string so that I can reverse it using slicing, which only works with sequences
  if str(nums) == str(nums)[::-1]:
    print("Yes. Given number is palindrome number)
  else:
    print("No. Given number is not palindrome")


palindrome_number(121)

