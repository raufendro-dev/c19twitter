import urllib, json, requests
import tweepy
from datetime import datetime
import time
import threading

def func():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  url = "https://covid19.mathdro.id/api/countries/Indonesia/"
  response = urllib.request.urlopen(url)
  data = json.loads(response.read())
  konfirmasi=json.dumps(data['confirmed'])
  terkonfirmasi = json.loads(konfirmasi)
  a = str(terkonfirmasi['value'])
  mati = json.dumps(data['deaths'])
  meninggal = json.loads(mati)
  b = str(meninggal['value'])
  kalimat= str('Bot COVID-19 Info : ''Terkonfirmasi : '+a+', '+'Meninggal : '+b+', '+'Tanggal Update : '+data['lastUpdate'])
  print(kalimat)
  con_key='XL5WljIZOCXNYzOQlWGSkBU2w'
  con_sec='ZqzcYiXVDd9VVqVMoTXIoClh9kQl37R5T3f2M9deqkxPgfm9wQ'
  access_tok='1354031617086394368-fxgsEKbK7RqHO29U96bf8uZo3zivbP'
  access_toksec='7rCmqs1lU7KmRfybO9VfYZ2LIqRNQ3dVMb4zuoUYrlccw'
  auth = tweepy.OAuthHandler(con_key, con_sec)
  auth.set_access_token(access_tok, access_toksec)
  api = tweepy.API(auth)
  api.update_status(current_time+' '+kalimat)
  print("Tweet posted :)")

while True:
  t= time.time()
  th=threading.Thread(target=func, args=())
  th.start()
  th.join()
  t= time.time()-t
  time.sleep(300-t)
