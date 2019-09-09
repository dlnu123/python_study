# base64

import base64


print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print(base64.b64encode(b"abcd"))
# print(base64.b64encode())


# 课后习题
def safe_base64_decode(s):
    if len(s) % 4 != 0:
        s = s + b"="*(4 - len(s) % 4)
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
