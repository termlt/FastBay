import requests
from bs4 import BeautifulSoup

class fbay:

    def __init__(self, search):
        self.search = search

    #Title
    def title(self):
        r = requests.get(f'https://thepiratebay10.org/search/{self.search}')
        soup = BeautifulSoup(r.content, 'html.parser')

        title = soup.find('div', class_ = 'detName')

        return title.find('a')['title'].strip('Details for')


    #Download Link
    def link(self):
        r = requests.get(f'https://thepiratebay10.org/search/{self.search}')
        soup = BeautifulSoup(r.content, 'html.parser')

        link_main_class = soup.find('td', class_ = None)
        link = link_main_class.find('a', class_ = None)

        return link['href']


    #Information
    def info(self):
        r = requests.get(f'https://thepiratebay10.org/search/{self.search}')
        soup = BeautifulSoup(r.content, 'html.parser')

        information_class = soup.find('font', class_ = 'detDesc')
        get_text = information_class.get_text()

        return get_text.replace('ULed by ', 'ULed by')
