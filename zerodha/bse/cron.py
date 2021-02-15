from zipfile import ZipFile
from bse.downloadFromWeb import requestWeb
from bse.setExport import setStatic

def routine():
    statusFromWeb=requestWeb()
    staticfile=setStatic()
    analyseCSV(filename)
    if requestWeb!="None":
        path_parent = os.path.dirname(os.getcwd())
        os.chdir("static/")
        with ZipFile(filename,'r') as zip:
             zip.extractall()
        os.remove(filename)
        os.remove(staticfile)
        os.chdir(path_parent)
