import os

def SearchName(SearchDir, SearchPattern) -> list:
    '''
    Implements functionality of the application which searches for a list of files and directories containing a string in the name
    :param SearchDir: Takes in the directory to search
    :param SearchPattern: Takes in the pattern to search for
    :return: A list of directories and files whose names match the search term
    '''

    pass

    try:
        itemlist = os.listdir(SearchDir)
    except PermissionError:
        return []

    returnList = []

    for item in itemlist:
        # If the item is a directory
        if (os.path.isdir(SearchDir + "/" + item)):
            if (SearchString(item, SearchPattern) == True):
                returnList.append(f'{SearchDir}/{item}')
                for subitem in SearchName(SearchDir + '/' + item, SearchPattern):
                    returnList.append(subitem)
            else:
                for subitem in SearchName(SearchDir + '/' + item, SearchPattern):
                    returnList.append(subitem)
        # If the item is a file
        else:
            if (SearchString(item, SearchPattern) == True):
                returnList.append(f'{SearchDir}/{item}')
            else:
                continue

    return returnList


def SearchString(SearchString, PatternString) -> bool:
    '''
    Takes in a string to search for a pattern, and returns whether the string contains the pattern
    :param SearchString: Takes in a string to search for a pattern
    :param SearchPattern: Takes in a pattern to compare
    :return: Boolean value stating whether the string contains the pattern
    '''

    SearchStringLen = len(SearchString)
    PatternStringLen = len(PatternString)

    if (PatternStringLen > SearchStringLen):
        return False
    elif (PatternStringLen == SearchStringLen):
        if (PatternString == SearchString):
            return True
        else:
            return False
    else:
        offset = 0
        Index = 0
        Equal = True
        while (PatternStringLen + offset <= SearchStringLen):
            Equal = True
            for char in PatternString:
                if (PatternString[Index] == SearchString[Index + offset]):
                    Index = Index + 1
                    continue
                else:
                    Equal = False
                    break
            if (Equal == True):
                return True
            else:
                Index = 0
                offset = offset + 1
                continue
        return False