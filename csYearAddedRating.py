from chiSquareMain import *
from dataHolders.yearAdded import *
from dataHolders.rating import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedList
    secondParam = ratingList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAdded, makeQueryEndersRating, "yearAddedRating.txt")