def OutputAttributes(filelist: list, numberResults, time):
    print(f'\nResults ({numberResults} results, {time}ns): \n')
    print(f'{'Filename':33} | {'Path':106}| {'Filesize':18} | {'Creation Date':14} | {'Modified Date'}')
    print('-'*195)
    for item in filelist:
        PrintLine(item)
    print()

def OutputInputSearch():
    pass

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

def OutputFileContentSearch(filelist):
    print(f'{'Filename':33} | {'Path':53} | Content')
    print(f'-'*173)