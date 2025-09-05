# REPLで逐次実行

import requests

r = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(r)
r.status_code == requests.codes.ok
len(r.text)
print(r.text[:250])
