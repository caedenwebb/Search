# Python Libraries
import os
import time

# Internal Project Files
import FileClass

# External Libraries

def SearchDateCreated(path, pattern) -> list:
    rawCreationTime = time.localtime(os.path.getctime(path))
    creationDate = [rawCreationTime.tm_mon, rawCreationTime.tm_mday, rawCreationTime.tm_year]
    inDateRange = False

    # If Directory
    if (os.path.isdir(path)):
        dirlist = os.listdir(path)

        # Identify if the file meets the search pattern

        # Recursively search the directory for files and directories meeting the search pattern (if applicable)

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

if __name__ == "__main__":
    print(SearchDateCreated('G:/My Drive/To-do list.docx', ['5/5/2024-5/29/2024']))