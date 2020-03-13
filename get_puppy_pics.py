import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://unsplash.com/s/photos/dogs'

page = requests.get(url)
print (page)
soup = bs(page.text, 'html.parser')
image_tags = soup.findAll('img')

if not os.path.exists('Puppies'):
    os.makedirs('Puppies')

os.chdir('Puppies')

x = 0

for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('puppy-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                print (x)
                x += 1
                

    except:
        pass
