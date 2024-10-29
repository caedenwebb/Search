import sys

def OutputAttributes(filelist: list, numberResults, time):
    print(f'\nResults ({numberResults} results, {time}ns): \n')
    print(f'{'Filename':33} | {'Path':106}| {'Filesize':18} | {'Creation Date':14} | {'Modified Date'}')
    print('-'*195)
    for item in filelist:
        PrintLine(item)
    print()

def OutputToFile(filelist, path):
    outputFile = open(path, 'w')
    outputBuffer = []
    for file in filelist:
        outputBuffer.append(f'{'{'}TYPE="{file.type}";FILENAME="{file.filename}";PATH="{file.path}";DATE_CREATED="{file.date_created}";DATE_MODIFIED="{file.date_modified}";RAWCREATIONTIME="{file.rawCreationTime}";RAWMODIFIEDTIME="{file.rawModifiedTime}"{'}'}')
    outputFile.writelines(outputBuffer)
    outputFile.close()

def SimpleStringOutput(filelist):
    outputBuffer = ''
    for file in filelist:
        outputBuffer = outputBuffer + f'{'{'}TYPE="{file.type}";FILENAME="{file.filename}";PATH="{file.path}";DATE_CREATED="{file.date_created}";DATE_MODIFIED="{file.date_modified}";RAWCREATIONTIME="{file.rawCreationTime}";RAWMODIFIEDTIME="{file.rawModifiedTime}"{'}'}'
    if (outputBuffer == ''):
        outputBuffer = '{}'
    print(outputBuffer)

def PrintLine(file):
    filename = file.filename
    path = file.path
    filesize = file.size
    CreationDate = f'{file.date_created[0]}/{file.date_created[1]}/{file.date_created[2]}'
    ModifiedDate = f'{file.date_modified[0]}/{file.date_modified[1]}/{file.date_modified[2]}'

    # Adjust filename size
    if (len(filename) > 31):
        filename = filename[:30]
        filename = filename + '...'
    # Adjust path size
    if (len(path) > 103):
        path = path[:102]
        path = path + '...'

    # String formatting with the help of: https://docs.python.org/3/library/string.html
    print(f'{filename:33} | {path:<105} | {filesize:<12} bytes | {CreationDate:<14} | {ModifiedDate:<15}')

def OutputFileContentSearch(filelist, duration):

    print(f'\nResults ({len(filelist)}, {duration}ns):')
    print(f'Search Pattern Type: {sys.argv[2]}')
    print(f'Search Pattern: \'{sys.argv[3]}\'')

    print(f'\n{'Filename':33} | {'Path':53} | Content')
    print(f'='*182)

    for file in filelist:
        # Adjust filename size
        filename = file.filename
        if (len(filename) > 31):
            filename = filename[:30]
            filename = filename + '...'

        # Adjust path size
        path = file.path
        if (len(path) > 50):
            path = path[:49]
            path = path + '...'

        # Content
        content = file.ReturnData[0][1]
        if (len(content) > 87):
            content = content[:84]
            content = content + '...'

        # Print first line:
        print(f'{filename:33} | {path:<52}  | {file.ReturnData[0][0]}. {content:<87}')

        # Print subsequent lines
        if (len(file.ReturnData) > 1):
            for index in range(1, len(file.ReturnData)):
                content = file.ReturnData[index][1]
                if (len(content) > 87):
                    content = content[:84]
                    content = content + '...'
                print(f'{' '*92}{file.ReturnData[index][0]}. {content:<87}')
        print('-'*182)