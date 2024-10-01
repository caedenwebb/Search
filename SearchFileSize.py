# Python Libraries
import os

# Internal Project Files

# External Libraries

def SearchFileSize(dir, min_bytes, max_bytes, recursiveFlag=False) -> list:
    '''
    Returns a list of files (and directories?) that are within the range of min_bytes and max_bytes inclusive
    :param dir: Directory to search
    :param min_bytes: Minimum byte size
    :param max_bytes: Maximum byte size
    :return:
    '''
    # os.path.getsize() -> integer value representing size in bytes

    fileList = os.listdir(dir) # List of files in the directory input into the function
    retList = [] # List of files and directories to return
    dirSize = os.path.getsize(dir) # integer value to store the size of the directory input into the function

    # Determine whether files and subdirs in directory fall within the range
    for file in fileList:
        # If the item is a directory
        if (os.path.isdir(f'{dir}/{file}')):
            if (recursiveFlag == True):
                # Recursively search the directory for files that fall in the range of min_bytes and max_bytes
                try:
                    res = SearchFileSize(f'{dir}/{file}', min_bytes, max_bytes, recursiveFlag)
                # Suppress Permission Errors and skip files which raise them
                except PermissionError:
                    continue
                # Suppress OSErrors and skip files which raise them
                except OSError:
                    continue
                # Add the returned directories to the list of returned files and directories
                retList = retList + res[0]
                # Add the returned size of the subdirectory to the size of the present directory
                dirSize = dirSize + res[1]
            else:
                continue
        # If the item is a file
        else:
            # Determine the filesize
            filesize = os.path.getsize(f'{dir}/{file}')
            # If filesize falls within the range
            if (min_bytes <= filesize <= max_bytes):
                # Add file to the list of files to return
                retList.append(f'{dir}/{file}')
                # Add file size to the size of the directory input into the function
                dirSize = dirSize + filesize
            # Include files not falling within the range in the size of the parent directory
            else:
                dirSize = dirSize + filesize

    # If the size of the directory input into the function is within the range, insert that directory into the returned file list
    if (min_bytes <= dirSize <= max_bytes):
        retList = retList + [dir]

    return [retList, dirSize]