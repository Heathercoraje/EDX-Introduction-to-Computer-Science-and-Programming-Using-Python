aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    if (not aDict): #if an empty dict is given, return False (non-empty dict is True)
        return {}
    else:
        result = [] # container
        values = list(aDict.values()) # extract values from aDict and remove replicates
        uniqueValues = [value for value in values if values.count(value) == 1]
        for uniqueValue in uniqueValues:
            for key in aDict.keys():
                if aDict[key] == uniqueValue:
                    result.append(key)
                    break # move on to next value to find key
        result.sort()
        return result
        
# 19.09 out of 20, I am not covering all cases
