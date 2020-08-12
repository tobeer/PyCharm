import socket

client = socket.socket()
client.connect(('localhost', 8080))
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode())  # 发送请求
    server_response = client.recv(1024)
    if server_response.decode().startswith('not'):
        print('请输入有效文件名')
        continue
    client.send(b"ready to recv file")  # 发送确认
    file_size = int(server_response.decode())
    recv_size = 0
    filename = cmd.split()[1]
    f = open(filename + '.new', 'wb')
    while recv_size < file_size:
        if file_size - recv_size > 1024:
            size = 1024
        else:
            size = file_size - recv_size
            print('last receive:', size)
        recv_data = client.recv(size)
        recv_size += len(recv_data)
        f.write(recv_data)
    else:
        print('文件下载完成')
        f.close()
client.close()
