# urllib
# Get
# Post
# Handler

from urllib import request
from urllib import parse
import json


# Get
with request.urlopen("https://www.baidu.com") as f:
    data = f.read()
    print("Status:", f.status, f.reason)
    for key, value in f.getheaders():
        print("%s: %s" % (key, value))
    print("Data:", data)


print()
print("------------------------------------------------------------------------")
print()

# 模拟浏览器发送Get请求
req = request.Request("http://www.douban.com/")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# Post
print()
print("------------------------------------------------------------------------")
print()

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# Handler


# 课后习题
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        data_s = data.decode("utf-8")
        return json.loads(data_s)


# 测试
URL = 'https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
