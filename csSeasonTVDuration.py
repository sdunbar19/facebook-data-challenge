from chiSquareMain import *
from dataHolders.season import *
from dataHolders.TVDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = seasonList
    secondParam = TVDurationList
    chiSquareTest('netflix_tv', firstParam, secondParam, makeQueryEndersSeason, makeQueryEndersTVDuration, "seasonTVDuration.txt")