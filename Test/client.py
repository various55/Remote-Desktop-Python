#client .py

import socket

# Như mình đã nói ở trên thì chúng ta không truyền tham số vào vẫn ok

# 1024 là số bytes mà client có thể nhận được trong 1 lần
# Phần tin nhắn đầu tiên

# Phần tin nhắn tiếp theo
while True:
  try:
    s = socket.socket()
    s.connect(("localhost", 4000))
    data = input('Input : ')
    s.send(data.encode())
    msg = s.recv(1024)
    print("Recvied ", msg.decode())
    msg = s.recv(1024)
  finally:
    s.close()