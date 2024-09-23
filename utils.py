# Python Libraries
import sys
# Internal Project Files

# External Libraries

def SearchString(SearchString, PatternString) -> bool:
    '''
    Takes in a string to search for a pattern, and returns whether the string contains the pattern
    :param SearchString: Takes in a string to search for a pattern
    :param SearchPattern: Takes in a pattern to compare
    :return: Boolean value stating whether the string contains the pattern
    '''

    SearchStringLen = len(SearchString)
    PatternStringLen = len(PatternString)

    if (PatternStringLen > SearchStringLen):
        return False
    elif (PatternStringLen == SearchStringLen):
        if (PatternString == SearchString):
            return True
        else:
            return False
    else:
        offset = 0
        Index = 0
        Equal = True
        while (PatternStringLen + offset <= SearchStringLen):
            Equal = True
            for char in PatternString:
                if (PatternString[Index] == SearchString[Index + offset]):
                    Index = Index + 1
                    continue
                else:
                    Equal = False
                    break
            if (Equal == True):
                return True
            else:
                Index = 0
                offset = offset + 1
                continue
        return False

def CheckDate(date: str):
    '''
    Checks a date to see if the date is a valid date; will exit the code if the date is invalid
    :param date: Takes a date in the form (1/1/2004)
    :return: None
    '''

    if (int(date.split('/')[2]) <= 1969):
        print(f'\nError: \'{date}\' is invalid because Search does not support dates prior to 1/1/1970.')
        sys.exit()
    elif (int(date.split('/')[0]) <= 0 or int(date.split('/')[0]) >= 13):
        print(f'\nError: \'{date}\' is not a valid date.')
        sys.exit()
    else:
        # Months other than February
        if (date.split('/')[0] == '1'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 32):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of January (1-31).\n')
                sys.exit()
        elif (date.split('/')[0] == '3'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 32):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of March (1-31).\n')
                sys.exit()
        elif (date.split('/')[0] == '4'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 31):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of April (1-30).\n')
                sys.exit()
        elif (date.split('/')[0] == '5'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 32):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of May (1-31).\n')
                sys.exit()
        elif (date.split('/')[0] == '6'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 31):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of June (1-30).\n')
                sys.exit()
        elif (date.split('/')[0] == '7'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 32):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of July (1-31).\n')
                sys.exit()
        elif (date.split('/')[0] == '8'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1]) >= 32):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of August (1-31)\n.')
                sys.exit()
        elif (date.split('/')[0] == '9'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1] >= 31)):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of September (1-30)\n.')
                sys.exit()
        elif (date.split('/')[0] == '10'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1] >= 32)):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of October (1-31)\n.')
                sys.exit()
        elif (date.split('/')[0] == '11'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1] >= 31)):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of November (1-30)\n.')
                sys.exit()
        elif (date.split('/')[0] == '12'):
            if (int(date.split('/')[1]) <= 0 or int(date.split('/')[1] >= 32)):
                print(f'\nError: \'{date}\' is not a valid date because \'{date.split('/')[1]}\' is not in the range of days in the month of December (1-31)\n.')
                sys.exit()
        # February
        else:
            pass
def CheckDateRange(firstDate: str, secondDate: str):
    lFirstDate = secondDate.split('/')
    lSecondDate = secondDate.split('/')

    if (lSecondDate[2] > lFirstDate[2]):
        print(f'\nError: \'{firstDate}-{secondDate}\' is not a valid date-range because \'{secondDate}\' is later than \'{firstDate}\'')
        sys.exit()