'''
NOTE: SOMETIMES YOU NEED TO PROVIDE THE WHOLE NAME OF A TORRENT.
WRONG: charlie and the choco
RIGHT: charlie and the chocolate factory
'''


import requests
from bs4 import BeautifulSoup

class fb:

	def __init__(self, search):
		self.search = search

	def main(self):
		r = requests.get(f'https://thepiratebay10.org/search/{self.search}')

		soup = BeautifulSoup(r.content, 'html.parser')

		try:
			#Title
			title = soup.find('div', class_ = 'detName')

			#Link for the download

			#Getting the class where the <a href> is
			link_main_class = soup.find('td', class_ = None)
			#Finding <a href>
			link = link_main_class.find('a', class_ = None)

			#Info about the torrent file

			#Getting the class where the information about the file is
			information_class = soup.find('font', class_ = 'detDesc')
			#Getting the text from information_class
			get_text = information_class.get_text()
			#Removing word Uploaded from the text
			strip_uploaded = get_text.strip('Uploaded')
			#Replace , ULed by   with   Uploader:
			replace_uled = strip_uploaded.replace(', ULed by', ',  Uploader:')

			information = replace_uled.replace('Size', ' Size: ')

			#Category
			#category = soup.find('center')


			print('\nTitle: ' + title.find('a')['title'].strip('Details for'))

			print(f'\nInformation about the torrent \nUploaded: {information}')

			#print('\nCategory: ' + details.get_text())

			print('\nLink for a download: ' + link['href'])

		except:
			print(f'\nNo torrent was found for {self.search}')
