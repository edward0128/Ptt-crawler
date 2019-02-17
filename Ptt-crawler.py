import requests
from bs4 import BeautifulSoup
import re



curl = "https://www.ptt.cc/bbs/Beauty/index2829.html"

r = requests.Session()

payload ={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}
# 回覆成人告警功能
r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)



response = r.get(curl)
soup = BeautifulSoup(response.text, 'lxml')
articles = soup.find_all('div', 'r-ent')


for article in articles:
    
    # 作者
    author = article.find('div','author').getText()
    # 推文數
    nrec = article.find('div','nrec').getText()
    # 文章開頭
    title = article.find('div','title').getText()
        
    # 當文章被刪除時,超連結會被移除,檢測超連結是否存在
    if len(article.find('div','title'))>1:        
        curl = article.find('div','title').find('a').get('href')    
    else:
        continue              
    
    
    r2 = requests.Session()
    r = r2.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)    
    curl = "https://www.ptt.cc" +curl;
    
    print(title,"作者: "+author,"推文數: "+nrec,curl)

    response = r2.get(curl)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.prettify()
    
    # 圖片連結
    articles = soup.findAll('a', {'href':re.compile('.jpg')})
    for article in articles:
      print(article.get('href'))
    
    # 網頁連結
    articles = soup.findAll('a', {'href':re.compile('http')})
    for article in articles:
      print(article.get('href'))