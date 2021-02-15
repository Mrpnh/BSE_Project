from zipfile import ZipFile
import redis
import csv
from bse.downloadFromWeb import requestWeb
from datetime import datetime
import os

connection=redis.Redis()
keys=[]
def analyseCSV(filename):
    print(len(keys))
    now=datetime.now()
    day=now.strftime("%d")
    month=now.strftime("%m")
    year=now.strftime("%y")
    if filename!=f"EQ{day}{month}{year}_CSV.ZIP":
        with open(f"static/{filename}",'r') as infile:
            csvfile=csv.reader(infile,delimiter=",")
            execute=0
            connection.flushall()
            for row in csvfile:
                if execute<1:
                    execute+=1
                    continue
                name=row[1].strip().lower()
                connection.hset(name,'code',row[0])
                connection.hset(name,'name',name)
                connection.hset(name,'open',row[4])
                connection.hset(name,'high',row[5])
                connection.hset(name,'low',row[6])
                connection.hset(name,'close',row[7])
                keys.append(name)

    else:
        path_parent = os.path.dirname(os.getcwd())
        os.chdir("static/")
        with ZipFile(filename,'r') as zip:
            zip.extractall()
        os.remove(filename)
        os.chdir(path_parent)
        with open(f"static/EQ{day}{month}{year}.CSV",'r') as infile:
            csvfile=csv.reader(infile,delimiter=",")
            execute=0
            connection.flushall()
            for row in csvfile:
                if execute<1:
                    execute+=1
                    continue
                name=row[1].strip().lower()
                connection.hset(name,'code',row[0])
                connection.hset(name,'name',name)
                connection.hset(name,'open',row[4])
                connection.hset(name,'high',row[5])
                connection.hset(name,'low',row[6])
                connection.hset(name,'close',row[7])
                keys.append(name)       