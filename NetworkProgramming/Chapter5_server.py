import socket
import select

s = socket.socket()
s.bind(('127.0.0.1', 8000))  # 服务器: http://127.0.0.1:8000
s.listen(5)
r_list = [s, ]
num = 0
while True:
    rl, wl, error = select.select(r_list, [], [], 10)  # r_list赋值给rl
    num += 1
    print('counts is %s' % num)
    print('rl=%s' % rl)
