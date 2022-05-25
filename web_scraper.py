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

print("Enter the URL you want to scrape from:") 
url = input() 

page = requests.get(url)
soup = bs(page.text, 'html.parser')

print("Enter the tag you want to scrape:") # Lets you decide what data you would like to scrap based on the data's tag on the website. 
tag = input().lower()
tags = soup.findAll(tag)

print(tags)

def text_scrape(tags):
    print("What would you like the file name to be called:")
    file_name = input()

def image_scrape(tags):
    print("What would you like the folder to be called:")
    folder_name = input()
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.chdir(folder_name)

    for image in tags:
        x = 0
        try:
            url = image.get('src')
            source = requests.get(url)
            if source.status_code == 200:
                with open(f'{folder_name}-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    f.close
                    x += 1
        except:
            pass 

if tag == 'img':
    image_scrape(tags)
else:
    text_scrape(tags)