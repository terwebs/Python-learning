from bs4 import BeautifulSoup
from urllib2 import urlopen

my_address = "https://realpython.com/practice/dionysus.html"

html_page = urlopen(my_address)
html_text = html_page.read()

my_soup = BeautifulSoup(html_text)
