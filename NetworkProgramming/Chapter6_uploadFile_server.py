import socket, os, time

server = socket.socket()
server.bind(('localhost', 8080))
server.listen()
while True:
    conn, addr = server.accept()
    print('连接到客户端')
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print('客户端已断开')
                break
        except Exception as e:
            print('客户端已断开')
            break
        cmd, filename = data.decode().split()
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            # 获取文件的字节大小
            size = os.stat(filename).st_size
            conn.send(str(size).encode())  # 发送文件大小
            conn.recv(1024)
            for line in f:  # 客户端确认后发送文件内容
                conn.send(line)
            f.close()
            print('文件下载完毕')
        conn.send('not file'.encode())
    server.close()
