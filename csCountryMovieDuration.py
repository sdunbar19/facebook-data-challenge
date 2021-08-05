from chiSquareMain import *
from dataHolders.country import *
from dataHolders.movieDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = countryList
    secondParam = createMovieDurationList(50, 200)
    chiSquareTest('netflix_movie', firstParam, secondParam, makeQueryEndersCountry, makeQueryEndersMovieDuration, "countryMovieDuration.txt")