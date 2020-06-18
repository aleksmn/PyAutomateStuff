import bs4
import requests


def getTopNews(url):
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # select by CSS path:  
    selection = soup.select('div.mainblock div.leftside div.newsmain a h3')
    
    return [i.text for i in selection]
     

url = 'https://www.interfax.ru/'


for i in getTopNews(url):
    print (i)

