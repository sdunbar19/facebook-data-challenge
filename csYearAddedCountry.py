from chiSquareMain import *
from dataHolders.yearAdded import *
from dataHolders.country import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedList
    secondParam = countryList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAdded, makeQueryEndersCountry, "yearAddedCountry.txt")