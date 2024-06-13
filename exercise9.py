"""
Exercise 9: Check Palindrome Number

Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is
the palindrome numbers
"""

# Writing a function that will take in a number and print out if the number is a palindrome
# I will check the number to see if it is a palindrome by casting str() over the number and using slicing
# I will use slicing to reverse the number and check to see if it is the same compared with the number without reverese

def palindrome_number1(nums: int):
  # casting str() over the nums parameter to conver to string so that I can reverse it using slicing, which only works with sequences
  if str(nums) == str(nums)[::-1]:
    print("Yes. Given number is palindrome number)
  else:
    print("No. Given number is not palindrome")


palindrome_number1(121)


# Trying another solution without slicing
# going to create a fucntuion similar to the first one
# convert number into a list
# Then I will use control flow to compare each element in reverse
def palindrome_number2(number: int):
  # creating a counter to count if the elements are the same
  counter = 0
  nums = list(number)
  # creating a for loop to iterate through the list
  for i in range(len(nums)):
    # creating another for loop inside the first for loop to compare the list with itself in reverse
    for j in range(len(nums), 0, -1):
      # counter will increment 
      count+=1

  # if the counter is the same as the length of the list, if it is, then that means the same amount of elements were equal to each other
   which shold be the same as the list
  if counter == len(nums):
    print("Yes. Given number is palindrome number)
  else:
    print("No. Given number is not palindrome")
    
    
      







