import requests
from bs4 import BeautifulSoup 
from urllib import *
from urllib.parse import urljoin
visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)

    except:
        print(f"request error {url}")
        return
    
    if response .status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        #  grab all a tags 
        a_tag = soup.find_all('a')
        urls = []
    
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                # add the hrefs in my empty list
                urls.append(href)
        
        print(urls)

#  https://www.yahoo.com

url = input('enter the url you want to scrape: ')
keyword = input('enter the keyword to search in the url provided: ')


spider_urls(url, keyword)

for urls2 in url:
    if urls2  not in visited_urls:
        visited_urls.add(urls2)
        url_join = urljoin(url, urls2)
        if keyword in url_join:
            print(url_join)
            spider_urls(url_join, keyword)
    else:
        pass        
