import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome("C:\\Users\\user\\ChromeDriver\\chromedriver.exe",options=chrome_options)



address = 'https://www.dallaspetland.com/puppy-photo-gallery/'

driver.get(address)


images = []

SCROLL_PAUSE_TIME = 2


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")


while True :
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

    


#driver.execute_script("window.scrollBy(0, 1000000)")

time.sleep(1)

#images = driver.find_elements_by_tag_name('img')


'''
for image in images:
    print(image.get_attribute('src'))
    

'''

content = driver.page_source
soup = bs(content, 'html.parser')

image_tags = soup.findAll('img', attrs = {'class': "img-responsive center-block pet-info-img"})

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

driver.close()
