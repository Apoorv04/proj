import bs4 as bs
from urllib.request import Request, urlopen
import re

#s1 = urllib.request.urlopen('https://www.keepinspiring.me/martin-luther-king-jr-quotes/').read()

req = Request('https://www.keepinspiring.me/martin-luther-king-jr-quotes/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = bs.BeautifulSoup(webpage,'lxml')

quotes=[]
for div in soup.find_all('div',class_='author-quotes'):
	quotes.append(div.get_text())
#print(type(quotes))
quote = ""

for quote in quotes:
	quote=quote[1:-1]
	q1=re.findall(r"(.*)", quote)
	print('\n\n\n'.join(q1))
#print(len(quote))
