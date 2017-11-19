import urllib.request as uLib
import csv
from datetime import datetime as dt
from bs4 import BeautifulSoup
from dataModel.Document import Document
from crawlers.BankierExtraction import BankierText
from databaseHelpers.SqliteHelper import SqliteHelper

#parametry które będa wejsciowe do funkcji
firstPage = 1
lastPage = 4

BaseURL = 'https://www.bankier.pl'
BankierNewsURL = 'https://www.bankier.pl/wiadomosc/'
articles = []

for i in range(firstPage, lastPage):
    page = uLib.urlopen(BankierNewsURL + str(i))
    soup = BeautifulSoup(page, 'lxml')

    links = []
    containers = soup.find_all('div', {'class':'article'})
    for container in containers:
        links.append(BaseURL + container.find('a', href = True)['href'])

    for link in links:
        art = BankierText(link) 
        articles.append(art) 

with open('BannkierArticles' + dt.now().strftime("%Y%m%d-%H%M%S") + '.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file, delimiter=';')

    for article in articles:
        for paragraph in article.Text:
            csv_writer.writerow([article.Title, article.Date, paragraph])

