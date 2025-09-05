import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
print(spanElem)
spanElem.get('id')
print(spanElem.get('id'))
spanElem.get('some_nonexistent_addr') == None
print(spanElem.get('some_nonexistent_addr') == None)
spanElem.attrs
print(spanElem.attrs)
