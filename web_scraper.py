# WARNING: the code that follows will make you cry; a safety pig is provided below for your benefit.
#
#                          _
#  _._ _..._ .-',     _.._(`))
# '-. `     '  /-._.-'    ',/
#    )         \            '.
#   / _    _    |             \
#  |  a    a    /              |
#  \   .-.                     ;
#   '-('' ).-'       ,'       ;
#      '-;           |      .'
#         \           \    /
#         | 7  .__  _.-\   \
#         | |  |  ``/  /`  /
#        /,_|  |   /,_/   /
#           /,_/      '`-'
import os
import requests
from bs4 import BeautifulSoup as bs
import traceback

print("Enter the URL you want to scrape from:") 
websiteURL = input() 

req = requests.get(websiteURL)
soup = bs(req.content, 'html.parser')

print("Enter the tag you want to scrape:") # Lets you decide what data you would like to scrap based on the data's tag on the website. 
tag = input().lower()
tags = soup.findAll(tag)

print(tags)

def text_scrape(tags):
    print("What would you like the file name to be called:")
    file_name = input()
    file = open(f'{file_name}.txt', 'w')
    print("What data tag would you like to scrape:")
    data = input()
    for attribute in tags:
        source = requests.get(url)
        if source.status_code == 200:
            try:
                url = attribute.attrs(data)
                attribute = str(attribute)
                print(attribute)
                file.write(attribute)
            except:
                traceback.print_exc() 

def image_scrape(tags):
    print("What would you like the folder to be called:")
    folder_name = input()
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.chdir(folder_name)

    x = 0
    for image in tags:
        try:
            imageUrl = image['src']
            print(image['src']) # Test to see output.
            source = requests.get(websiteURL, imageUrl)
            print(source) # prints response code. 
            if source.status_code == 200:
                with open(f'{folder_name}-' + str(x) + '.jpg', 'wb') as f:
                    f.write(source.content)
                    x += 1
        except:
            traceback.print_exc()

if tag == 'img':
    image_scrape(tags)
else:
    text_scrape(tags)