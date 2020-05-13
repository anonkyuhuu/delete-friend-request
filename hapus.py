class Delete:

	def __init__(self):
		self.url = 'https://mbasic.facebook.com'
		self.tot = []

	def start(self):
		sus = parser(req.get(f'{self.url}/friends/center/requests/',
			headers={'Cookie': self.kuki}).text, 'html.parser')
		for i in sus.find_all('a', string='Hapus Permintaan'):
			i = i['href']
			self.tot.append(i)
			ajg = req.get(self.url+i, headers={'Cookie': self.kuki})
		print(f'Request Canceled : {len(self.tot)}')
		if 'Lihat selengkapnya' in sus:
			gb = sus.find('a', string='Lihat selengkapnya').get('href')
			sd = req.get(f'{self.url}{gb}', headers={'Cookie': self.kuki}).text
		if len(self.tot) == 0:
			exit('No Friend Request Send')
		self.start()

	def main(self):
		self.kuki = input('Cookie : ')
		gz = parser(req.get(self.url, headers={'Cookie': self.kuki}).text, 'html.parser')
		if 'Masuk Facebook | Facebook' in gz.title or 'Facebook - Masuk atau Daftar' in gz.title:
			exit('Cookie Invalid')
		os.system('clear')
		print('''Author   : Anonk Yuhuu
Function : Delete Friends Request
Version  : 0.1
''')
		self.start()


import os
import requests as req
from bs4 import BeautifulSoup as parser
os.system('clear')
b = Delete()
b.main()
