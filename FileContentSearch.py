import re
import os
import sys
import utils
import time
import FileClass
from FormatOutput import OutputFileContentSearch


def FileContentSearch():
    # If the user types "search -f"
    if (len(sys.argv) < 3):
        FileContentSearchInstructions()
        sys.exit()

    if (sys.argv[2] != 'str' and sys.argv[2] != 'regex'):
        print(f'Error: Search pattern type "{sys.argv[3]}" not recognized.')
        sys.exit()

    # if the user fails to provide a search pattern
    if (len(sys.argv) < 4):
        print('Error: No search pattern has been entered.')
        sys.exit()

    # If the user fails to provide a list of files to search
    if (len(sys.argv) < 5):
        print('Error: No files have been entered. To enter files, surround the files in quotations marks and separate them by a semi-colon.')
        sys.exit()

    # Check files for compatibility
    filelist = sys.argv[4].split(';')
    for index in range(len(filelist)):
        try:
            fileHandler = open(filelist[index], 'r')
        except FileNotFoundError:
            print(f'Error: "{filelist[index]}" not found.')
            filelist.pop(index)
        except OSError:
            print(f'Error: "{filelist[index]}" is not supported.')
            filelist.pop(index)

    # Execute search on valid files
    start_time = time.time_ns()
    results = ExecuteSearch(filelist, sys.argv[2], sys.argv[3])
    end_time = time.time_ns()
    duration = end_time - start_time


    # Output Results
    OutputFileContentSearch(results, duration)

def FileContentSearchInstructions(tab=''):
    print(f'\n{tab}Usage: search -f [pattern type] [pattern] [files] [flags]')
    print(f'\n{tab*2}Pattern type:')
    print(f'{tab*3}\'regex\' ---------- regular expression (searches files for a string of characters matching a regular expression)')
    print(f'{tab*3}\'literal\' -------- string literal (searches files for a string literal)')
    print(f'\n{tab*2}How to input files: ')
    print(f'{tab*3}EX 1: "C:/Users/John Doe.txt;G:/Files/file.txt" -- searhces the files "C:/Users/John Doe.txt" and "G:/Files/file.txt"')
    print(f'{tab*3}EX 2: "C:/Users/Caeden/item.txt" -- searches the file "C:/Users/Caeden/item.txt"')
    print(f'\n{tab*2}Flags:')
    print()  # Insert newline under final print

def ExecuteSearch(filelist, patternType, pattern) -> list:
    ReturnData = [] # List for returning a list of file objects matching the search pattern
    for file in filelist:
        fileHandler = open(file, 'r') # Object to hold the file handler for file I/O
        fileContents = fileHandler.readlines() # list to contain the lines of the file
        fileReturnObject = None # Null ptr to a fileReturnObject for the file in the event that the file matches the pattern
        lineNum = 1 # Value to store the current line number

        # If the pattern type is a string literal
        if (patternType == 'str'):
            for line in fileContents:
                line = line.strip('\n')
                if (utils.SearchString(line, pattern) == True):
                    if (fileReturnObject == None):
                        fileReturnObject = FileClass.File(file)
                        fileReturnObject.ReturnData = [[lineNum, line]]
                        lineNum = lineNum + 1
                    else:
                        fileReturnObject.ReturnData.append([lineNum, line])
                        lineNum = lineNum + 1
                else:
                    lineNum = lineNum + 1
                    continue
        # If the pattern type is a regular expression
        elif (patternType == 'regex'):
            for line in fileContents:
                line = line.strip('\n')
                if (re.match(pattern, line)):
                    if (fileReturnObject == None):
                        fileReturnObject = FileClass.File(file)
                        fileReturnObject.ReturnData = [[lineNum, line]]
                        lineNum = lineNum + 1
                    else:
                        fileReturnObject.ReturnData.append([lineNum, line])
                        lineNum = lineNum + 1
                else:
                    lineNum = lineNum + 1
                    continue
        # if the pattern type is not recognized
        else:
            print(f'Error: Pattern type {pattern} not recognized.')
            sys.exit()

        if (fileReturnObject != None):
            ReturnData.append(fileReturnObject)

    return ReturnData