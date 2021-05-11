import requests
from bs4 import BeautifulSoup

#________________________________________________

print('Script is written by: termit ( termlt - on GitHub ) \n')

search = input('Search: ')

r = requests.get(f'https://thepiratebay10.org/search/{search}')

soup = BeautifulSoup(r.content, 'html.parser')

try:
	title = soup.find('div', class_ = 'detName')
	links = soup.find('td', class_ = None)
	link = links.find('a', class_ = None)

	print('\nTitle: ' + title.find('a')['title'].strip('Details for'))
	print('\nLink for download: ' + link['href'])

except:
	print(f'No torrent was found for {search}.')	
