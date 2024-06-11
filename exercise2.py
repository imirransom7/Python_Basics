'''
EXERCISE 2: Print the sum of the current number and the previous number

Write a program to iterarte the first 10 numbers, and in each iteration, print the sum of the current
and previous number
'''

# I will start making a function for this program to take in one integer
# Then, I will start by creating a range of 10
# making the previous number and current number start at 0
# then add them together within the range so it happens 10 times

def precious_number(num: int, amount):
    # created a conditional so there are no negatives if the current number starts at 0
    prev = 0 if num == 0 else num - 1
    # making a range of to with the printning format to not repeat code
    for i in range(amount):
        # printing in the required format and adding the currrent and previous numbers at the end
        print(f'Current Number {num} Previous Number {prev} Sum: {num + prev}')
        # created a conditional that only the current number will increase if it is at 0, so there are no negatives
        # and so that the previous number of 1 will be 0. and if current is 0 then so will previous number
        if num == 0:
            num+=1
        # now it will increment both previous and current number after current number is not 0
        else:
            num+=1
            prev+=1

precious_number(0, 10)


previous_num = 0

# another solutionl; less code; but only works with a certain range. The code I wrote will work
# for whatever number or range
print('\n')
# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i
