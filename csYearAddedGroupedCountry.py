from chiSquareMain import *
from dataHolders.yearAddedGrouped import *
from dataHolders.country import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedGroupedList
    secondParam = countryList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAddedGrouped, makeQueryEndersCountry, "yearAddedGroupedCountry.txt")