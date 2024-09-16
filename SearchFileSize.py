import os

def SearchFileSize(dir, min_bytes, max_bytes) -> list:
    '''
    Returns a list of files (and directories?) that are within the range of min_bytes and max_bytes inclusive
    :param dir: Directory to search
    :param min_bytes: Minimum byte size
    :param max_bytes: Maximum byte size
    :return:
    '''
    # os.path.getsize() -> integer value representing size in bytes

    fileList = os.listdir(dir)
    retList = []
    dirSize = os.path.getsize(dir)

    for file in fileList:
        if (os.path.isdir(f'{dir}/{file}')):
            try:
                res = SearchFileSize(f'{dir}/{file}', min_bytes, max_bytes)
            except PermissionError:
                continue
            except OSError:
                continue
            retList = retList + res[0]
            dirSize = dirSize + res[1]
        else:
            filesize = os.path.getsize(f'{dir}/{file}')
            if (min_bytes <= filesize <= max_bytes):
                retList.append(f'{dir}/{file}')
                dirSize = dirSize + filesize
            else:                        
                dirSize = dirSize + filesize

    if (min_bytes <= dirSize <= max_bytes):
        retList = retList + [dir]

    return [retList, dirSize]