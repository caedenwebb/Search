# Python Libraries
import os

# Internal Project Files
from utils import SearchString

# External Libraries

def SearchName(SearchDir, SearchPattern) -> list:
    '''
    Implements functionality of the application which searches for a list of files and directories containing a string in the name
    :param SearchDir: Takes in the directory to search
    :param SearchPattern: Takes in the pattern to search for
    :return: A list of directories and files whose names match the search term
    '''

    # Attempt to list the directory
    try:
        itemlist = os.listdir(SearchDir)
    # If obtaining a list of files and directories in a directory fails because of a lack of permission, return empty list
    except PermissionError:
        return []

    returnList = [] # List to contain files and directories meeting the search pattern

    # Recursively search through files and directories to check if their filenames meet the search pattern
    for item in itemlist:
        # If the item is a directory
        if (os.path.isdir(SearchDir + "/" + item)):
            # If the directory meets the search pattern, add to the returnList, and recurse through the files and directories inside said dir
            if (SearchString(item, SearchPattern) == True):
                returnList.append(f'{SearchDir}/{item}')
                for subitem in SearchName(SearchDir + '/' + item, SearchPattern):
                    returnList.append(subitem)
            # If the directory does not meet the search pattern, recurse through the files and directories inside directory
            else:
                for subitem in SearchName(SearchDir + '/' + item, SearchPattern):
                    returnList.append(subitem)
        # If the item is a file
        else:
            # If the file meets the search pattern
            if (SearchString(item, SearchPattern) == True):
                returnList.append(f'{SearchDir}/{item}')
            # If the file does not meet the search pattern
            else:
                continue

    # Return the list of files and dirs meeting search pattern
    return returnList