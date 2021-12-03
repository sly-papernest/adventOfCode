def getIntFileasArray(fileName: str)-> list:
    """
    Read file as an array of integer
    """
    list_of_reading = []
    path = './' + fileName + '.txt'

    with open(path) as f:
        for line in f:
            list_of_reading.append(int(line))
        
    return list_of_reading


def getStringFileAsArray(fileName: str)-> list:
    """
    Read file as an array of string
    """
    list_of_reading = []
    path = './' + fileName + '.txt'
    print(path)

    with open(path) as f:
        for line in f:
            list_of_reading.append(str(line))

    return list_of_reading