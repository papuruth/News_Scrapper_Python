import urllib2
from bs4 import BeautifulSoup
import os, codecs
import unicodecsv as csv


site = 'https://www.hindustantimes.com/'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers = hdr)
try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

soup = BeautifulSoup(page, 'html.parser')

headlines_list = soup.find_all(['h1', 'h3'])

index = 1
news_list = []
urls_list = []
for headline in headlines_list:
	#headline_link = headline.find('a')
	#print headline_link
	url = headline.parent.get('href')
	if not url:
		url = headline.find('a').get('href')
	headline = headline.text.strip()
	news_list.append(headline)
	urls_list.append(site + url)
	index += 1

#CSV Creation
try:
    f = csv.writer(open('news.csv', 'w'))
    f.writerow(['Headlines','Link'])
    #print(article)
    for i, headline in enumerate(news_list):
        Headline = headline
        Url=urls_list[i]
        f.writerow([Headline, Url])
except Exception as e: print(e)
