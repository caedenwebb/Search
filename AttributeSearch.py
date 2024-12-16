# Python Libraries
import os
import sys
import time

# Internal Project Files
import SearchDate
import SearchName
import SearchFileSize
import SortOutput
import utils
import FormatOutput

def AttributeSearch():

    # When only the mode is specified
    if (len(sys.argv) < 3):
        AttributeSearchInstructions()
        sys.exit() # For exiting to ensure that the following if statements do not run

    # When input is: "search" followed by a space and then an invalid or non-existent path.
    if (os.path.exists(sys.argv[2]) == False or os.path.isdir(sys.argv[2]) == False):
        print(f'Error: Invalid path: \'{sys.argv[2]}\' entered.\n')
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # When the user fails to specify an attribute to search
    if (len(sys.argv) < 4 or sys.argv[3] == ''):
        print('Error: No attribute provided to search.\n')
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # When the user specifies the filename attribute to search
    if (sys.argv[3] == 'filename'):
        FileNameSearch()
        sys.exit()  # For exiting to ensure that the following if statements do not run

    if (sys.argv[3] == 'file-size'):
        FileSizeSearch()
        sys.exit()  # For exiting to ensure that the following if statements do not run

    if (sys.argv[3] == 'date-created'):
        DateCreatedSearch()
        sys.exit()  # For exiting to ensure that the following if statements do not run

    if (sys.argv[3] == 'date-modified'):
        DateModifiedSearch()
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # When an unsupported or invalid attribute is specified
    print(f'Error: Invalid attribute: \'{sys.argv[3]}\'.')

def FileNameSearch():
    # Check flags
    recursiveFlag = False
    outputToFile = False
    outputFilePath = ''
    SimpleStringOutput = False
    if (len(sys.argv) > 6 and sys.argv[6] != ' '):
        i = 6
        while (i != len(sys.argv)):
            if (sys.argv[i] == '/r'):
                recursiveFlag = True
            elif (sys.argv[i].startswith('/f')):
                outputToFile = True
                if (sys.argv[i].startswith('/f=')):
                    outputFileFlag = sys.argv[i].split('=')
                    if (outputFileFlag[1] == ''):
                        print('Error: No output file path, or an invalid output file path, has been provided.')
                        sys.exit()
                    else:
                        try:
                            fileObject = open(f'{outputFileFlag[1]}', 'w')
                            fileObject.close()
                        except:
                            print('Error: Invalid output file path provided.')
                            sys.exit()
                        outputFilePath = outputFileFlag[1]
                else:
                    print('Error: No output file path provided.')
                    sys.exit()
            elif (sys.argv[i] == '/str'):
                SimpleStringOutput = True
            else:
                print(f'Error: Flag \'{sys.argv[i]}\' is not recognized.')
                sys.exit()
            i = i + 1

    # If proper input is specified (i.e. a directory, attribute, and pattern)
    if (len(sys.argv) > 5 and (sys.argv[4] == 'str' or sys.argv[4] == 'regex')):
        # Execute the search
        startTime = time.time_ns()
        filelist = SearchName.SearchName(sys.argv[2], sys.argv[4], sys.argv[5], recursiveFlag)
        endTime = time.time_ns()
        timeUsed = endTime - startTime

        # Print out file list
        if (SimpleStringOutput == False):
            FormatOutput.OutputAttributes(filelist, len(filelist), timeUsed)
        else:
            FormatOutput.SimpleStringOutput(filelist)

        if (outputToFile == True):
            FormatOutput.OutputToFile(filelist, outputFilePath)

    # When the user fails to specify a search pattern
    if (len(sys.argv) == 5 and sys.argv[4] != 'regex' and sys.argv[4] != 'str'):
        print(f'Error: \'{sys.argv[4]}\' is not a recognized pattern type.')
        sys.exit()


