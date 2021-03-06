
"""
dla podanego url sciaga tresc artykulu i zapisuje do obiektu Article
"""
def BankierText(url):
    import urllib.request as uLib
    from bs4 import BeautifulSoup
    from dataModel.Document import Document
    
    page = uLib.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')


    article_content = soup.find('div', {'id':'articleContent'})
    article_text = []
    for paragraph in article_content.find_all('p'):
        if not paragraph.text.strip() == "":
            article_text.append(paragraph.text.strip())
    
    date = soup.find('time', {'class','entry-date'}).text
    title_txt = soup.title.text.strip()

    article = Document()
    article.title = title_txt
    article.text = article_text  
    article.date = date
    article.source = url
    return article

"""
dla Bankiera przechodzi przez podaną liczbę stron
i pobiera artykuły
"""
""" BankierNewsCrawler"""
def BankierNewsCrawler(site_start=1, last_site=1):
    import urllib.request as uLib
    import csv
    from datetime import datetime as dt
    from bs4 import BeautifulSoup
    from dataModel.Document import Document
    from crawlers.BankierExtraction import BankierText
    from databaseHelpers.SqliteHelper import SqliteHelper

    #parametry które będa wejsciowe do funkcji

    BaseURL = 'https://www.bankier.pl'
    BankierNewsURL = 'https://www.bankier.pl/wiadomosc/'
    articles = []

    for i in range(site_start, last_site):
        page = uLib.urlopen(BankierNewsURL + str(i))
        soup = BeautifulSoup(page, 'lxml')

        links = []
        containers = soup.find_all('div', {'class':'article'})
        for container in containers:
            links.append(BaseURL + container.find('a', href = True)['href'])

        for link in links:
            art = BankierText(link) 
            articles.append(art) 

    with open('Bankier Articles sites ' +str(site_start) + '-' + str(last_site) + ' ' \
            + dt.now().strftime("%Y-%m-%d %H-%M-%S") + '.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=';')

        for article in articles:
            for paragraph in article.text:
                csv_writer.writerow([article.title, article.date, article.source, paragraph])
