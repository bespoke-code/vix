import json

def temporalFilter(dataList, startTime, endTime):
    filteredData = []
    matchesFound = 0
    for dataElement in dataList:
        # TODO: Code this part, pls
        continue
    return filteredData

def spatialFilter(dataList, inputCoordinates):
    filteredData = []
    matchesFound = 0
    for dataElement in dataList:
        # TODO: Code this part, pls
        continue
    return filteredData

def keyWordFilter(dataList, inputKeywords):
    filteredData = []
    matchesFound=0
    for dataElement in dataList:
        for keyword in inputKeywords:
            if keyword in dataElement["keyword"]:
                matchesFound+=1
        if matchesFound > 0:
            filteredData.append(dataElement)
        matchesFound=0
    return filteredData

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
