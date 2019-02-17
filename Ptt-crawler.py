import requests
from bs4 import BeautifulSoup
import re

r = requests.Session()
payload ={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}
r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)



response = r.get("https://www.ptt.cc/bbs/Beauty/index2829.html")
soup = BeautifulSoup(response.text, 'lxml')
articles = soup.find_all('div', 'r-ent')


for article in articles:
    
    author = article.find('div','author').getText()
    nrec = article.find('div','nrec').getText()
    title = article.find('div','title').getText()
    
    curl = ""
    #curl = article.find('div','title').find('a').get('href')
    
    
    if len(article.find('div','title'))>1:        
        curl = article.find('div','title').find('a').get('href')    
    else:
        continue              
    
    
    
    
    r2 = requests.Session()
    r = r2.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)
    
    curl = "https://www.ptt.cc" +curl;
    print(title,author,nrec,curl)

    response = r2.get(curl)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.prettify()
    articles = soup.findAll('a', {'href':re.compile('.jpg')})
    for article in articles:
      print(article.get('href'))
