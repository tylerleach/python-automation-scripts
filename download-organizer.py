from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, json, time, shutil

'''
This script sorts files moved in the downloads folder to
another folder based on the files filetype
'''

baseFolder = 'C:/Users/Tyler/Desktop/testFolder' # Downloads folder
documentsFolder = 'C:/Users/Tyler/Desktop/testDocuments'
musicFolder = 'C:/Users/Tyler/Desktop/testMusic' 
videoFolder = 'C:/Users/Tyler/Desktop/testVideos'
archiveFolder = 'C:/Users/Tyler/Desktop/testArchives'

# Lists of filetype categories and their extensions
document = ['pdf', 'txt', 'docx']
music = ['mp3', 'wav']
video = ['mkv', 'mp4', 'avi']
archive = ['zip', '7zip']

class MyHandler(FileSystemEventHandler):

    # When the baseFolder is modified (a new file is added or moved there)
    def on_modified(self, event):
        for filename in os.listdir(baseFolder):
            ext = filename.split('.')[1] # Splits the extension type from the filename
            src = baseFolder + '/' + filename #Src file location

            # If the files filetype is within the category, move file to that folder
            if ext in document:
                shutil.move(src, documentsFolder)
            elif ext in music:
                shutil.move(src, musicFolder)
            elif ext in video:
                shutil.move(src, videoFolder)
            elif ext in archiveFolder:
                shutil.move(src, archiveFolder)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, baseFolder, recursive=True)

observer.start()
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
            