from chiSquareMain import *
from dataHolders.yearAdded import *
from dataHolders.genre import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedList
    secondParam = genreList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAdded, makeQueryEndersGenre, "yearAddedGenre.txt")