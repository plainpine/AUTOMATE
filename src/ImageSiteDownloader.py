import re, requests, threading, os
from bs4 import BeautifulSoup

def download_image(url):
    with open(os.path.basename(url), "wb") as f:
        f.write(requests.get(url).content)
    print(url, "download successfully")

original_url = "https://www.flickr.com/search/?text=sea&view_all=1&page={}"

pages = range(1, 5000) # not sure how many pages here

for page in pages:
    concat_url = original_url.format(page)
    print("Now it is page", page)
    soup = BeautifulSoup(requests.get(concat_url).content, "html.parser")
    soup_list = soup.select(".photo-list-photo-view")
    #print(soup_list)
    for element in soup_list:
        #print(element)
        img_tag = element.find("img")
        #print(img_tag)
        img_url = ""
        if img_tag and img_tag.has_attr('src'):
            img_url = img_tag['src']
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            print(img_url)
        else:
            continue

        threading.Thread(target=download_image, args=(img_url,)).start()
