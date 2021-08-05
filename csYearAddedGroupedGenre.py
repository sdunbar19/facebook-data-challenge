from chiSquareMain import *
from dataHolders.yearAddedGrouped import *
from dataHolders.genre import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedGroupedList
    secondParam = genreList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAddedGrouped, makeQueryEndersGenre, "yearAddedGroupedGenre.txt")