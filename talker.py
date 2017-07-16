import requests

r = requests.get('http://localhost:5000/posts')
print(r.status_code)
