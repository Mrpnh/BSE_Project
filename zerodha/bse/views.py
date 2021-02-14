#  https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

from django.shortcuts import render,HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    now=datetime.now()
    day=now.strftime("%d")
    month=now.strftime("%m")
    year=now.strftime("%y")
    context={
        'filename': f"EQ{12}{month}{year}.csv"
    }
    return render(request,'index.html',context)