
#parser

import os
os.chdir('C:\project\Lib\site-packages')
from bs4 import BeautifulSoup
import requests
page_link = 'http://readrate.com/rus/ratings/top100'
response = requests.get(page_link)
response
html = response.content
soup = BeautifulSoup(html, 'html.parser')
soup

#часть 1-я

divs = soup.findAll("div",{'class':'list-item'})
for div in divs:
	div_name = div.find('div',{'class':'title'})
	div_author = div.find('ul',{'class':'contributors-list list'})
	book = div_name.find('a').text
	author = div_author.find('a').text
	print('Название книги: ', book,'\n','Автор: ', author)

#часть 2-я

all_books = []
for div in divs:
	div_name = div.find('div',{'class':'title'})
	div_author = div.find('ul',{'class':'contributors-list list'})
	book = div_name.find('a').text
	author = div_author.find('a').text
	all_books.append([book, author])


def show(number):
	if number>100:
		print("Введи число, ушлепок")
	else:
		for i in range(number):
			print (all_books[i])
		return()

number = int(input())
result = show(number)
		











