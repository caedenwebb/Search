import os

def SearchFileSize(dir, min_bytes, max_bytes):
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
    for file in fileList:
        if (os.path.isdir(f'{dir}/{file}')):
            continue
        else:
            filesize = os.path.getsize(f'{dir}/{file}')
            if (min_bytes <= filesize <= max_bytes):
                retList.append(f'{dir}/{file}')

    return retList