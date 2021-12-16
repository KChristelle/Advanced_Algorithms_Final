# Algorithms summative Question 4

def Summation(nbr, k):
    # call function that will add up the digits of the integer
    def sumDigits(value):
        # check if value is a one-digit number if yes return number
        if value < 10:
            return value
        # sum up the digits of the passed number
        sumD = sum(int(i) for i in str(value))
        # Recall next function with sum to make sure it is a one-digit number
        return sumDigits(sumD)
    # once the number is reduced to one-digit number set super number
    super_number = sumDigits(int(nbr))
    # multiply super number by k to get final answer
    return sumDigits(super_number*k)

