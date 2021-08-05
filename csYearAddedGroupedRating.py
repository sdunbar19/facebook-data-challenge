from chiSquareMain import *
from dataHolders.yearAddedGrouped import *
from dataHolders.rating import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedGroupedList
    secondParam = ratingList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAddedGrouped, makeQueryEndersRating, "yearAddedGroupedRating.txt")