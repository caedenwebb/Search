# Python Libraries
import os
import sys
import time

# Internal Project Files
import SearchFileContent


def FileContentSearch():
    # If the user types "search -f"
    if (len(sys.argv) < 3):
        FileContentSearchInstructions()
        sys.exit()

    if (len(sys.argv) < 4):
        print('Error: No search pattern has been entered.')
        sys.exit()

    # Parse directories and files input by the user
    inputFileArgument = sys.argv[2]
    inputFileList = sys.argv[2].split(';')
    filteredFileList = []
    for file in inputFileList:
        if (file == ''):
            continue
        if (os.path.exists(file)):
            filteredFileList.append(file)
        else:
            print(f'Skipping \'{file}\' because it does not exist...')

    # Parse the pattern
    pattern = sys.argv[3]

    # Parse the additional flags input by the user
    recursiveFlag = False
    outputLines = True
    outputPaths = True
    if (len(sys.argv) >= 5):
        currentIndex = 4
        while (currentIndex < len(sys.argv)):
            if (sys.argv[currentIndex] == '/r'):
                recursiveFlag = True
                currentIndex = currentIndex + 1
            elif (sys.argv[currentIndex] == '/l'):
                outputLines = True
                currentIndex = currentIndex + 1
            elif (sys.argv[currentIndex] == '/p'):
                outputPaths = True
                currentIndex = currentIndex + 1
            else:
                currentIndex = currentIndex + 1
                continue

    # Execute the search and print results
    dirNum = 1
    for file in filteredFileList:
        if (os.path.isdir(file) == True):
            results = SearchFileContent.SearchDirectory(file, pattern, recursiveFlag)
        else:
            results = SearchFileContent.SearchFile(file, pattern)
            print()
            print(f'{dirNum}. {results[1].path}:\n')
            for line in results[1].ReturnData:
                print(f'\tln {line[0]} -- "{line[1]}"')
            dirNum = dirNum + 1
    print('\n')

    # Exit
    sys.exit()

def FileContentSearchInstructions(tab=''):
    print(f'\n{tab}Usage: search -f [files/directories] [pattern] [additional flags for File Content Mode]')
    print(f'\n{tab}  Listing files and directories: Files and directories should be listed in quotes and separated by semicolons')
    print(f'\n{tab}       Ex: ')
    print(f'{tab}          On Windows: "C:/Users/John Doe;C:/testfile.txt"')
    print(f'{tab}          On Unix: "/home/John Doe;/testfile.txt"')
    print(f'\n{tab}  Flags for File Content Mode:\n')
    print(f'{tab}     1. \'/r\' (recursive) ------------------ recursively search the files in any subdirectories of the provided directories')
    print(f'{tab}     2. \'/l\' (output-lines) --------------- tells search to output the lines of the file or files containing the pattern')
    print(f'{tab}     3. \'/p\' (output-paths) --------------- tells search to output paths of files matching the pattern')
    print(f'\n{tab}     NOTE: Please note that recursively searching directories may take a long time.')
    print()  # Insert newline under final print