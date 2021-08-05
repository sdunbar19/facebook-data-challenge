from chiSquareMain import *
from dataHolders.yearAdded import *
from dataHolders.yearReleased import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedList
    secondParam = yearReleasedList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersYearAdded, makeQueryEndersYearReleased, "yearAddedYearReleased.txt")