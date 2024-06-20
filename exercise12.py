"""
Exercise 12: Calculate income tax for the given income by adhering to the riles below

For example, suppose the taxable income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.
"""

# I am going to create a fuction that will take in one number as the parameter and return on number
# Then, I will implement the equation used above. I will do (nums - 20,000)*20% since I need the remainder
# of the money after the first and second 10,000 used in the equation. Then, I will return the answer


def taxable(income: float) -> float:
    # implementing the equation given and subtracting the number given by 20,000 to get the remainder
    # making a conditional for if the taxable income is less than or equal to 10,000
    if income <= 10000:



    return (10000 * .00) + (10000 * .10) + ((income - 20000) * .20)


print(taxable(45000))
