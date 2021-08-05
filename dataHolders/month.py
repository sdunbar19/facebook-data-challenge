from chiSquareMain import *

monthList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Makes the enders for month
def makeQueryEndersMonth():
    params = range(1, 13)
    constTuple = ("MONTH(date_added) = ", "")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)