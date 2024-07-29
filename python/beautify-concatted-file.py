import os
from os import listdir, path
from os.path import isfile, join
import sys
import shutil

#Remove last N lines from the script-generated appended_file.yaml
def removeLastLines(file, numberOfLines):
    with open (file,'w') as file:
        lines = file.readlines()
        print("Number of lines BEFORE: " + len(lines))
        lines = lines[:-numberOfLines]
        print("Number of lines AFTER: " + len(lines))

#Retrieve namespace information from appended_file.yaml
def getNamespace(file):
    with open(file,'r') as file:
        for line in file:
            if "namespace" in line:
                return line.partition(':')[2].replace(' ','').replace('\n','').lower()
                break

#Retrieve kind information from appended_file.yaml
def getKind(file):
    with open(file,'r') as file:
        for line in file:
            if "kind" in line:
                return line.partition(':')[2].replace(' ','').replace('\n','').lower()
                break

#Rename old append_file.yaml to new format
def rename(oldName, newName):
    os.rename(oldName,newName)

try:
    filePath = sys.argv[1]
    linesToRemove = sys.argv[2]
    
    dirPath = os.path.dirname(filePath)
    print('file name: ' + fileName)
    namespace = getNamespace(filePath)
    kind = getKind(filePath)
    newFileName = namespace+'_'+kind+'_'+'concattedfile.yaml'
    newFilePath = os.path.join(dirPath,newFileName)

    #Removing trailing lines from file
    removeLastLines(filePath,linesToRemove)

    #Renaming file
    rename(filePath,newFilePath)
except Exception as error:
    print("An error occurred:", error)
    print("Exiting script")
    sys.exit(1)


