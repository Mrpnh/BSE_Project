import redis
import csv
from datetime import datetime
import os

connection=redis.Redis()
keys=[]
def analyseCSV(filename):
    global keys
    keys.clear()
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
    return keys