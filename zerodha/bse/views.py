#  https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

from django.shortcuts import render,HttpResponse
from datetime import datetime
from bse.setExport import setStatic
from bse.parseCSV import analyseCSV,keys,connection



# Create your views here.
def index(request):
    filename=setStatic()
    analyseCSV(filename)
    single=connection.hget('abb ltd.','open').decode('utf-8')
    context={
        'filename': f"{filename}",
        'keys':f"{keys}",
        'single':f"{single}",
    }
    return render(request,'index.html',context)