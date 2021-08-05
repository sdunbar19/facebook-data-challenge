from chiSquareMain import *
from dataHolders.month import *
from dataHolders.genre import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = monthList
    secondParam = genreList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersMonth, makeQueryEndersGenre, "monthGenre.txt")