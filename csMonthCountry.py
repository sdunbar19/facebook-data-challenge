from chiSquareMain import *
from dataHolders.month import *
from dataHolders.country import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = monthList
    secondParam = countryList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersMonth, makeQueryEndersCountry, "monthCountry.txt")