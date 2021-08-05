from chiSquareMain import *

yearAddedGroupedList = [(2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017), (2018, 2019), (2020, 2021)]

# Makes the enders for genre
def makeQueryEndersYearAddedGrouped():
    params = yearAddedGroupedList
    constTuple = ("YEAR(date_added) = ", "")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)