from datetime import datetime as dt
import os


workDir = os.getcwd()

# legt dateTime fest damit jede datei unique benamst werden kann
now = dt.now()
dateTime = now.strftime("%Y%m%d-%H%M%S")

srcFolder = workDir + "/src/"
srcFile = os.listdir(srcFolder)[0]
src = srcFolder + srcFile

dstFolder = workDir + "/dst/"
dstFile = dstFolder + dateTime + '-Importfile' + '.csv'

arcFolder = workDir + "/arc/"

logFolder = workDir + "/log/"