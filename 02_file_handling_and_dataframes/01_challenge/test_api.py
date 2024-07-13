import requests

# 次のリンクにある "appid" プレースホルダーを自分のトークンに置き換えてください
url = "https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&appid=c72b9093a1a50d253b1b1ce5130148c4"
response = requests.get(url).json()
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")