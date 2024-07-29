from os import listdir
from os.path import isfile, join
import sys
import shutil

filepath = sys.argv[1]
fileList = [f for f in listdir(filepath) if isfile(join(filepath, f))]
#print(fileList)
appendedFileName = "appended_file.yaml"
fullAppendedFilePath = filepath+'/'+appendedFileName
with open(fullAppendedFilePath, 'w') as outfile:
    for fileName in fileList:
        fullFilePath=filepath+'/'+fileName        
        with open(fullFilePath,'r') as infile:
            outfile.write(infile.read())
            outfile.write('\n\n---\n\n')
