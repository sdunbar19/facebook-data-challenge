from chiSquareMain import *
from dataHolders.month import *
from dataHolders.rating import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = monthList
    secondParam = ratingList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersMonth, makeQueryEndersRating, "monthRating.txt")