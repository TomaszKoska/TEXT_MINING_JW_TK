import urllib.request as uLib
import csv
from datetime import datetime as dt
from bs4 import BeautifulSoup
from dataModel.Document import Document
from crawlers.BankierExtraction import BankierText
from databaseHelpers.CsvHelper import CsvHelper
from databaseHelpers.SqliteHelper import SqliteHelper

#parametry które będa wejsciowe do funkcji
firstPage = 1
lastPage = 1

BaseURL = 'https://www.bankier.pl'
BankierNewsURL = 'https://www.bankier.pl/wiadomosc/'
articles = []

for i in range(firstPage, lastPage+1):
    page = uLib.urlopen(BankierNewsURL + str(i))
    soup = BeautifulSoup(page, 'lxml')

    links = []
    containers = soup.find_all('div', {'class':'article'})
    for container in containers:
        links.append(BaseURL + container.find('a', href = True)['href'])

    for link in links:
        art = BankierText(link) 
        articles.append(art) 


    myHelper = CsvHelper(databesePath="D:/databases/csv/",delimiter=",")
    #myHelper = SqliteHelper(databesePath="D:/databases/bazka1.db")


    myHelper.start()
    for article in articles:
        #for paragraph in article.Text:
        myHelper.saveDocument(tableName="pozdro",document=article)

    myHelper.close()          


