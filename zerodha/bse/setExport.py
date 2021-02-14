from datetime import datetime
import os

def setStatic():
    now=datetime.now()
    day=now.strftime("%d")
    month=now.strftime("%m")
    year=now.strftime("%y")
    if os.path.exists(f"/static/EQ{day}{month}{year}.CSV"):
            return f"EQ{day}{month}{year}.CSV"
    else:
            return [f for f in os.listdir('static') if f.endswith('.CSV')][0]
