from chiSquareMain import *
from dataHolders.country import *
from dataHolders.rating import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = countryList
    secondParam = ratingList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersCountry, makeQueryEndersRating, "countryRating.txt")