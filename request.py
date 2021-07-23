import requests

url = 'http://localhost:5000/recomend'
r = requests.post(url,json={'movie':'Hungama'})

print(r.json())