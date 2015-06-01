from __future__ import unicode_literals #all string literals will automatically be unicode characters
import requests
from bs4 import BeautifulSoup

url = "http://www.benjerry.com/flavors"
r = requests.get(url)
soup = BeautifulSoup(r.content)

divTags = soup.find_all('div',{"class": "ingredients"})
ingredients = []
for item in divTags:
	ingredients.append(item.contents[1].text)

hFourTags = soup.find_all("h4")
flavors = []
for item in flavors:
	hFourTags.append(item.text)

clean_list = []
for strings in flavors:
  clean_list.append(strings.replace("\u2122", " ").replace("\xae", " ").replace('\n', " "))

theGoods = dict(zip(flavors, ingredients))

print ingredients








	  
