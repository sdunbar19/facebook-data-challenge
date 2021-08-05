import csv

filePath = "textDocs/"
filePathCSV = "csvDocs/"

def createFName(myFilePath, fileNameRaw):
    return myFilePath + fileNameRaw

def clearFile(fileNameRaw):
    fileName = createFName(filePath, fileNameRaw)
    with open(fileName, "w") as file:
        file.write("")

def printToFile(fileName, string):
    with open(fileName, "a") as file:
        file.write(string + "\n")

def createCSVFName(fileName):
    return fileName[0:len(fileName) - 4] + ".csv"

def createCSVFile(fileName):
    CSVFName = createCSVFName(fileName)
    with open(CSVFName, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile) 
        params = ["Trend", "Chi square val", "dfThreshold", "Parameter", "Expected count yes", "Actual count yes", "Expected count no", "Actual count no", "Significance value yes", "Significance value no"]
        csvwriter.writerow(params) 

def prettyPrinting(fileNameRaw, csVal, sParam, firstParam, countYes, expYes, sigYes, countNo, expNo, sigNo, dfThreshold):
    fileName = createFName(filePath, fileNameRaw)
    printToFile(fileName, "Trend detected: " + str(sParam))
    printToFile(fileName, "Chi square val: " + str(csVal))
    printToFile(fileName, "This is greater than dfThreshold: " + str(dfThreshold))
    amntExp = dfThreshold / len(firstParam)
    for i in range(len(firstParam)):
        param = firstParam[i]
        sY = sigYes[i]
        sN = sigNo[i]
        cY = countYes[i]
        cN = countNo[i]
        expY = expYes[i]
        expN = expNo[i]
        if sY > amntExp or sN > amntExp:
            printToFile(fileName, "Significant parameter: " + str(param))
            if cY > expY:
                printToFile(fileName, "Value was more than expected")
            elif cY < expY:
                printToFile(fileName, "Value was less than expected")
            printToFile(fileName, "Expected count: " + str(expY))
            printToFile(fileName, "Actual count: " + str(cY))
            printToFile(fileName, "Significance value yes: " + str(sY))
            printToFile(fileName, "Significance value no: " + str(sN))
            printToFile(fileName, " ")
    printToFile(fileName, " ")
    printToFile(fileName, " ")
    printToFile(fileName, " ")
    printToFile(fileName, " ")

def printAllVals(fileNameRaw, csVal, sParam, firstParam, countYes, expYes, sigYes, countNo, expNo, sigNo, dfThreshold):
    fileName = createFName(filePathCSV, createCSVFName(fileNameRaw))

    with open(fileName, 'a', newline='') as csvfile:

        csvwriter = csv.writer(csvfile) 
    
        for i in range(len(firstParam)):
            row = []
            row.append(sParam)
            row.append(csVal)
            row.append(dfThreshold)
            sY = sigYes[i]
            sN = sigNo[i]
            cY = countYes[i]
            cN = countNo[i]
            expY = expYes[i]
            expN = expNo[i]
            param = firstParam[i]
            row.append(param)
            row.append(expY)
            row.append(cY)
            row.append(expN)
            row.append(cN)
            row.append(sY)
            row.append(sN)
            csvwriter.writerow(row) 