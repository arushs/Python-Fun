from bs4 import BeautifulSoup
import urllib
file = urllib.urlopen("http://nytimes.com")

soup = BeautifulSoup(file)

# print(soup.prettify())
# print(soup.get_text())
for link in soup.find_all('a'):
	print(link.get('href'))
