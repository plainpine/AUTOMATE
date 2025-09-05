import requests, bs4
exampleFile = open('example.html')
example_soup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(example_soup)
print(type(example_soup))
