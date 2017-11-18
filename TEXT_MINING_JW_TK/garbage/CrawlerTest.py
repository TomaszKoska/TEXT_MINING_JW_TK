
import urllib.request as uLib
from bs4 import BeautifulSoup
from dataModel.ArticleClass import ArticleClass
from crawlers.BankierExtraction import BankierText

#dfhkjhsd
#parametry które będa wejsciowe do funkcji
firstPage = 1
lastPage = 4

#from importlib import reload
#reload(ProjectClasses)

BaseURL = 'https://www.bankier.pl'
BankierNewsURL = 'https://www.bankier.pl/wiadomosc/'

page = uLib.urlopen(BankierNewsURL)
soup = BeautifulSoup(page, 'lxml')

links = []
dates = []
containers = soup.find_all('div', {'class':'article'})
for container in containers:
    links.append(BaseURL + container.find('a', href = True)['href'])
    dates.append(container.find('time', {'class':'entry-date'}).text)

links = zip(links, dates)
#list(links)
##list(links)[0]
print(list(links)[1][1])
#print("\n".join(dates))

Articles = []
for link in links:
    print("co my tu mamy?", link)
    art = BankierText(link[0])
    art.Date = link[1] 
    Articles.append(art)
    print("a pod nim artykuł: ", art.Title)

