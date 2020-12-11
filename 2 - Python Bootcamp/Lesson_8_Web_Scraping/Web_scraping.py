import requests
import lxml
import bs4


# We first ask for a request to thw website.
result = requests.get("http://exmaple.com")

# Once we get the requests, we get the requests object.
print(type(result))
print('')
print(result.text)
print('')
# We can get the web html text, then we separate the different types

print('Soup:\n')
sup = bs4.BeautifulSoup(result.text, 'lxml')
print(sup)
print('\n\n')

print(sup.select('p'))
print('')
print(sup.select('p')[0])
print('')
print(sup.select('p')[0].getText())


site_body = sup.select('h1')
print(site_body[0].getText())
print(type(site_body[0]))# It's a TAG
print('\n\n\n\n\n\n\n')



res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)
print('\n\n\n\n')
# We have checked that in the wikipedia article the all the "titles" of the content table have the toctext class
# Has we know a class in html starts with a dor.

titles = soup.select(".toctext")
print(titles)
# As we know, the elements inside os my title list are not really strings, they are TAG's

print(type(titles[0]))

titles = [titles[num].getText() for num in range(len(titles))]
print(titles)
print('\n')

# another way to do it;

first_item = soup.select('.toctext')[0]
print(first_item.text) # attrbute

for item in soup.select('.toctext'):
    print(item.text)
print('\n\n\n')

##########################
# IMAGES
#########################

petition_3 = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
sup_3 = bs4.BeautifulSoup(petition_3.text, 'lxml')


# We use it to select all the images on the page
images = sup_3.select('img')
print(images)
print('')
for link in images:
    print(link)
print('\n\n')

# If we want to select the images inside the page;

image_inside = sup_3.select('.thumbimage')
print('List of images URL', image_inside)
print('')
for link in image_inside:
    print(link)
print('\n')

computer = image_inside[0]
print(computer['src'])
print('')

link_image = requests.get('https:'+computer['src'])
print(link_image.content)

f = open('my_computer_image.jpg', 'wb')  # Usually the extension (.jpg) it had to mach with the image extension.
# 'wb' it's write binary
f.write(link_image.content)
f.close()



