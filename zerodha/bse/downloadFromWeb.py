import requests
from datetime import datetime
import os

def requestWeb():
   # Current time
   now=datetime.now()
   day=now.strftime("%d")
   month=now.strftime("%m")
   year=now.strftime("%y")
   # BSE India Don't allow get requests without User-agent
   header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
   downloadURL=f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{day}{month}{year}_CSV.ZIP"
   response=requests.get(downloadURL,headers=header,stream=True)
   filename=downloadURL[downloadURL.rfind('/')+1:]

   # If there is a response then only it downloads otherwise returns None
   if response.ok:
	   if not os.path.exists(f'static/{filename}'):
	      with open(f"static/{filename}",'wb') as infile:
	 	      for chunk in response.iter_content(chunk_size=1200):
	 		       infile.write(chunk)
   else:
	   return "None"
   return filename