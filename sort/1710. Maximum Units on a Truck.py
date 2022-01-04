def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x:x[1], reverse=True) #sort by the 2nd element DESC
    res = 0
    
    for box, units in boxTypes:
        if truckSize > box:
            truckSize -= box
            res += box * units
        else:
            res += truckSize * units
            return res
    return res
