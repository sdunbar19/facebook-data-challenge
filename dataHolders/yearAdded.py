from chiSquareMain import *

yearAddedList = [2015, 2016, 2017, 2018, 2019, 2020]

# Makes the enders for genre
def makeQueryEndersYearAdded():
    params = yearAddedList
    constTuple = ("YEAR(date_added) = ", "")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)