from chiSquareMain import *
from dataHolders.season import *
from dataHolders.rating import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = seasonList
    secondParam = ratingList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersSeason, makeQueryEndersRating, "seasonRating.txt")