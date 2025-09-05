import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(no_starch_soup)
print(type(no_starch_soup))
