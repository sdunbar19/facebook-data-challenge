from chiSquareMain import *
from dataHolders.country import *
from dataHolders.yearReleased import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = countryList
    secondParam = yearReleasedList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersCountry, makeQueryEndersYearReleased, "countryYearReleased.txt")