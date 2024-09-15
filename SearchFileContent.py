import os
import sys
import FileClass
import utils

def SearchFile(path, pattern) -> tuple:
    matchesPattern = False
    file = FileClass.File(path)
    file.ReturnData = []
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

    return (matchesPattern, file)