def FileSizeSearch():
    # Check flags
    recursiveFlag = False
    alphabetize = False
    size = True
    smallestFirst = True
    largestFirst = False
    earliestFirst = True
    latestFirst = False
    date_created = False
    date_modified = False
    outputToFile = False
    SimpleStringOutput = False
    outputFilePath = ''
    if (len(sys.argv) > 5 and sys.argv[5] != ' '):
        i = 5
        while (i != len(sys.argv)):
            if (sys.argv[i] == '/r'):
                recursiveFlag = True
            elif (sys.argv[i].startswith('/f')):
                outputToFile = True
                if (sys.argv[i].startswith('/f=')):
                    outputFileFlag = sys.argv[i].split('=')
                    if (outputFileFlag[1] == ''):
                        print('Error: No output file path, or an invalid output file path, has been provided.')
                        sys.exit()
                    else:
                        try:
                            fileObject = open(f'{outputFileFlag[1]}', 'w')
                            fileObject.close()
                        except:
                            print('Error: Invalid output file path provided.')
                            sys.exit()
                        outputFilePath = outputFileFlag[1]
                else:
                    print('Error: No output file path provided.')
                    sys.exit()
            elif (sys.argv[i] == '/str'):
                SimpleStringOutput = True
            elif (sys.argv[i] == '/a'):
                date_created = False
                date_modified = False
                alphabetize = True
                size = False
            elif (sys.argv[i] == '/ra'):
                date_created = False
                date_modified = False
                alphabetize = False
                size = False
            elif (sys.argv[i].startswith('/s') and sys.argv[i] != '/str'):
                date_created = False
                date_modified = False
                alphabetize = False
                size = True
                if (sys.argv[i] == '/s=sf'):
                    smallestFirst = True
                    largestFirst = False
                elif (sys.argv[i] == '/s=lf'):
                    smallestFirst = False
                    largestFirst = True
                else:
                    print('Error: Failure to specify order (smallest to largest or largest to smallest). Should be specified as follows: /s=sf or /s=lf')
                    sys.exit()
            elif (sys.argv[i].startswith('/dc')):
                date_created = True
                date_modified = False
                alphabetize = False
                size = False
                if (sys.argv[i] == '/dc=ef'):
                    earliestFirst = True
                    latestFirst = False
                elif (sys.argv[i] == '/dc=lf'):
                    latestFirst = True
                    earliestFirst = False
                else:
                    print(
                        'Error: Failure to specify order (earliest first or latest first). Should be specified as follows: /s=ef or /s=lf')
                    sys.exit()
            elif (sys.argv[i].startswith('/dm')):
                date_created = False
                date_modified = True
                alphabetize = False
                size = False
                if (sys.argv[i] == '/dm=ef'):
                    earliestFirst = True
                    latestFirst = False
                elif (sys.argv[i] == '/dm=lf'):
                    latestFirst = True
                    earliestFirst = False
                else:
                    print('Error: Failure to specify order (earliest first or latest first). Should be specified as follows: /s=ef or /s=lf')
                    sys.exit()
            else:
                print(f'Error: Flag \'{sys.argv[i]}\' is not recognized.')
                sys.exit()
            i = i + 1
    # If the user does not provide a size range
    if (len(sys.argv) < 5):
        print('Error: No size range provided.\n')
        sys.exit()
    '''
    Size ranges are to be specified by the user as follows: "[minimum]-[maximum][sizeUnit]"
    
    Supported size units:
        1. b ----- bytes
        2. kb ---- kilobytes
        3. mb ---- megabytes
        4. gb ---- gigabytes
        5. tb ---- terabytes
    
    '''

    sizeRange = sys.argv[4].split('-')  # Take search argument and split it into a list with two members based on the hyphen

    # Attempt to determine the maximum and minimum ranges by obtaining it from the list and converting them to integers
    try:
        rightValue = sizeRange[1]

        maximumValueString = ''
        curIndex = 0
        for char in rightValue:
            if (char.isnumeric()):
                maximumValueString = maximumValueString + char
                curIndex = curIndex + 1
            else:
                break

        units = rightValue[curIndex:]
        minVal = 0
        maxVal = 0
        if (units == '' or units == 'b'):
            minVal = int(sizeRange[0])
            maxVal = int(maximumValueString)

        elif (units == 'kb'):
            minVal = int(sizeRange[0])*1000
            maxVal = int(maximumValueString)*1000

        elif (units == 'mb'):
            minVal = int(sizeRange[0])*1000*1000
            maxVal = int(maximumValueString)*1000*1000

        elif (units == 'gb'):
            minVal = int(sizeRange[0])*1000*1000*1000
            maxVal = int(maximumValueString)*1000*1000*1000

        elif (units == 'tb'):
            minVal = int(sizeRange[0])*1000*1000*1000*1000
            maxVal = int(maximumValueString)*1000*1000*1000*1000

        else:
            print(f'Error: \'{units}\' is not a recognized unit.')
            sys.exit()

    # If the user fails to input a range correctly (e.g. failure to use a hyphen to divide minimum and maximum)
    except IndexError:
        print("Error: Input size ranges as follows: [minimum]-[maximum][sizeUnit]\n")
        sys.exit()

    # If the user inputs a range correctly, but specified anything that cannot be converted to an int (e.g. 30-15d)
    except ValueError:
        print("Error: Search only accepts integer size ranges\n")
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # Check if the size range minimum is smaller than or equal to the maximum:
    if (minVal > maxVal):
        print(f"\nError: Search minimum '{minVal}' is greater than search maximum '{maxVal}'. Did you mean '{maxVal}-{minVal}?'\n")
        sys.exit()

    # Execute the search
    startTime = time.time_ns()
    res = SearchFileSize.SearchFileSize(sys.argv[2], minVal, maxVal, recursiveFlag)
    endTime = time.time_ns()
    timeUsed = endTime - startTime

    # Sort Output
    # Format output
    if (alphabetize == True):
        res = SortOutput.OrderAToZ(res)
    elif (size == True):
        if (smallestFirst == True):
            res[0] = SortOutput.SmallestToLargest(res[0])
        else:
            res[0] = SortOutput.LargestToSmallest(res[0])
    elif (date_created == True):
        if (earliestFirst == True):
            res[0] = SortOutput.DCOldestToNewest(res[0])
        else:
            res[0] = SortOutput.DCNewestToOldest(res[0])
    elif (date_modified == True):
        if (earliestFirst == True):
            res[0] = SortOutput.DMOldestToNewest(res[0])
        else:
            res[0] = SortOutput.DMNewestToOldest(res[0])
    else:
        res[0] = SortOutput.OrderZToA(res[0])

    # Print out file list
    FormatOutput.OutputAttributes(res[0], len(res[0]), timeUsed)

