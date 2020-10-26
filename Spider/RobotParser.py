import urllib.robotparser as urobot
import requests

url = "https://www.taobao.com/"
rp = urobot.RobotFileParser()
rp.set_url(url + "/robots.txt")
rp.read()
user_agent = 'Baiduspider'
if rp.can_fetch(user_agent, 'https://www.taobao.com/product/'):
    site = requests.get(url)
    print('seems good')
else:
    print('cannot scrap because robots.txt banned you!')
