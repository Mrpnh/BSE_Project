#  https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

from django.shortcuts import render,HttpResponse
from datetime import datetime
from bse.setExport import setStatic
from bse.parseCSV import analyseCSV,keys,connection
from bse.cron import routine



# Create your views here.
def index(request):
    routine()
    global keys
    filename=setStatic()
    keys=analyseCSV(filename)
    date=filename[2:4]+'/'+filename[4:6]+'/'+filename[6:8]
    context={
        'filename': f"{filename}",
        'date' : f"{date}"
    }
    return render(request,'index.html',context)

def search(request):
    # When you make a search
    filename=setStatic()
    value=request.POST['search'].lower()
    matching = [everyMatch for everyMatch in keys if value in everyMatch]
    answers=[]
    answers.clear()

    if value=='' or len(matching)==0:
        answers.append({'code':"No results Found!",'name':"No results Found!",'open':"No results Found!",'high':"No results Found!",'low':"No results Found!",'close':"No results Found!"})
    else:
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
    return render(request,'index.html',context)
