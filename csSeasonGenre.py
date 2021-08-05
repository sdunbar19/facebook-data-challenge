from chiSquareMain import *
from dataHolders.season import *
from dataHolders.genre import *
import mysql.connector
import sys

if __name__ == "__main__":
    fqEnders = makeQueryEndersSeason()
    sqEnders = makeQueryEndersGenre()
    chiSquareTest('netflix', seasonList, genreList, makeQueryEndersSeason, makeQueryEndersGenre, "seasonGenre.txt")