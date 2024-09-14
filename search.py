import os
import sys
import SearchName
import SearchFileSize
import time

def main():

    # Variables
    SearchDir = ''
    SearchPattern = ''

    if (len(sys.argv) < 2):
        print('\nUsage: search [directory] [attribute] [pattern]')
        print('\nData Attributes to Search:')
        print('filename ------------------ returns files and directories containing the given pattern in their filenames')
        print('file-size ------------------ returns files and directories matching the size range provided in the pattern for their filesize')
        print('date-created --------------- returns files and directories matching the date range provided in the pattern for their creation dates')
        print('date-modified -------------- returns files and directories matching the date range provided in the pattern for their modification dates\n')
        sys.exit()

    if (os.path.exists(sys.argv[1]) == False or os.path.isdir(sys.argv[1]) == False):
        print(f'Error: Invalid path: \'{sys.argv[1]}\' entered.\n')
        sys.exit()

    if (len(sys.argv) < 3 or sys.argv[2] == ''):
        print('Error: No attribute provided to search.\n')
        sys.exit()

    if (sys.argv[2] == 'filename'):
        if (len(sys.argv) > 3 and sys.argv[3] != ''):
            startTime = time.time_ns()
            filelist = SearchName.SearchName(sys.argv[1], sys.argv[3])
            endTime = time.time_ns()
            timeUsed = endTime - startTime

            # Print out file list
            print(f'\nResults ({len(filelist)} results, {timeUsed}ns):\n')
            for item in filelist:
                print(item)
            print('')

        else:
            print(f'Error: No search pattern provided.\n')

        sys.exit()

    if (sys.argv[2] == 'file-size'):
        sizeRange = sys.argv[3].split('-')
        try:
            minimum = sizeRange[0]
            maximum = sizeRange[1]

            minVal = int(sizeRange[0])
            maxVal = int(sizeRange[1])

        except IndexError:
            print("Error: Input size ranges as follows: [minimum]-[maximum]")
        except ValueError:
            print("Error: Search only accepts integer size ranges")

        startTime = time.time_ns()
        filelist = SearchFileSize.SearchFileSize(sys.argv[1], minVal, maxVal)
        endTime = time.time_ns()
        timeUsed = endTime - startTime

        # Print out file list
        print(f'\nResults ({len(filelist)} results, {timeUsed}ns):\n')
        for item in filelist:
            print(item)
        print('')
        sys.exit()

    if (sys.argv[2] == 'date-created'):
        sys.exit()

    if (sys.argv[2] == 'date-modified'):
        sys.exit()


    print(f'Error: Invalid attribute: \'{sys.argv[2]}\'.')

if __name__ == "__main__":
    main()