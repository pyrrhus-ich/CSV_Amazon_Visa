# import built in module
import shutil, os.path
# import eigene module
from settings import *
from loghandler import logger as lg
import re


# Räumt den dst Folder auf und verschiebt die Files nach arc

def cleanDst(dst):
    lg.info("<<<<<<<<<<<<<<   CLEARING DST Folder gestartet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    dir = os.listdir(dst)
    for el in dir:
        src = dst + el
        reg = re.findall('csv$', src)
        if reg:
            shutil.move(src, arcFolder)
            lg.info("{} was moved to arc".format(el))
    lg.info("<<<<<<<<<<<<<<<  CLEARING DST Folder BEENDET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def cleanArc(arc):
    lg.info("<<<<<<<<<<<<<<< Clearing Arc gestartet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    dir = os.listdir(arc)
    dirSort = sorted(dir)
    lenDirSort = len(dirSort)
    while lenDirSort > 5:
        remFile = arc + dirSort[0]
        reg = re.findall('csv$', remFile)
        if reg:
            os.remove(remFile)
            lg.info("File {} removed".format(dirSort[0]))
            lenDirSort = lenDirSort -1
            dirSort.pop(0)
    lg.info("<<<<<<<<<<<<< Clearing Arc beendet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    
   
def cleanLog(log):
    lg.info('<<<<<<<<<<<  Clearing Logfile gestartet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    dir = os.listdir(log)
    dirSort = sorted(dir)
    lenDirSort = len(dirSort)
    while lenDirSort > 3 :
        fileName = dirSort[lenDirSort - 1]
        remFile = log + fileName
        reg = re.findall('visaFunc+', remFile)
        if reg:
            os.remove(remFile)
            dirSort.pop()
            lg.info("File : {} removed from Logfolder".format(fileName))
            lenDirSort = lenDirSort -1
    lg.info("<<<<<<<<<<<<<< Clearing Logfiles beendet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
       


    
        


