import requests
import bs4
import time

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)
print('\n\n\n')


authors = set()
# to don't worry about the repeat it authors

for author in soup.select('.author'):
    authors.add(author.text)
print('Authors: ')
print(authors)
print('\n\n')


quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)

print('Quotes: ')
print(quotes)
print(len(quotes))
print("\n")

print('Tags: ')
tags = []
for tag in soup.select('.tag-item'):
    tags.append(tag.text)
print(tags)
print(len(tags))

res = requests.get("http://quotes.toscrape.com/page/{}/")

base_url = "http://quotes.toscrape.com/page/{}/"
res = requests.get(base_url.format(9))
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.select('.next'))


authors = set()
quotes = []
tags = set()


for n in range(1,400):
    res = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    for author in soup.select('.author'):
        authors.add(author.text)

    for quote in soup.select('.text'):
        quotes.append(quote.text)

    for tag in soup.select('.tag-item'):
        tags.add(tag.text)

    print('I am in the page: ', base_url.format(n))
    if soup.select('.next'):
        continue
    else:
        break

print(authors)
print(len(authors))
print('')
print(quotes)
print(len(quotes))
print('')
print(tags)
print(len(tags))
print('\n\n\n')




authors = set()
quotes = []
tags = set()


# Try it with a while loop

