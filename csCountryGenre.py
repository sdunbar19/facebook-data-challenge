from chiSquareMain import *
from dataHolders.country import *
from dataHolders.genre import *
import mysql.connector
import sys

if __name__ == "__main__":
    firstParam = countryList
    secondParam = genreList
    chiSquareTest('netflix', firstParam, secondParam, makeQueryEndersCountry, makeQueryEndersGenre, "countryGenre.txt")