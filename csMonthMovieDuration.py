from chiSquareMain import *
from dataHolders.month import *
from dataHolders.movieDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = monthList
    secondParam = createMovieDurationList(40, 200)
    chiSquareTest('netflix_movie', firstParam, secondParam, makeQueryEndersMonth, makeQueryEndersMovieDuration, "monthMovieDuration.txt")