def DateCreatedSearch():
    # Check flags
    recursiveFlag = False
    outputToFile = False
    SimpleStringOutput = False
    outputFilePath = ''
    if (len(sys.argv) > 5 and sys.argv[5] != ' '):
        i = 5
        while (i != len(sys.argv)):
            if (sys.argv[i] == '/r'):
                recursiveFlag = True
            elif (sys.argv[i].startswith('/f')):
                outputToFile = True
                if (sys.argv[i].startswith('/f=')):
                    outputFileFlag = sys.argv[i].split('=')
                    if (outputFileFlag[1] == ''):
                        print('Error: No output file path, or an invalid output file path, has been provided.')
                        sys.exit()
                    else:
                        try:
                            fileObject = open(f'{outputFileFlag[1]}', 'w')
                            fileObject.close()
                        except:
                            print('Error: Invalid output file path provided.')
                            sys.exit()
                        outputFilePath = outputFileFlag[1]
                else:
                    print('Error: No output file path provided.')
                    sys.exit()
            elif (sys.argv[i] == '/str'):
                SimpleStringOutput = True
            i = i + 1
    # Check that a search pattern was provided
    if (len(sys.argv) < 5):
        print('Error: No search pattern provided.\n')
        sys.exit()

    # Prelimary checks that dates are valid dates
    dateSets = sys.argv[4].split(';')
    for dateSet in dateSets:
        sDateSet = dateSet.split('-')
        if (len(sDateSet) == 1):
            if (utils.CheckDate(sDateSet[0]) == False):
                sys.exit()
            continue
        firstDate = sDateSet[0]
        lastDate = sDateSet[1]
        if (utils.CheckDate(firstDate) == False):
            sys.exit()
        if (utils.CheckDate(lastDate) == False):
            sys.exit()

    # Sanity checks on date ranges
    for dateSet in dateSets:
        sDateSet = dateSet.split('-')
        if (len(sDateSet) == 1):
            continue
        else:
            if utils.CheckDateRange(sDateSet[0], sDateSet[1]) == False:
                sys.exit()

    # Execute search on date ranges
    starttime = time.time_ns()
    results = SearchDate.SearchDateCreated(sys.argv[2], dateSets, recursiveFlag)
    endtime = time.time_ns()
    duration = endtime - starttime

    if (outputToFile == False and SimpleStringOutput == False):
        FormatOutput.OutputAttributes(results, len(results), duration)
    elif (SimpleStringOutput == True):
        for item in results:
            print(item.filename)
    elif (outputToFile == True):
        FormatOutput.OutputToFileTable(results, outputFilePath)
