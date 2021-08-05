from chiSquareMain import *
from dataHolders.yearAdded import *
from dataHolders.movieDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedList
    secondParam = createMovieDurationList(50, 200)
    chiSquareTest('netflix_movie', firstParam, secondParam, makeQueryEndersYearAdded, makeQueryEndersMovieDuration, "yearAddedMovieDuration.txt")