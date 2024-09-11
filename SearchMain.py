import os
import sys
import SearchName
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
        exit()

    if (os.path.exists(sys.argv[1]) == False or os.path.isdir(sys.argv[1]) == False):
        print(f'Error: Invalid path: \'{sys.argv[1]}\' entered.\n')
        exit()

    if (len(sys.argv) < 3 or sys.argv[2] == ''):
        print('Error: No attribute provided to search.\n')
        exit()

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

        exit()

    if (sys.argv[2] == 'file-size'):
        pass
        exit()

    if (sys.argv[2] == 'date-created'):
        exit()

    if (sys.argv[2] == 'date-modified'):
        exit()


    print(f'Error: Invalid attribute: \'{sys.argv[2]}\'.')

if __name__ == "__main__":
    main()