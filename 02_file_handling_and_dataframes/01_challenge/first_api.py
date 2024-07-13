import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
print(data[0])