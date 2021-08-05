from chiSquareMain import *
from dataHolders.season import *
from dataHolders.yearAdded import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = seasonList
    secondParam = yearAddedList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersSeason, makeQueryEndersYearAdded, "seasonYearAdded.txt")