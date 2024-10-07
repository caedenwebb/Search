# Python Libraries
import os
import sys

# Internal Project Files


# Internal Libraries

def SmallestToLargest(filelist: list):
    # Base Cases
    if (len(filelist) == 0):
        return filelist

    if (len(filelist) == 1):
        return filelist

    if (len(filelist) == 2):
        if (filelist[0].size > filelist[1].size):
            return [filelist[1], filelist[0]]
        else:
            return [filelist[0], filelist[1]]

    # Find pivot
    pivot = filelist[0]

    # Create lists of values less than pivot
    lesserValues = []
    equalValues = []
    greaterValues = []

    for value in filelist:
        if (value.size < pivot.size):
            lesserValues.append(value)
        elif (value.size == pivot.size):
            equalValues.append(value)
        else:
            greaterValues.append(value)

    # Create lists of values lesser than the pivot
    sortedLesserValues = SmallestToLargest(lesserValues)

    # Recursively sort values greater than pivot
    sortedGreaterValues = SmallestToLargest(greaterValues)

    # Merge
    returnList = sortedLesserValues + equalValues + sortedGreaterValues

    return returnList

def LargestToSmallest(filelist: list):
    '''Sorts the output of files based on their sizes from largest to smallest'''
    sortedFilelist = SmallestToLargest(filelist)

    # Generate reversed list
    i = len(filelist)-1
    finalList = []
    while (i >= 0):
        finalList.append(sortedFilelist[i])
        i = i - 1

    return finalList

def DCOldestToNewest(filelist: list):

    # Base Cases
    if (len(filelist) == 0):
        return filelist

    if (len(filelist) == 1):
        return filelist

    if (len(filelist) == 2):
        if (filelist[0].rawCreationTime > filelist[1].rawCreationTime):
            return [filelist[1], filelist[0]]
        else:
            return [filelist[0], filelist[1]]

    # Find pivot
    pivot = filelist[0]

    # Create lists of values less than pivot
    lesserValues = []
    equalValues = []
    greaterValues = []

    for value in filelist:
        if (value.rawCreationTime < pivot.rawCreationTime):
            lesserValues.append(value)
        elif (value.rawCreationTime == pivot.rawCreationTime):
            equalValues.append(value)
        else:
            greaterValues.append(value)

    # Create lists of values lesser than the pivot
    sortedLesserValues = DCOldestToNewest(lesserValues)

    # Recursively sort values greater than pivot
    sortedGreaterValues = DCOldestToNewest(greaterValues)

    # Merge
    returnList = sortedLesserValues + equalValues + sortedGreaterValues

    return returnList
def DCNewestToOldest(filelist: list):
    '''
    Sorts files based on their dates of creation from newest to oldest
    :param filelist:
    :return:
    '''
    sortedFileList = DCOldestToNewest(filelist)
    finalFileList = []
    i = len(sortedFileList)-1
    while (i >= 0):
        finalFileList.append(sortedFileList[i])
        i = i - 1

    return finalFileList

def DMOldestToNewest(filelist: list):

    # Base Cases
    if (len(filelist) == 0):
        return filelist

    if (len(filelist) == 1):
        return filelist

    if (len(filelist) == 2):
        if (filelist[0].rawModifiedTime > filelist[1].rawModifiedTime):
            return [filelist[1], filelist[0]]
        else:
            return [filelist[0], filelist[1]]

    # Find pivot
    pivot = filelist[0]

    # Create lists of values less than pivot
    lesserValues = []
    equalValues = []
    greaterValues = []

    for value in filelist:
        if (value.rawModifiedTime < pivot.rawModifiedTime):
            lesserValues.append(value)
        elif (value.rawModifiedTime == pivot.rawModifiedTime):
            equalValues.append(value)
        else:
            greaterValues.append(value)

    # Create lists of values lesser than the pivot
    sortedLesserValues = DMOldestToNewest(lesserValues)

    # Recursively sort values greater than pivot
    sortedGreaterValues = DMOldestToNewest(greaterValues)

    # Merge
    returnList = sortedLesserValues + equalValues + sortedGreaterValues

    return returnList
def DMNewestToOldest(filelist: list):
    '''
    Sorts files based on their dates of creation from newest to oldest
    :param filelist:
    :return:
    '''
    sortedFileList = DMOldestToNewest(filelist)
    finalFileList = []
    i = len(sortedFileList)-1
    while (i >= 0):
        finalFileList.append(sortedFileList[i])
        i = i - 1

    return finalFileList


def OrderAToZ(filelist):
    '''
    Quicksorts the output of files based on alphabetizing the filenames
    :param filelist:list of file objects
    :return:
    '''
    if (len(filelist) == 0):
        return filelist
    elif (len(filelist) == 1):
        return filelist
    elif (len(filelist) == 2):
        if (filelist[0].filename > filelist[1].filename):
            return [filelist[1], filelist[0]]
        else:
            return [filelist[0], filelist[1]]
    else:
        # Find pivot
        pivot = filelist[0]

        # Create lists of values less than pivot
        lesserValues = []
        equalValues = []
        greaterValues = []

        for value in filelist:
            if (value.filename < pivot.filename):
                lesserValues.append(value)
            elif (value.filename == pivot.filename):
                equalValues.append(value)
            else:
                greaterValues.append(value)

        # Create lists of values lesser than the pivot
        sortedLesserValues = OrderAToZ(lesserValues)

        # Recursively sort values greater than pivot
        sortedGreaterValues = OrderAToZ(greaterValues)

        # Merge
        returnList = sortedLesserValues + equalValues + sortedGreaterValues

        return returnList

def OrderZToA(filelist):
    sortedFileList = OrderAToZ(filelist)
    finalFileList = []
    i = len(sortedFileList)-1
    while (i >= 0):
        finalFileList.append(sortedFileList[i])
        i = i - 1

    return finalFileList