import os

def SearchName(SearchDir, SearchPattern) -> list:
    '''
    Implements functionality of the application which searches for a list of files and directories containing a string in the name
    :param SearchDir: Takes in the directory to search
    :param SearchPattern: Takes in the pattern to search for
    :return: A list of directories and files whose names match the search term
    '''

    pass

    itemlist = os.listdir(SearchDir)

    for item in itemlist:
        # If the item is a directory
        if (os.path.isdir(SearchDir + "/" + item)):
            pass
        # If the item is a file
        else:
            pass

    return []


def SearchString(SearchString, Pattern) -> bool:
    '''
    Takes in a string to search for a pattern, and returns whether the string contains the pattern
    :param SearchString: Takes in a string to search for a pattern
    :param SearchPattern: Takes in a pattern to compare
    :return: Boolean value stating whether the string contains the pattern
    '''

    SearchStringLen = len(SearchString)
    PatternStringLen = len(Pattern)

    if (PatternStringLen > SearchStringLen):
        return False
    elif (PatternStringLen == SearchStringLen):
        if (Pattern == SearchString):
            return True
        else:
            return False
    else:
        IterationValue = PatternStringLen
        IndexVal = 0  #  start index value
        while (IterationValue <= SearchStringLen):
            while (IndexVal <= IndexVal + PatternStringLen):
                CmpRes = []
                if (SearchString[IndexVal] == PatternString[IndexVal])