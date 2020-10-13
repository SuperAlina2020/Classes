import requests

response = requests.get('https://api.github.com/events')
print(response.json())
r = requests.post('https://httpbin.org/post',data = {'key':'value'})
print(r.json())
