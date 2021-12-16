# Algorithms summative Question 2

# Addition of function


def SumOfDigits(nbr):
    if nbr == 0:
        return 0
    else:
        # counter = counter + 1
        return nbr % 10 + SumOfDigits(int(nbr / 10))
