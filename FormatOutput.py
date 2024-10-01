def OutputAttributes(filelist: list, numberResults, time):
    print(f'\nResults ({numberResults} results, {time}ns): \n')
    print('Filename                         | Path                                                                |  File Size  | Date Created | Date Modified ')
    print('---------------------------------------------------------------------------------------------------------------------------------------------------')
    for item in filelist:
        PrintLine(item)
def PrintLine(file):
    filename = file.filename
    path = file.path
    filesize = file.size
    CreationDate = file.date_created
    ModifiedDate = file.date_modified

    # Adjust filename size
    if (len(filename) > 28):
        filename = filename[:27]
        filename = filename + '...'
    # Adjust path size
    if (len(path) > 64):
        path = path[:63]
        path = path + '...'

    print(f'{filename}|{path}|{filesize} bytes |{CreationDate}|{ModifiedDate}')