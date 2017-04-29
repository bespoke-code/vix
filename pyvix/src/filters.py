import json
import math
import re
def temporalFilter(dataList, startTime, endTime):
    filteredData = []
    matchesFound = 0
    for dataElement in dataList:
        # TODO: Code this part, pls
        continue
    return filteredData


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
    matchesFound=0
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
