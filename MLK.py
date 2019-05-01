import bs4 as bs
from urllib.request import Request, urlopen
import re

#s1 = urllib.request.urlopen('https://www.keepinspiring.me/martin-luther-king-jr-quotes/').read()

req = Request('http://wisdomquotes.com/martin-luther-king-jr-quotes/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = bs.BeautifulSoup(webpage,'lxml')
quote=""
quotes=[]
for div in soup.find_all('blockquote'):
	quotes.append(div.get_text())

quotes1=[]
for quote in quotes:
	quote = [re.sub(r"Part\s\S\.\s?", r"", str(quote))]
	quotes1.append(quote)
	#quotes1.append("\n")
#print(quotes1)



      
	
for quote1 in quotes1:
	quote1=str(quote1)
	k = quote1.rfind(".")
	quote2=quote1[2:k]+"."
	print(quote2)




