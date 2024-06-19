"""
Exercise 13: Print multiplication table from 1 to 10

Expected Output:

1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 
"""

# Going to create a function for that takes in one number as parameters and will print
# out the table above. I will then make a for loop with another for loop nested within
# It will loop through a range of a given number


def multi_table(num: int):
    # creating the first for loop
    for i in range(1, num+1):
        print("")
        for j in range(1, num+1):
            print(i*j, end="\t")
    

multi_table(10)
