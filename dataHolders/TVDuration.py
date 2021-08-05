from chiSquareMain import *

TVDurationList = ['1 Season', '2 Seasons', '3 Seasons', '4 Seasons', ('5 Seasons', '6 Seasons', '7 Seasons', '8 Seasons', '9 Seasons', '10 Seasons')]

# Makes the enders for month
def makeQueryEndersTVDuration():
    params = TVDurationList
    constTuple = ("duration = '", "'")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)