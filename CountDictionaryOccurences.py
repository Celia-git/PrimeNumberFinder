# Return a list of keys which map to values that appear once
# param: Dictionary
def uniqueValues(aDict):
    keys = []

    # Track number of occurrences of these values
    occurDict = {}
    for key, value in aDict.items():
        if value in occurDict.keys():
            occurDict[value] += 1
        else:
            occurDict[value] = 1

    # Return the keys, from aDict, which are mapped to values which occur once
    for value, occur_value in occurDict.items():
        if occur_value==1:
            for aDict_key, aDict_value in aDict.items():
                if value==aDict_value:
                    keys.append(aDict_key)                    
    
    return keys

def demo():
    print('Sample Dictionary: \n{"apples":"red","bananas":"yellow","oranges":"orange","apples":"green","pomegranates":"red","apples":"yellow","bananas":"green"}\n')
    print("All Unique entries in the Dict:")
    print(uniqueValues({"apples":"red","bananas":"yellow","oranges":"orange","apples":"green","pomegranates":"red","apples":"yellow","bananas":"green"}))

