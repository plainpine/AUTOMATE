import json, requests, sys

# コマンドライン引数から地名を組み立てる
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    print('　　　　　　　　　　　　　　　　　　　　　location　Ex: San Francisco, CA, US')
    sys.exit()

location = ' '.join(sys.argv[1:])
#print(location)

API_key = '976a5b0293b0631c132824e893d4ec45'
response = requests .get(f'https://api.openweathermap.org/geo/1.0/direct?q={location}&appid={API_key}')
response.text
#print(response.text)

response_data = json.loads(response.text)
response_data
#print(response_data)

response_data[0]['lat'] # 緯度
#print(response_data[0]['lat'])
response_data[0]['lon'] # 経度
#print(response_data[0]['lon'])

lat = json.loads(response.text)[0]['lat']
lon = json.loads(response.text)[0]['lon']
response = requests .get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}')
response_data = json.loads(response.text)
response_data
#print(response_data)

# 天気予報の情報を表示する
w = response_data['list']  # ❶
print(f'{location}の現在の天気:')
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('明日:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('明後日:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