def DateModifiedSearch():
    # Check flags
    recursiveFlag = False
    alphabetize = False
    size = False
    smallestFirst = True
    largestFirst = False
    earliestFirst = True
    date_created = False
    date_modified = True
    latestFirst = False
    outputToFile = False
    SimpleStringOutput = False
    outputFilePath = ''
    if (len(sys.argv) > 5):
        i = 5
        while (i != len(sys.argv)):
            if (sys.argv[i] == '/r'):
                recursiveFlag = True
            elif (sys.argv[i].startswith('/f')):
                outputToFile = True
                if (sys.argv[i].startswith('/f=')):
                    outputFileFlag = sys.argv[i].split('=')
                    if (outputFileFlag[1] == ''):
                        print('Error: No output file path, or an invalid output file path, has been provided.')
                        sys.exit()
                    else:
                        try:
                            fileObject = open(f'{outputFileFlag[1]}', 'w')
                            fileObject.close()
                        except:
                            print('Error: Invalid output file path provided.')
                            sys.exit()
                        outputFilePath = outputFileFlag[1]
                else:
                    print('Error: No output file path provided.')
                    sys.exit()
            elif (sys.argv[i] == '/str'):
                SimpleStringOutput = True
            elif (sys.argv[i] == '/a'):
                date_created = False
                date_modified = False
                alphabetize = True
                size = False
            elif (sys.argv[i] == '/ra'):
                date_created = False
                date_modified = False
                alphabetize = False
                size = False
            elif (sys.argv[i].startswith('/s') and sys.argv[i] != '/str'):
                date_created = False
                date_modified = False
                alphabetize = False
                size = True
                if (sys.argv[i] == '/s=sf'):
                    smallestFirst = True
                    largestFirst = False
                elif (sys.argv[i] == '/s=lf'):
                    smallestFirst = False
                    largestFirst = True
                else:
                    print('Error: Failure to specify order (smallest to largest or largest to smallest). Should be specified as follows: /s=sf or /s=lf')
                    sys.exit()
            elif (sys.argv[i].startswith('/dc')):
                date_created = True
                date_modified = False
                alphabetize = False
                size = False
                if (sys.argv[i] == '/dc=ef'):
                    earliestFirst = True
                    latestFirst = False
                elif (sys.argv[i] == '/dc=lf'):
                    latestFirst = True
                    earliestFirst = False
                else:
                    print('Error: Failure to specify order (earliest first or latest first). Should be specified as follows: /s=ef or /s=lf')
                    sys.exit()
            elif (sys.argv[i].startswith('/dm')):
                date_created = False
                date_modified = True
                alphabetize = False
                size = False
                if (sys.argv[i] == '/dm=ef'):
                    earliestFirst = True
                    latestFirst = False
                elif (sys.argv[i] == '/dm=lf'):
                    latestFirst = True
                    earliestFirst = False
                else:
                    print('Error: Failure to specify order (earliest first or latest first). Should be specified as follows: /s=ef or /s=lf')
                    sys.exit()
            else:
                print(f'Error: Flag \'{sys.argv[i]}\' is not recognized.')
                sys.exit()
            i = i + 1
    # Check that a search pattern was provided
    if (len(sys.argv) < 5):
        print('Error: No search pattern provided.\n')
        sys.exit()

    # Prelimary checks that dates are valid dates
    dateSets = sys.argv[4].split(';')
    for dateSet in dateSets:
        sDateSet = dateSet.split('-')
        if (len(sDateSet) == 1):
            if (utils.CheckDate(sDateSet[0]) == False):
                sys.exit()
            continue
        firstDate = sDateSet[0]
        lastDate = sDateSet[1]
        if (utils.CheckDate(firstDate) == False):
            sys.exit()
        if (utils.CheckDate(lastDate) == False):
            sys.exit()

    # Sanity checks on date ranges
    for dateSet in dateSets:
        sDateSet = dateSet.split('-')
        if (len(sDateSet) == 1):
            continue
        else:
            if (utils.CheckDateRange(sDateSet[0], sDateSet[1]) == False):
                sys.exit()

    # Execute search on date ranges
    starttime = time.time_ns()
    results = SearchDate.SearchDateModified(sys.argv[2], dateSets, recursiveFlag)
    endtime = time.time_ns()
    duration = endtime - starttime

    if (outputToFile == False and SimpleStringOutput == False):
        FormatOutput.OutputAttributes(results, len(results), duration)
    elif (SimpleStringOutput == True):
        for item in results:
            print(item.filename)
    elif (outputToFile == True):
        FormatOutput.OutputToFileTable(results, outputFilePath)


