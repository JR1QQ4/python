#!/usr/bin/python
# -*- coding:utf-8 -*-
#
import requests, os, bs4
import urllib3
import time, pprint


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://www.iqiyi.com'
page_home = '/manhua/reader/18yzmrxmph_18yzho44rt.html'
current_url = url + page_home
selector = '.main-item img'
save_filename = 'cartoon'
next_button = "a[class='J_next_eposide_btn']"
os.makedirs(save_filename, exist_ok=True)
for i in range(2):
    # Download the page.
    print('Downloading page %s...' % current_url)
    res = requests.get(current_url, verify=False)
    res.raise_for_status()
    time.sleep(3)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    # Find the URL of the comic image.
    comicElems = soup.select(selector)
    if not comicElems:
        print('Could not find comic image.')
    else:
        # pprint.pprint(comicElems, indent=2)
        for comicElem in comicElems:
            comicUrl = comicElem.get('src') or comicElem.get('data-original')
            print(comicUrl)
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image
            imageFile = open(os.path.join(save_filename, os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select(next_button)[0]
    page_home = prevLink.get('href')
    current_url = url + page_home
print('Done.')
