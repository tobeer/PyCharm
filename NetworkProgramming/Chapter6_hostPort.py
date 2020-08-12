import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1', 8080))
if 10061 == result:
    print('Port is open')
    print('主机名：' + socket.gethostname())
else:
    print('Port is not open, return code: %s' % result)
