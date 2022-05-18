import wad.detection as wad

# 查看网站所用技术
wad.unicode_literals = 'utf-8'
det = wad.Detector()
url = input()
print(det.detect(url))

# %%

import whois

# 查看网站所有者信息
url = 'https://baidu.com'
data = whois.whois(url)
print(data)
