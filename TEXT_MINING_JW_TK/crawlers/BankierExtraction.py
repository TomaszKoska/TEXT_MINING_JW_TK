
"""
dla podanego url sciaga tresc artykulu i zapisuje do obiektu Article
"""
def BankierText(url):
    import urllib.request as uLib
    from bs4 import BeautifulSoup
    from dataModel.ArticleClass import ArticleClass
    
    page = uLib.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')

    article_txt = soup.find('div', {'id':'articleContent'})
    outcome = article_txt.text.strip()
    
    title_txt = soup.title.text.strip()
    article = ArticleClass()
    article.Title = title_txt
    article.Text = outcome  
    return article

"""
dla podanej podstrony Bankiera przechodzi przez podaną liczbę stron
i pobiera artykuły
"""
""" BankierWebCrawler"""
def BankierWebCrawler(url, site_start, sites_amount):
    import urllib.request as uLib
    from bs4 import BeautifulSoup