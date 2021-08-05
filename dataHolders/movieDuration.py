from chiSquareMain import *

def appendToTuple(rangeStart, rangeEnd, final):
    tup = []
    for i in range(rangeStart, rangeEnd):
        tup.append(str(i) + " min")
    final.append(tuple(tup))

# make minRange, maxRange multiples of 10
def createMovieDurationList(minLength, maxLength):
    finalList = []
    appendToTuple(1, minLength, finalList)
    currCount = minLength
    while currCount < maxLength:
        appendToTuple(currCount, currCount + 50, finalList)
        currCount += 50
    return finalList

# Makes the enders for month
def makeQueryEndersMovieDuration():
    params = createMovieDurationList(50, 200)
    constTuple = ("duration = '", "'")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)