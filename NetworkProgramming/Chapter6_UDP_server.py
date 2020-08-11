import socket  # 导入socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.AF_INET表示IPV4,socket.SOCK_DGRAM表示UDP
s.bind(('', 25555))  # ''表示任意地址
print('[+] Server Open.....')
while True:
    try:
        data, c_addr = s.recvfrom(1024)  # UDP不需要构成连接，直接接收1024bytes的数据
        print('from:', c_addr)  # 发送信息的客户端的IP和端口的二元组
        print('say: %s' % (data.decode('utf-8')))
        reply = "I'm fine, and you?"
        s.sendto(reply.encode('utf-8'), c_addr)
    except KeyboardInterrupt:
        break
print('[+] Server Close.....')
s.close()
