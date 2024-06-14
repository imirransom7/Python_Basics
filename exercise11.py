"""
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
digits.
"""

# I will make a function that will take in an integer and return a string
# I will convert the given integer into a list to reverse the order
# Then I will convert it into a string using the join method with a delimeter of spaces
# And since this will leave a space at the end and the beginning, I will use the strip method to remove those

def reveres_int(number: int) -> str:
  # I will not convert the given number into list by casting list() over it, but I will also need
  # to cast str() over it so that it will let me put the numbers into a list
  nums = list(str(numbers))
  # Now, I will reverse the order of the numbers using slicing And since the elements have already been turned into a string,
  # I can use the join methoduse the join method to convert the list back into a string with spaces as a delimeter
  # Using the strip method to get rid of the spaces at the beginning and end of the string
  return " ".join(nums[::-1])


print(reverse_int(7536))
