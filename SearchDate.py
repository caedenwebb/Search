# Python Libraries
import os
import time

# Internal Project Files
import FileClass

# External Libraries

def SearchDateCreated(path, pattern, recursiveFlag=False) -> list:
    rawCreationTime = time.localtime(os.path.getctime(path))
    creationDate = [rawCreationTime.tm_mon, rawCreationTime.tm_mday, rawCreationTime.tm_year]
    returnList = []

    # If file is a directory
    if (os.path.isdir(path)):
        dirlist = os.listdir(path)
        # Test if directory meets criteria
        if (TestDateForMatch(creationDate, pattern)):
            returnList.append(FileClass.Directory(path))
        # Search files in directory
        for item in dirlist:
            # If item is a directory and recursive flag is true
            if (os.path.isdir(f'{path}/{item}') == True and recursiveFlag == True):
                returnList = returnList + SearchDateCreated(f'{path}/{item}', pattern, recursiveFlag)
            # If the item is a directory and recursiveFlag is false
            elif (os.path.isdir(f'{path}/{item}') == True):
                subdirRawCreationTime = time.localtime(os.path.getctime(f'{path}/{item}'))
                subdirCreationDate = [subdirRawCreationTime.tm_mon, subdirRawCreationTime.tm_mday, subdirRawCreationTime.tm_year]
                if (TestDateForMatch(subdirCreationDate, pattern)):
                    returnList.append(FileClass.Directory(f'{path}/{item}'))
            # If the item is a file within the directory
            else:
                returnList = returnList + SearchDateCreated(f'{path}/{item}', pattern, recursiveFlag)
    # If file is a file
    else:
        if (TestDateForMatch(creationDate, pattern) == True):
            returnList.append(FileClass.File(path))
            return returnList
        else:
            return returnList

    return returnList # Necessary return statement

def SearchDateModified(path, pattern, recursiveFlag=False) -> list:
    rawModifiedTime = time.localtime(os.path.getmtime(path))
    modifiedTime = [rawModifiedTime.tm_mon, rawModifiedTime.tm_mday, rawModifiedTime.tm_year]
    returnList = []

    # If file is a directory
    if (os.path.isdir(path)):
        dirlist = os.listdir(path)
        # Test if directory meets criteria
        if (TestDateForMatch(modifiedTime, pattern)):
            returnList.append(FileClass.Directory(path))
        # Search files in directory
        for item in dirlist:
            # If item is a directory and recursive flag is true
            if (os.path.isdir(f'{path}/{item}') == True and recursiveFlag == True):
                returnList = returnList + SearchDateModified(f'{path}/{item}', pattern, recursiveFlag)
            # If the item is a directory and recursiveFlag is false
            elif (os.path.isdir(f'{path}/{item}') == True):
                subdirRawModifiedTime = time.localtime(os.path.getmtime(f'{path}/{item}'))
                subdirModifiedTime = [subdirRawModifiedTime.tm_mon, subdirRawModifiedTime.tm_mday, subdirRawModifiedTime.tm_year]
                if (TestDateForMatch(subdirModifiedTime, pattern)):
                    returnList.append(FileClass.Directory(f'{path}/{item}'))
            # If the item is a file within the directory
            else:
                returnList = returnList + SearchDateModified(f'{path}/{item}', pattern, recursiveFlag)
    # If file is a file
    else:
        if (TestDateForMatch(modifiedTime, pattern) == True):
            returnList.append(FileClass.File(path))
            return returnList
        else:
            return returnList

    return returnList # Necessary return statement



def TestDateForMatch(date, pattern) -> bool:
    '''
    This function tests to see if a date falls within a particular range of dates
    :param date: A list of integers representing a date in the following format [mm/dd/yy]
    :param pattern: A list of strings of the form "m1m1/d1d1/y1y1-m2m2/d2d2/y2y2"
    :return: True if date matches pattern, False if date does not match pattern
    '''
    afterFirstDate = False
    beforeSecondDate = False
    for dateSet in pattern:
        sDateSet = dateSet.split('-')
        # If there is only one date in a particular set of dates
        if (len(sDateSet) == 1 or sDateSet[1] == ''):
            compDate = sDateSet[0].split('/')
            for index in range(len(compDate)):
                compDate[index] = int(compDate[index])
            if (date == compDate):
                return True
            else:
                continue
        # If there is an actual range to compare
        else:

            firstDate = sDateSet[0].split('/')
            lastDate = sDateSet[1].split('/')

            # Change first and last dates into lists of integers
            for index in range(len(firstDate)):
                firstDate[index] = int(firstDate[index])

            for index in range(len(lastDate)):
                lastDate[index] = int(lastDate[index])

            # Compare if creation date is between the firstDate and lastDate

            if (date[2] >= firstDate[2]) and (date[2] <= lastDate[2]):
                if (date[2] == firstDate[2]):
                    if (date[0] >= firstDate[0]):
                        if (date[1] >= firstDate[1]):
                            afterFirstDate = True
                        else:
                            afterFirstDate = False
                    else:
                        afterFirstDate = False
                elif (date[2] > firstDate[2]):
                    afterFirstDate = True

                if (date[2] == lastDate[2]):
                    if (date[0] <= lastDate[0]):
                        if (date[0] == lastDate[0]):
                            if (date[1] <= lastDate[1]):
                                beforeSecondDate = True
                            else:
                                beforeSecondDate = False
                        else:
                            beforeSecondDate = True
                    else:
                        beforeSecondDate = False
                elif (date[2] < lastDate[2]):
                    beforeSecondDate = True
                else:
                    beforeSecondDate = False

        if (afterFirstDate == True and beforeSecondDate == True):
            return True
        else:
            continue

    if (afterFirstDate == False or beforeSecondDate == False):
        return False
    else:
        return True