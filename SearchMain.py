import os
import sys

def main():

    # Variables
    SearchDir = ''
    SearchPattern = ''

    if (len(sys.argv) < 2 or ((len(sys.argv) == 2) and (sys.argv[1] == '--help' or sys.argv[1] == '-h'))):
        print('Usage: search [arguments] [directory] [pattern]')


if __name__ == "__main__":
    main()