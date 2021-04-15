#server.py

import socket

# Định nghĩa host và port mà server sẽ chạy và lắng nghe
host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1) # 1 ở đây có nghĩa chỉ chấp nhận 1 kết nối
print("Server listening on port", port)
while True:
    try:
        c, addr = s.accept()
        print("Connect from ", str(addr))
        msg = c.recv(1024).decode()
        print('Out put : ',msg)
        #server sử dụng kết nối gửi dữ liệu tới client dưới dạng binary
        msg = input('Input :')
        c.send(msg.encode())
        c.send("Bye".encode())
    finally:
        c.close()