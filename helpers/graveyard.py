from databaseConnect import *
import mysql.connector
import sys

genreList = ["TV", "Movies", "Action & Adventure", "Dramas", "International", "Sci-Fi & Fantasy", "Horror", "Thriller", "Crime", 
            "Sports", ("Documentaries", "Docuseries"), "Independent", "Comedies", "Anime", "Reality TV", "Romantic", "Science & Nature", 
            "Mysteries", "Music & Musicals", ("Kids", "Children"), "LGBTQ", "Teen", "Cult", "Stand-Up Comedy"]

def extractResultVal(result):
    return result[0][0]

def getSQLInfoBase(cursor):
    totalsMonth = []
    totalsGenre = []
    countMonthGenreYes = []
    countMonthGenreNo = []
    for month in range(1, 13):
        query = "SELECT COUNT(show_id) FROM netflix WHERE MONTH(date_added) = %s" % str(month)
        total = extractResultVal(makeQuery(cursor, query))
        totalsMonth.append(total)
    for genre in genreList:
        query = "SELECT COUNT(show_id) FROM netflix WHERE "
        if type(genre) == str:
            query += "listed_in LIKE '%" + genre + "%' "
        else:
            tupList = []
            for tup in genre:
                tupList.append("listed_in LIKE '%" + tup + "%'")
            finVal = " OR ".join(tupList)
            finVal = "(" + finVal
            finVal = finVal + ") "
            query += finVal
        countsYes = []
        countsNo = []
        total = extractResultVal(makeQuery(cursor, query))
        totalsGenre.append(total)
        for month in range(1, 13):
            total = totalsMonth[month - 1]
            queryNew = query
            queryNew += "AND MONTH(date_added) = %s" % str(month)
            result = extractResultVal(makeQuery(cursor, queryNew))
            negResult = total - result
            countsYes.append(result)
            countsNo.append(negResult)
        countMonthGenreYes.append(countsYes)
        countMonthGenreNo.append(countsNo)
    return countMonthGenreYes, countMonthGenreNo, totalsMonth, totalsGenre

def makeQueryEnders(params, constTuple, joiner):
    queryEnders = []
    for param in params:
        complete = ""
        if type(param) != tuple:
            complete = constTuple[0] + str(param) + constTuple[1]
        else:
            tupList = []
            for tup in param:
                tupList.append(constTuple[0] + tup + constTuple[1])
            finVal = joiner.join(tupList)
            finVal = "(" + finVal
            finVal = finVal + ") "
            complete = finVal
        queryEnders.append(complete)
    return queryEnders

def makeQueryEndersGenre():
    params = genreList
    constTuple = ("listed_in LIKE '%", "%'")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)

def makeQueryEndersMonth():
    params = range(1, 13)
    constTuple = ("MONTH(date_added) = ", "")
    joiner = " OR "
    return makeQueryEnders(params, constTuple, joiner)

def checkListSame(list1, list2):
    if type(list1[0]) == list:
        for i in range(len(list1)):
            for j in range(len(list1[0])):
                if list1[i][j] != list2[i][j]:
                    print(list1)
                    print(list2)
                    print(i)
                    print(list1[i])
                    print(list2[i])
                    sys.exit()
    else:
        for i in range(len(list1)):
            assert(list1[i] == list2[i])

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

def testGetSQLInfo():
    conn, cursor = get_conn_cursor("netflix")
    monthQueryEnders = makeQueryEndersMonth()
    genreQueryEnders = makeQueryEndersGenre()
    query = "SELECT COUNT(show_id) FROM netflix WHERE "
    monthParam = range(1, 13)
    genreParam = genreList
    countMonthGenreYes, countMonthGenreNo, totalMonth, totalGenre = getSQLInfo(cursor, query, monthParam, genreParam, monthQueryEnders, genreQueryEnders)
    countMonthGenreYes2, countMonthGenreNo2, totalMonth2, totalGenre2 = getSQLInfoBase(cursor)
    checkListSame(countMonthGenreYes, countMonthGenreYes2)
    print("Yes is fine")
    checkListSame(countMonthGenreNo, countMonthGenreNo2)
    print("No is fine")
    checkListSame(totalMonth, totalMonth2)
    print("Total month fine")
    checkListSame(totalGenre, totalGenre2)
    print("Total genre fine")

def computeChiSquare(expected, actual):
    num = (expected - actual) * (expected - actual)
    return float(num)/float(expected)

def main():
    conn, cursor = get_conn_cursor("netflix")
    total = extractResultVal(makeQuery(cursor, "SELECT COUNT(show_id) FROM netflix"))
    query = "SELECT COUNT(show_id) FROM netflix WHERE "
    firstParam = range(1, 13)
    qeFP = makeQueryEndersMonth()
    qeSP = makeQueryEndersGenre()
    countMonthGenreYes, countMonthGenreNo, totalsMonth, totalsGenre = getSQLInfo(cursor, query, firstParam, genreList, qeFP, qeSP)
    percents = []
    for t in totalsGenre:
        percents.append(float(t) / float(total))

    for i in range(len(genreList)):
        chisquare = 0
        chisquareByMonthYes = []
        chisquareByMonthNo = []
        genre = genreList[i]
        valsYes = countMonthGenreYes[i]
        valsNo = countMonthGenreNo[i]
        percentTV = percents[i]
        expectedByMonthYes = []
        expectedByMonthNo = []
        for j in range(12):
            totalMonth = totalsMonth[j]
            expectedYesMonth = totalMonth * percentTV
            expectedByMonthYes.append(expectedYesMonth)
            expectedNoMonth = totalMonth * (1 - percentTV)
            expectedByMonthNo.append(expectedNoMonth)
            csYes = computeChiSquare(expectedYesMonth, valsYes[j])
            chisquareByMonthYes.append(csYes)
            chisquare += csYes
            csNo = computeChiSquare(expectedNoMonth, valsNo[j])
            chisquare += csNo
            chisquareByMonthNo.append(csNo)
        if chisquare > 19.675:
            print(genre)
            # print("Counts: " + str(valsYes))
            #print("Expected: " + str(expectedByMonthYes))
            #print("Significance: " + str(chisquareByMonthYes))
            #print("Counts not: " + str(valsNo))
            #print("Expected not: " + str(expectedByMonthNo))
            #print("Significance: " + str(chisquareByMonthNo))
            print("Total count: " + str(chisquare))
            print("         ")

if __name__ == "__main__":
    main()