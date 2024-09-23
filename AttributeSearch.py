# Python Libraries
import os
import sys
import time

# Internal Project Files
import SearchName
import SearchFileSize
import utils

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
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # When an unsupported or invalid attribute is specified
    print(f'Error: Invalid attribute: \'{sys.argv[3]}\'.')

def FileNameSearch():
    # If proper input is specified (i.e. a directory, attribute, and pattern)
    if (len(sys.argv) > 4 and sys.argv[4] != ''):
        # Execute the search
        startTime = time.time_ns()
        filelist = SearchName.SearchName(sys.argv[2], sys.argv[4])
        endTime = time.time_ns()
        timeUsed = endTime - startTime

        # Print out file list
        print(f'\nResults ({len(filelist)} results, {timeUsed}ns):\n')
        for item in filelist:
            print(item)
        print('')
    # When the user fails to specify a search pattern
    else:
        print(f'Error: No search pattern provided.\n')

def FileSizeSearch():
    # If the user does not provide a size range
    if (len(sys.argv) < 5):
        print('Error: No size range provided.\n')
        sys.exit()
    '''
    Size ranges are to be specified by the user as follows: "[minimum]-[maximum]"
    '''
    sizeRange = sys.argv[4].split(
        '-')  # Take search argument and split it into a list with two members based on the hyphen

    # Attempt to determine the maximum and minimum ranges by obtaining it from the list and converting them to integers
    try:
        minimum = sizeRange[0]
        maximum = sizeRange[1]

        minVal = int(sizeRange[0])
        maxVal = int(sizeRange[1])

    # If the user fails to input a range correctly (e.g. failure to use a hyphen to divide minimum and maximum)
    except IndexError:
        print("Error: Input size ranges as follows: [minimum]-[maximum]\n")
        sys.exit()

    # If the user inputs a range correctly, but specified anything that cannot be converted to an int (e.g. 30-15d)
    except ValueError:
        print("Error: Search only accepts integer size ranges\n")
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # Check if the size range minimum is smaller than or equal to the maximum:
    if (minVal > maxVal):
        print(
            f"\nError: Search minimum '{minVal}' is greater than search maximum '{maxVal}'. Did you mean '{maxVal}-{minVal}?'\n")
        sys.exit()

    # Execute the search
    startTime = time.time_ns()
    res = SearchFileSize.SearchFileSize(sys.argv[2], minVal, maxVal)
    endTime = time.time_ns()
    timeUsed = endTime - startTime

    # Print out file list
    print(f'\nResults ({len(res[0])} results, {timeUsed}ns):\n')
    for item in res[0]:
        print(item)
    print('')

def DateCreatedSearch():
    # Check that a search pattern was provided
    if (len(sys.argv) < 5):
        print('Error: No search pattern provided.\n')
        sys.exit()

    # Check that the search pattern is valid (i.e. that all dates are valid dates; that all date ranges are valid date ranges; and that all sets of dates are separated by semicolons)
    dateSets = sys.argv[4].split(';')
    for dateSet in dateSets:
        sDateSet = dateSet.split('-')
        firstDate = sDateSet[0]
        lastDate = sDateSet[1]
        utils.CheckDate(firstDate)
        utils.CheckDate(lastDate)

def AttributeSearchInstructions(tab=''):
    print(f'\n{tab}Usage: search -a [directory] [attribute] [pattern]')
    print(f'\n{tab}   Data Attributes to Search:\n')
    print(f'{tab}   filename ------------------ returns files and directories containing the given pattern in their filenames')
    print(f'{tab}   file-size ------------------ returns files and directories matching the size range provided in the pattern for their filesize')
    print(f'{tab}   date-created --------------- returns files and directories matching the date range provided in the pattern for their creation dates')
    print(f'{tab}   date-modified -------------- returns files and directories matching the date range provided in the pattern for their modification dates\n')