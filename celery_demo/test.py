import requests
from bs4 import BeautifulSoup
import re


filename="index3200.html"

file_path='/tmp/'

file_path=file_path+filename

f=open(file_path,'a')
f.write('12345')
f.write('\n')


f.write('<img src="web" title="web" alt="web">') 
f.write('\n')

curl = "https://www.ptt.cc/bbs/Beauty/"+filename

r = requests.Session()

payload ={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}
r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)



response = r.get(curl)
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
      f.write('<img src="'+article.get('href')+'" title="web" alt="web">')
      f.write(article.get('href'))
      f.write('\n')
    
    articles = soup.findAll('a', {'href':re.compile('http')})
    for article in articles:
      print(article.get('href'))
      f.write('<img src="'+article.get('href')+'" title="web" alt="web">')
      f.write('\n')

