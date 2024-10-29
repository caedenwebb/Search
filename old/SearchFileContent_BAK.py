# Python Libraries
import os
import sys

# Internal Project Files
import FileClass
import utils

# External Libraries

def SearchFile(path, pattern) -> tuple:
    matchesPattern = False
    file = FileClass.File(path)
    file.ReturnData = []
    try:
        file.ReadMode()
        FileContents = file.Filestream.readlines()
        lineNum = 1

        for line in FileContents:
            line = line.strip('\n')
            if (utils.SearchString(line, pattern) == True):
                file.ReturnData.append((lineNum, line))
                matchesPattern = True
                lineNum = lineNum + 1
            else:
                lineNum = lineNum + 1
    except:
        print(f'Error: Input file "{path}" not supported.')
        file.ReturnData = []

    return (matchesPattern, file)

def SearchDirectory(path, pattern, recursiveFlag) -> tuple:
    matchesPattern = False
    fileList = os.listdir(path)
    directory = FileClass.Directory(path)

    for item in fileList:
        if (os.path.isdir(f'{path}/{item}') == True):
            if (recursiveFlag == True):
                results = SearchDirectory(f'{path}/{item}', pattern, recursiveFlag)
            else:
                continue
        else:
            result = SearchFile(f'{path}/{item}', pattern)
            if (result[0] == True):
                matchesPattern = True
                directory.ReturnData.append(result[1])

    return (matchesPattern, directory)
