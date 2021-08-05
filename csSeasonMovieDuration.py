from chiSquareMain import *
from dataHolders.season import *
from dataHolders.movieDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = seasonList
    secondParam = createMovieDurationList(50, 200)
    chiSquareTest('netflix_movie', firstParam, secondParam, makeQueryEndersSeason, makeQueryEndersMovieDuration, "seasonMovieDuration.txt")