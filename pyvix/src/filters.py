import math
import re
import datetime


def temporalFilter(dataList, startTime=datetime.datetime(2017, 4, 27), endTime=datetime.timedelta(1), offset=0):
    if (endTime == datetime.timedelta(1)):
        endTime += startTime
    filteredData = []
    matchesFound = 0
    for dataElement in dataList:
        dataEL = re.split('R|T|[- :]|/P1Y|Z|/', dataElement['temporal'])

        if (dataEL[0] == ''):
            dataEL[0] = dataEL[1]
            dataEL[1] = dataEL[2]
            dataEL[2] = dataEL[3]

        if (endTime - datetime.datetime(int(dataEL[0]), int(dataEL[1]), int(dataEL[2]))) > datetime.timedelta(0):
            if (datetime.datetime(int(dataEL[0]), int(dataEL[1]), int(dataEL[2])) - startTime >= datetime.timedelta(0)):
                matchesFound += 1
        if matchesFound > 0:
            filteredData.append(dataElement)
    return filteredData[offset * 10:(1 + offset) * 10]


def spatialFilter(dataList, inputCoordinates, offset=0):
    filteredData = []
    matchesFound = 0
    for dataElement in dataList:
        # Coordinates are given in degrees
        dataElementCoords = re.split(', | ',dataElement['spatial'])
        if math.sqrt(
                (dataElementCoords[0] - inputCoordinates['lat'])**2 +
                (dataElementCoords[1] - inputCoordinates['lon'])**2
                ) <= 100:
                matchesFound+=1
        if matchesFound > 0:
            filteredData.append(dataElement)
    return filteredData[offset * 10:(1 + offset) * 10]


def keyWordFilter(dataList, inputKeywords, offset=0):
    filteredData = []
    matchesFound = 0
    for dataElement in dataList:
        for keyword in inputKeywords:
            if keyword in dataElement["keyword"]:
                matchesFound+=1
        if matchesFound > 0:
            filteredData.append(dataElement)
        matchesFound=0
    return filteredData[offset*10:(1+offset)*10]

def filter(jsonFile, isSpatial, isTemporal, isKeyword, searchQuery, offset=0):

    # JSON File transform
    dataset = []
    if isSpatial:
        dataset = spatialFilter(dataset, searchQuery['spatialCoordinates'])
    if isTemporal:
        dataset = temporalFilter(
            dataset,
            searchQuery.['startTime'],
            searchQuery['endTime']
        )
    if isKeyword:
        dataset = keyWordFilter(dataset, searchQuery['keywords'])

    return dataset[offset*10:(offset+1)*10]
