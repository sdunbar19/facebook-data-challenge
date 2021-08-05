from chiSquareMain import *
from dataHolders.season import *
from dataHolders.country import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = seasonList
    secondParam = countryList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersSeason, makeQueryEndersCountry, "seasonCountry.txt")