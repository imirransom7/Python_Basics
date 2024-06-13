"""
Exercise 8: Print the following pattern:

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""

# I will make a function that will take in a list of numbers
# I will also need a control flow to be able to get the numbers to print out like the example above
# When iterating through the list, I will add however many of the element to itself as a string to get
# it to print out the same number shown

def triangle1(nums: List[int]):
  # creating a for loop to iterate the numbers
  for num in nums:
    # casting str() over the elements/numbers so that I can multiply the number against itself
    # to have them print a triangle or step
    print(str(num) * num)


traingle1([1, 2, 3, 4, 5])
