import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    try:
        msg = input('>>>')
        if msg == 0:  # 判断输入是否为空，或是直接按下回车键
            continue
        else:
            c.sendto(msg.encode('utf-8'), ('127.0.0.1', 25555))
        data, s_addr = c.recvfrom(1024)
        print('$: %s' % (data.decode('utf-8')))
    except KeyboardInterrupt:
        break
c.close()
