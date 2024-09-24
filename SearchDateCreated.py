# Python Libraries
import os
import time

# Internal Project Files
import FileClass

# External Libraries

def SearchDateCreated(path, pattern, recursiveFlag) -> list:
    rawCreationTime = time.localtime(os.path.getctime(path))
    creationDate = [rawCreationTime.tm_mon, rawCreationTime.tm_mday, rawCreationTime.tm_year]
    inDateRange = False

    # If Directory
    if (os.path.isdir(path)):
        dirlist = os.listdir(path)

        # Identify if the file meets the search pattern

        for item in dirlist:
            if (os.path.isdir(f'{path}/{item}')):

                # Does search directory meet search pattern
                for dateSet in pattern:
                    sDateSet = dateSet.split('-')


                # Recursively search subdirectory if applicable
                if (recursiveFlag == True):
                    SearchDateCreated(f'{path}/{item}', pattern, recursiveFlag)



            else:
                SearchDateCreated(f'{path}/{item}', pattern, recursiveFlag)



        # Return list of directory and file objects meeting search pattern

    # If file
    else:
        for dateSet in pattern:
            sDateSet = dateSet.split('-')
            # If there is only one date in a particular set of dates
            if (len(sDateSet) == 1 or sDateSet[1] == ''):
                compDate = sDateSet[0].split('/')
                for index in range(len(compDate)):
                    compDate[index] = int(compDate[index])
                if (creationDate == compDate):
                    print('Same') # If dates are in fact the same
                else:
                    print('Not the same') # if dates are not the same
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
                if (creationDate[2] >= firstDate[2]) and (creationDate[2] <= lastDate[2]):
                    if (creationDate[0] >= firstDate[0]) and (creationDate[0] <= lastDate[0]):
                        if (creationDate[1] >= firstDate[1]) and (creationDate[1] <= lastDate[1]):
                            # If it is in the date range
                            inDateRange = True
                            break
                        else:
                            # If its not in the date range
                            continue
                    else:
                        # if its not in the date range
                        continue
                else:
                    # If its not in the date range
                    continue

        if (inDateRange == True):
            file = FileClass.File(path)
            return [file]
        else:
            return []

def TestDateForMatch(date, pattern) -> bool:
    '''
    This function tests to see if a date falls within a particular range of dates
    :param date: A list of integers representing a date in the following format [mm/dd/yy]
    :param pattern: A list of strings of the form "m1m1/d1d1/y1y1-m2m2/d2d2/y2y2"
    :return: True if date matches pattern, False if date does not match pattern
    '''
    inDateRange = False
    for dateSet in pattern:
        sDateSet = dateSet.split('-')
        # If there is only one date in a particular set of dates
        if (len(sDateSet) == 1 or sDateSet[1] == ''):
            compDate = sDateSet[0].split('/')
            for index in range(len(compDate)):
                compDate[index] = int(compDate[index])
            if (date == compDate):
                inDateRange = True  # If dates are in fact the same
            else:
                inDateRange = False  # if dates are not the same
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
                if (date[0] >= firstDate[0]) and (date[0] <= lastDate[0]):
                    if (date[1] >= firstDate[1]) and (date[1] <= lastDate[1]):
                        # If it is in the date range
                        inDateRange = True
                        break
                    else:
                        # If its not in the date range
                        pass
                else:
                    # if its not in the date range
                    pass
            else:
                # If its not in the date range
                pass

    if (inDateRange == True):
        return True
    else:
        return False


if __name__ == "__main__":
    print(TestDateForMatch([3, 2, 1993], ['1/1/1971-1/1/1994']))