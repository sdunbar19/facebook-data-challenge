from helpers.databaseConnect import get_conn_cursor, makeQuery
from helpers.calcDegFreedom import findDegreesFreedom
from helpers.resultProcessing import *
import mysql.connector
import sys

# Makes the enders we tack onto the queries
def makeQueryEnders(params, constTuple, joiner):
    queryEnders = []
    for param in params:
        complete = ""
        if type(param) != tuple:
            complete = constTuple[0] + str(param) + constTuple[1]
        else:
            tupList = []
            for tup in param:
                tupList.append(constTuple[0] + str(tup) + constTuple[1])
            finVal = joiner.join(tupList)
            finVal = "(" + finVal
            finVal = finVal + ") "
            complete = finVal
        queryEnders.append(complete)
    return queryEnders

# Extract the results
def extractResultVal(result):
    return result[0][0]

# Get SQL info
def getSQLInfo(cursor, query, firstParam, secondParam, firstQueryEnders, secondQueryEnders):
    totalsFirst = []
    totalsSecond = []
    countFirstSecondYes = []
    countFirstSecondNo = []
    for i in range(len(firstParam)):
        queryFirstTotal = query + firstQueryEnders[i]
        total = extractResultVal(makeQuery(cursor, queryFirstTotal))
        totalsFirst.append(total)
    for i in range(len(secondParam)):
        querySecondTotal = query + secondQueryEnders[i]
        total = extractResultVal(makeQuery(cursor, querySecondTotal))
        totalsSecond.append(total)
        countsYes = []
        countsNo = []
        for j in range(len(firstParam)):
            queryFirstSecond = query + firstQueryEnders[j] + " AND " + secondQueryEnders[i]
            result = extractResultVal(makeQuery(cursor, queryFirstSecond))
            total = totalsFirst[j]
            negResult = total - result
            countsYes.append(result)
            countsNo.append(negResult)
        countFirstSecondYes.append(countsYes)
        countFirstSecondNo.append(countsNo)
    return countFirstSecondYes, countFirstSecondNo, totalsFirst, totalsSecond

# Compute a single chi square statistic
def computeChiSquare(expected, actual):
    num = (expected - actual) * (expected - actual)
    return float(num)/float(expected)

# Overall chi square values
def chiSquareTest(dbName, firstParam, secondParam, makeQueryEndersFirstParam, makeQueryEndersSecondParam, fileName):

    clearFile(fileName)
    createCSVFile(createFName(filePathCSV, createCSVFName(fileName)))

    dfVal = findDegreesFreedom(firstParam)
    conn, cursor = get_conn_cursor('netflix')
    query = "SELECT COUNT(show_id) FROM %s WHERE " % dbName
    total = extractResultVal(makeQuery(cursor, "SELECT COUNT(show_id) FROM %s" % dbName))

    firstQueryEnders = makeQueryEndersFirstParam()
    secondQueryEnders = makeQueryEndersSecondParam()
    countFirstSecondYes, countFirstSecondNo, totalsFirst, totalsSecond = getSQLInfo(cursor, query, 
        firstParam, secondParam, firstQueryEnders, secondQueryEnders)

    percentBySecond = []
    for ts in totalsSecond:
        percentBySecond.append(float(ts) / float(total))
    
    for i in range(len(secondParam)):
        chisquare = 0
        chiSquareByFirstYes = []
        chiSquareByFirstNo = []
        currSP = secondParam[i]
        valsYes = countFirstSecondYes[i]
        valsNo = countFirstSecondNo[i]
        percentExp = percentBySecond[i]
        expFirstYes = []
        expFirstNo = []
        for j in range(len(firstParam)):
            totalFirst = totalsFirst[j]
            expectedYesFirst = totalFirst * percentExp
            expFirstYes.append(expectedYesFirst)
            expectedNoFirst = totalFirst * (1 - percentExp)
            expFirstNo.append(expectedNoFirst)
            csYes = computeChiSquare(expectedYesFirst, valsYes[j])
            chiSquareByFirstYes.append(csYes)
            chisquare += csYes
            csNo = computeChiSquare(expectedNoFirst, valsNo[j])
            chiSquareByFirstNo.append(csNo)
            chisquare += csNo
        if chisquare > dfVal:
            prettyPrinting(fileName, chisquare, currSP, firstParam, valsYes, expFirstYes, chiSquareByFirstYes, valsNo, expFirstNo, chiSquareByFirstNo, dfVal)
        printAllVals(fileName, chisquare, currSP, firstParam, valsYes, expFirstYes, chiSquareByFirstYes, valsNo, expFirstNo, chiSquareByFirstNo, dfVal)
    print("Done")