from chiSquareMain import *

seasonList = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

def makeQueryEndersSeason():
    params = seasonList
    constTuple = ("MONTH(date_added) = ", "")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)