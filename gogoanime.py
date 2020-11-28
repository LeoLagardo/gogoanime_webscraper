from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
url = 'https://gogoanime.so/category/bokura-wa-minna-kawaisou'
prefix_link = 'https://gogoanime.so'
browser.get(url)
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, features='html.parser')
episodes = soup.findAll('ul', attrs={'id': 'episode_related'})

page1 = []
for ep in episodes:
    for a in ep.findAll('a'):
        page1.append(prefix_link + a.get('href')[1:])

page2 = []
try:
    for link in page1:
        browser.get(link)
        time.sleep(3)
        dp = browser.page_source
        soup = BeautifulSoup(dp, features='html.parser')
        dlink = soup.findAll('li', attrs={'class': 'dowloads'})
        for li in dlink:
            for a in li.findAll('a'):
                page2.append(a.get('href'))
    
    for link in page2:
        browser.get(link)
        time.sleep(2)
        dp = browser.page_source
        soup = BeautifulSoup(dp, features='html.parser')
        dlink = soup.findAll('div', attrs={'class': 'dowload'})
        for a in dlink[3].findAll('a'):
            print(a.get('href'))
except:
    print('err')

finally:
    browser.close()
    browser.quit()