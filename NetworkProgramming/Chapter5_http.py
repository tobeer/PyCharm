import http.cookiejar
import urllib.request

filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)  # 创建CookieJar对象
# 使用HTTPCookieProcessor创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
openner = urllib.request.build_opener(handler)  # 创建openner对象
# 向http://www.baidu.com发送请求
request = urllib.request.Request('http://www.baidu.com')
response = openner.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)
# 读取cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
openner = urllib.request.build_opener(handler)
response = openner.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

text = '天气真好'
bytetext = text.encode()  # 对text进行编码
print(bytetext)
print(bytetext.decode())  # 对bytetext进行解码

u = '字符串'
str = u.encode('utf-8')  # 以utf-8对u进行编码
print(str)
print(str.decode('utf-8'))  # 以utf-8对u进行解码