def AttributeSearchInstructions(tab=''):
    print(f'\n{tab}Usage: {sys.argv[0]} -a [directory] [attribute] [pattern] [flags]')
    print(f'\n{tab}   Data Attributes to Search:\n')
    print(f'{tab}   filename ------------------ returns files and directories containing the given pattern in their filenames')
    print(f'{tab}   file-size ------------------ returns files and directories matching the size range provided in the pattern for their filesize')
    print(f'{tab}   date-created --------------- returns files and directories matching the date range provided in the pattern for their creation dates')
    print(f'{tab}   date-modified -------------- returns files and directories matching the date range provided in the pattern for their modification dates\n')

    print(f'{tab}   For filename searches:')
    print(f'{tab}     Special Usage: {sys.argv[0]} -a [directory] [attribute] [pattern type] [pattern] [flags]')
    print(f'{tab}       Filename Search Pattern Types: ')
    print(f'{tab}          \'str\' ------------------ searches for files and directories having a filename matching a string literal pattern')
    print(f'{tab}          \'regex\' ---------------- searches for files and directories having a filename matching a regular expression pattern\n')

    print(f'{tab}   For File Size Searches:')
    print(f'{tab}       Flags: ')
    print(f'{tab}          \'/r\' -- recursive, enables recursion through subdirectories of the search directory\n')

    print(f'{tab}   Usage: {sys.argv[0]} -a [directory] file-size [minValue]-[maxValue][units: OPTIONAL]')
    print(f'{tab}       Valid Units for File-Size Searches:')
    print(f'{tab}             1. \'b\' (bytes)')
    print(f'{tab}             2. \'kb\' (kilobytes)')
    print(f'{tab}             3. \'mb\' (megabytes)')
    print(f'{tab}             4. \'gb\' (gigabytes)')
    print(f'{tab}             5. \'tb\' (terabytes)')

    print(f'\n{tab}   For Date Created Searches:\n')
    print(f'{tab}   Usage: {sys.argv[0]} -a [directory] date-created [datesList]')
    print(f'{tab}      How to enter dates:')
    print(f'{tab}         1. Enter all sets of date ranges separated by semi-colons')
    print(f'{tab}         2. Enter date ranges with the first date covered by the range on the left, and the last date on the right, separated by a \'-\'')
    print()
    print(f'{tab}      Examples:')
    print(f'{tab}         1. {sys.argv[0]} -a [directory] date-created "1/2/2015-1/3/2016" -- identifies all files created between January 2, 2015 and January 3, 2016, inclusive')
    print(f'{tab}         2. {sys.argv[0]} -a [directory] date-created "1/2/2015-1/3/2016;1/9/2016" -- identifies all files created between January 2, 2015 and January 3, 2016, inclusive, \n{tab}{tab} as well as any files created on January 9, 2016')
    print(f'{tab}         3. {sys.argv[0]} -a [directory] date-created "1/2/2015-1/3/2016;1/9/2016-1/10/2016" -- identifies all files created between January 2, 2015 and January 3, 2016, inclusive\n{tab}{tab} as well as all files created on January 9, 2016 or January 10, 2016\n')