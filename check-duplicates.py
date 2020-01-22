from __future__ import print_function
import os, hashlib, datetime, time

'''
This script goes through a given directory and it's subdirectories
and check if there are an duplicate files
'''
def findDuplicateFiles(pth, minSize = 0):
    visitedFiles = {}
    duplicates = []

    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(pth):
        for file in files:
            fullFileName = os.path.join(root, file)
            isLink = os.path.islink(fullFileName)
            
            if isLink:
                continue # Skip links(shortcuts)

            si = os.path.getsize(fullFileName)
            if si < minSize:
                continue # Skip files below a specified size threshold
            
            print(fullFileName)
            #fi = open(fullFileName, "rb")
            #data = fi.read()
            checksum = hashlib.blake2b(open(fullFileName, "rb").read()).hexdigest()
            #fi.close()
            
            if checksum in visitedFiles:
                fileRec = visitedFiles[checksum]
                fileRec.append(fullFileName)
                duplicates.append(fileRec)
            else:
                visitedFiles[checksum] = [fullFileName]
    
    print()
    
    for dup in duplicates:
        print("=======Duplicate=======")
        for d in dup:
            print(os.path.relpath(d, pth))

if __name__ == "__main__":
    findDuplicateFiles('D:\Libraries\Downloads\Video', 1024*1024)