import time  
from celery_app import app  
import redis
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re
  
@app.task  
def add(x, y):  
    #time.sleep(2)
    r = redis.Redis()
    data =r.get("curl")
    
    print (data)
    #if int(data) > 2010:
    # return 0

    data=int(data)+1;
    r.mset({"curl": data})




    filename="index"+str(data)+".html"
    file_path='/home/picture/'
    file_path=file_path+filename
   
    print(file_path)
    
    f=open(file_path,'a')
   
    curl = "https://www.ptt.cc/bbs/Beauty/"+filename

    r = requests.Session()

    payload ={
        "from":"/bbs/Gossiping/index.html",
        "yes":"yes"
    }
    r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)



    response = r.get(curl)
    print(response)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('div', 'r-ent')


    for article in articles:

        author = article.find('div','author').getText()
        nrec = article.find('div','nrec').getText()
        title = article.find('div','title').getText()

        if len(article.find('div','title'))>1:
            curl = article.find('div','title').find('a').get('href')
        else:
            continue


        r2 = requests.Session()
        r = r2.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)
        curl = "https://www.ptt.cc" +curl;

        print(title,"author: "+author,"nrec: "+nrec,curl)

        response = r2.get(curl)
        soup = BeautifulSoup(response.text, 'lxml')
        soup.prettify()

        articles = soup.findAll('a', {'href':re.compile('.jpg')})
        for article in articles:
          print(article.get('href'))
          f.write('\n')
          f.write('<img src="'+article.get('href')+'" title="web" alt="web">')
          f.write('\n')

        articles = soup.findAll('a', {'href':re.compile('http')})
        for article in articles:
          print(article.get('href'))
          #f.write('\n')
          #f.write('<img src="'+article.get('href')+'" title="web" alt="web">')
          #f.write('\n')
    return 1234
