#  https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

from django.shortcuts import render,HttpResponse
from datetime import datetime
from bse.setExport import setStatic
from bse.parseCSV import analyseCSV,keys,connection



# Create your views here.
def index(request):
    global keys
    connection.flushall()
    filename=setStatic()
    context={
        'filename': f"{filename}",
        
    }
    return render(request,'index.html',context)

def search(request):
    filename=setStatic()
    analyseCSV(filename)
    value=request.POST['search'].lower()
    matching = [key for key in keys if value in key]
    answers=[]
    answers.clear()
    for match in matching:
        answers.append({'code':connection.hget(match,'code').decode('utf-8'),
            'name':connection.hget(match,'name').decode('utf-8'),
            'open':connection.hget(match,'open').decode('utf-8'),
            'high':connection.hget(match,'high').decode('utf-8'),
            'low':connection.hget(match,'low').decode('utf-8'),
            'close':connection.hget(match,'close').decode('utf-8'),
        })
    context={
        'filename': f"{filename}",
        'answers': answers,
    }
    connection.flushall()    
    return render(request,'index.html',context)
