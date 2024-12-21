import os
import time
from os import listdir, getcwd
from os.path import isfile, join, basename
import threading

# Get all files in current directory
directoryFiles = listdir(getcwd())

# Remove the name of this script so it's not included in the list
directoryFiles.remove(basename(__file__))

# current Dir
currentDir = getcwd()

# Thread function
def open_process(fileName):
    os.system(fileName)
    return

# List of all threads declared here for scope
threadList = []
ctr = 0
for fileName in directoryFiles:
    time.sleep(1)

    fileToRun = currentDir + fileName
    ctr = ctr +1
    print (ctr,"==>"+fileName)
    if fileName == "run.bat":
        print ("skipped run.bat")
        continue
    # Start a new thread for each process
    currentThread = threading.Thread(target=open_process, args=(fileName,))
    currentThread.start()
    threadList.append(currentThread)
   
# Close all threads 
for currentThread in threadList:
    currentThread.join()