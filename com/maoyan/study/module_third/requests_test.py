# requests
# get/post
# status_code/text/url/encoding/content/json()
# params/headers/data

import requests

# get
r1 = requests.get("https://www.baidu.com/")
print(r1.status_code)
print(r1.url)
print(r1.text)


r2 = requests.get("https://www.douban.com/search", params={'q': 'python', 'cat': '1001'})
print(r2.url)
print(r2.encoding)
print(r2.content)


# r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r3.json())

r4 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r4.text)


# post
r5 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r5.status_code)
