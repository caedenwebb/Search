# Python Libraries
import os
import sys

# Internal Project Files


# Internal Libraries


def Alphabetize(filelist: list):
    '''
    Sorts the output of files based on alphabetizing the filenames
    :param filelist:list of file objects
    :return:
    '''

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

def OldestToNewest(filelist: list):

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
    sortedLesserValues = OldestToNewest(lesserValues)

    # Recursively sort values greater than pivot
    sortedGreaterValues = OldestToNewest(greaterValues)

    # Merge
    returnList = sortedLesserValues + equalValues + sortedGreaterValues

    return returnList
def NewestToOldest(filelist: list):
    '''
    Sorts files based on their dates of creation from newest to oldest
    :param filelist:
    :return:
    '''
    sortedFileList = OldestToNewest(filelist)
    finalFileList = []
    i = len(sortedFileList)-1
    while (i >= 0):
        finalFileList.append(sortedFileList[i])
        i = i - 1

    return finalFileList