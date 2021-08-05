from chiSquareMain import *
from dataHolders.country import *
from dataHolders.TVDuration import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = countryList
    secondParam = TVDurationList
    chiSquareTest('netflix_tv', firstParam, secondParam, makeQueryEndersCountry, makeQueryEndersTVDuration, "countryTVDuration.txt")