from chiSquareMain import *
from dataHolders.month import *
from dataHolders.TVDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = monthList
    secondParam = TVDurationList
    chiSquareTest('netflix_tv', firstParam, secondParam, makeQueryEndersMonth, makeQueryEndersTVDuration, "monthTVDuration.txt")