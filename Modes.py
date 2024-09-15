import os
import sys
import SearchName
import SearchFileSize
import time

def AttributeMode():
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

        sys.exit()  # For exiting to ensure that the following if statements do not run

    if (sys.argv[3] == 'file-size'):
        '''
        Size ranges are to be specified by the user as follows: "[minimum]-[maximum]"
        '''
        sizeRange = sys.argv[4].split('-')  # Take search argument and split it into a list with two members based on the hyphen

        # Attempt to determine the maximum and minimum ranges by obtaining it from the list and converting them to integers
        try:
            minimum = sizeRange[0]
            maximum = sizeRange[1]

            minVal = int(sizeRange[0])
            maxVal = int(sizeRange[1])
        # If the user fails to input a range correctly (e.g. failure to use a hyphen to divide minimum and maximum)
        except IndexError:
            print("Error: Input size ranges as follows: [minimum]-[maximum]")
            sys.exit()
        # If the user inputs a range correctly, but specified anything that cannot be converted to an int (e.g. 30-15d)
        except ValueError:
            print("Error: Search only accepts integer size ranges")
            sys.exit()  # For exiting to ensure that the following if statements do not run

        # Execute the search
        startTime = time.time_ns()
        filelist = SearchFileSize.SearchFileSize(sys.argv[2], minVal, maxVal)
        endTime = time.time_ns()
        timeUsed = endTime - startTime

        # Print out file list
        print(f'\nResults ({len(filelist)} results, {timeUsed}ns):\n')
        for item in filelist:
            print(item)
        print('')
        sys.exit()  # For exiting to ensure that the following if statements do not run

    if (sys.argv[3] == 'date-created'):
        sys.exit()  # For exiting to ensure that the following if statements do not run

    if (sys.argv[3] == 'date-modified'):
        sys.exit()  # For exiting to ensure that the following if statements do not run

    # When an unsupported or invalid attribute is specified
    print(f'Error: Invalid attribute: \'{sys.argv[3]}\'.')

def FileContentMode():
    pass

def DirectoryContentMode():
    pass

def InputMode():
    pass