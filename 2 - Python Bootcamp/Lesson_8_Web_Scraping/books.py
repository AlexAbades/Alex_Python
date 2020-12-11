import requests
import bs4
import time

print('http://books.toscrape.com/catalogue/category/books_1/index.html')
print('http://books.toscrape.com/catalogue/category/books_1/page-2.html')

base_url = "http://books.toscrape.com/catalogue/category/books_1/page-{}.html"

page_number = 12
print(base_url.format(page_number))

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
b=soup.select(".product_pod")
print(len(b))


print(len(soup.select(".product_pod")))
# It has sence, because every page has twenty products
print('\n\n')

print('Analyzing the code:\n')
first_book = soup.select(".product_pod")[0]
print(first_book)
print("\n\n")
# We can convert the text into a python string and check if a the string "star-rating Two it's in the string or not
print(first_book.select(".star-rating.Three"))
# If there s an space in the class, you have to fill it with a dot

# we can chack it with:
print([] == first_book.select(".star-rating.Two"))
print("\n\n\n")

print('Searching for the title:\n')
print(first_book.select('a')[1]['title'])
print('\n\n\n\n')



# We compile everything here
start_time = time.time()
two_star_title = []

for page in range(1,51):
    res = requests.get(base_url.format(page))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if book.select('.star-rating.Two'):
            two_star_title.append(book.select('a')[1]['title'])
        else:
            pass


end_time = time.time()
elapsed_time = end_time-start_time
print('Time to run the for loop: ', elapsed_time)


print(len(two_star_title))
print(two_star_title)

