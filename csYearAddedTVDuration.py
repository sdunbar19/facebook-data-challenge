from chiSquareMain import *
from dataHolders.yearAdded import *
from dataHolders.TVDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = yearAddedList
    secondParam = TVDurationList
    chiSquareTest('netflix_tv', firstParam, secondParam, makeQueryEndersYearAdded, makeQueryEndersTVDuration, "yearAddedTVDuration.txt")