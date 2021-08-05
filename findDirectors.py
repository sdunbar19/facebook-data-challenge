import csv
from helpers.databaseConnect import get_conn_cursor, makeQuery

filePathCSV = "csvDocs/"

def printToFile(fileName, string):
    with open(fileName, "a") as file:
        file.write(string + "\n")

def createCSVFName(fileName):
    return fileName + ".csv"

def createFName(myFilePath, fileNameRaw):
    return myFilePath + fileNameRaw

def createCSVFile(fileName, results):
    CSVFName = createFName(filePathCSV, createCSVFName(fileName))
    with open(CSVFName, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        params = ["Name", "Count"]
        csvwriter.writerow(params)
        for result in results:
            csvwriter.writerow(result) 

def findCountsLike(result, topNum):
    items = {}
    for posItem in result:
        dirList = str(posItem[0]).split(', ')
        for item in dirList:
            if item not in items:
                items[item] = 0
            items[item] += 1
    arr = []
    for key, value in items.items():
        arr.append([key, value])
    arr.sort(key=lambda x: -1 * x[1])
    return arr[0: topNum]

def makeStandardQuery(column, rowLimit=10):
    query = "SELECT " + column + " FROM netflix"
    result = makeQuery(cursor, query)
    sortedFinal = findCountsLike(result, rowLimit)
    createCSVFile(column, sortedFinal)

conn, cursor = get_conn_cursor('netflix')
makeStandardQuery("director", 11)
makeStandardQuery("show_cast", 11)
makeStandardQuery("listed_in")
makeStandardQuery("country")
makeStandardQuery("year(date_added)")
makeStandardQuery("release_year")
makeStandardQuery("rating")