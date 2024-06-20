"""
Exercise 15: Write a function called exponent(base, exp) that returns
an int value of base raises to the power of exp

Note here exp is a non-negative integer, and the base is an integer
"""

# I will make a function that will take in two integers as parameters and return a number
# I will multiply the base with the exponent by using two asterisks (*) and return the result


def exponent(base: int, exp: int) -> int:
    return base**exp


print(exponent(2, 5))
print(exponent(5, 4))


# Here is another way to solve it
def expo(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)


expo(5, 4)

