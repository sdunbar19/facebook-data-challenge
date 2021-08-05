from chiSquareMain import *

ratingList = ['TV-MA', 'R', 'PG-13', 'TV-14', 'TV-PG', 'NR', 'TV-G', 'TV-Y']

# Makes the enders for month
def makeQueryEndersRating():
    params = ratingList
    constTuple = ("rating = '", "'")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)