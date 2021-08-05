from chiSquareMain import *

countryList = ['United States', 'India', 'United Kingdom', 'Japan', 'South Korea', 'Canada', 'Spain', 'France', 
'Egypt', 'Mexico', 'Turkey', 'Australia', 'Taiwan', 'Brazil']

# Makes the enders for countries
def makeQueryEndersCountry():
    params = countryList
    constTuple = ("country = '", "'")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)