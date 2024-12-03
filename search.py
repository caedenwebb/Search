# Python Libraries
import os
import sys
import time

# Internal Project Files
import SearchName
import SearchFileSize
import AttributeSearch
import FileContentSearch
from ModelSearchPkg import ModelSearch
from SearchSessionsPkg import SearchSession

# External Libraries


def main():

    # When input is either: "search" or "python search.py"
    if (len(sys.argv) < 2):
        print('\nUsage: search [search type] [arguments]') # [directory/file] [attribute] [pattern]
        print('\n  Search Types:')
        print('    \'-a\' Attribute Search ---------- Searches the attributes of files and directories within a directory for a specific pattern')
        print('    \'-f\' File Content Search ------- Searches the content of a file for a given pattern, or the files in a directory for a given pattern')
        print('    \'-m\' Model Search Mode --------- Run attribute searches on a model of a directory or filesystem for given information generated for quick searches')
        print('    \'-s\' Search Session Mode ------- Open a search session on a particular directory and execute searches on a search model generated in RAM')
        print('')
        print('\tATTRIBUTE SEARCH INSTRUCTIONS:')
        AttributeSearch.AttributeSearchInstructions('\t')
        print()
        print('\tFILE CONTENT SEARCH INSTRUCTIONS:')
        FileContentSearch.FileContentSearchInstructions('\t')
        print()
        print('\tMODEL SEARCH INSTRUCTIONS:')
        print()
        ModelSearch.ModelSearchInstructions('\t')
        print()
        sys.exit()

    # Determine the search mode
    # Attribute Mode
    if (sys.argv[1] == '-a'):
        AttributeSearch.AttributeSearch()
    # File Content Mode
    elif (sys.argv[1] == '-f'):
        FileContentSearch.FileContentSearch()
    # Model Mode
    elif (sys.argv[1] == '-m'):
        ModelSearch.ModelSearch()
    # Search Session
    elif (sys.argv[1] == '-s'):
        SearchSession.SearchSessionMain()
    # Invalid Mode
    else:
        print(f"Error: Invalid mode: '{sys.argv[1]}'")


if __name__ == "__main__":
    main()