import os
from utils import SearchString

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