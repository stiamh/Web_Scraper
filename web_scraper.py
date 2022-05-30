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
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup as bs
import traceback
import shutil

print("Enter the URL you want to scrape from:") 
websiteURL = input() 

req = requests.get(websiteURL)
soup = bs(req.content, 'html.parser')

print("Enter the tag you want to scrape:") # Lets you decide what data you would like to scrap based on the data's tag on the website. 
tag = input().lower()
tags = soup.findAll(tag)

illegalChars = ['\\','/', ':', '*', '"', '<', '>', '|'] # Windows does not allow these characters in file names. 

def illegal_chars_check(imageAlt):
    i = 0
    while i < len(illegalChars):
        if illegalChars[i] in imageAlt:
            imageAlt = imageAlt.replace(str(illegalChars[i]), ' -')
        i += 1
    return imageAlt
# if ':' in imageAlt:
#     imageAlt = imageAlt.replace(':', '-')
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

    x = 0 # Used for indexing pictures that do not have a title. 
    for image in tags:
        try:
            imageUrl = image['src']
            imageAlt = image['alt']
            imageAlt = illegal_chars_check(imageAlt)
            fullUrl = websiteURL + imageUrl
            source = requests.get(fullUrl, stream=True)
            print(source) # prints response code. 
            if source.status_code == 200:
                alt_test = image.find_all(image['alt'])
                print(alt_test)
                if alt_test != None:
                    with open(f'{imageAlt}' + '.jpg', 'wb') as f:
                        source.raw.decode_content = True
                        shutil.copyfileobj(source.raw, f)
                        print(imageAlt)
                else:
                    with open(f'{folder_name}-' + str(x) + '.jpg', 'wb') as f:
                        source.raw.decode_content = True
                        shutil.copyfileobj(source.raw, f)
                        x += 1
        except:
            traceback.print_exc()

if tag == 'img':
    image_scrape(tags)
else:
    text_scrape(tags)