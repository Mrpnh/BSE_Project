from zipfile import ZipFile
from bse.downloadFromWeb import requestWeb
from bse.setExport import setStatic
import os
from datetime import datetime

def routine():
    # This will be a routine when home page is loaded
    staticfile=setStatic()
    now=datetime.now()
    day=now.strftime("%d")
    month=now.strftime("%m")
    year=now.strftime("%y")
    if staticfile != f"EQ{day}{month}{year}.CSV":
        statusFromWeb=requestWeb()  
        if statusFromWeb!="None":
            path_parent = os.path.dirname(os.getcwd())
            os.chdir("static/")
            with ZipFile(statusFromWeb,'r') as zip:
                zip.extractall()
            os.remove(statusFromWeb)
            os.remove(staticfile)
            os.chdir(path_parent)