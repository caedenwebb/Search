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