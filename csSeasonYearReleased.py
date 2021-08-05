from chiSquareMain import *
from dataHolders.season import *
from dataHolders.yearReleased import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = seasonList
    secondParam = yearReleasedList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersSeason, makeQueryEndersYearReleased, "seasonYearReleased.txt")