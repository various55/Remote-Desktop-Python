from PIL import ImageGrab
import pyautogui as pg
import socket
import io

host = '127.0.0.1'
port = 9091
filename= "screenshot.png"

def send_Img(socket):
    print('Send')
    img = ImageGrab.grab()
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    socket.send(img_bytes.getvalue())
if __name__ == '__main__':
    isFirst = True
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the

    while True:
        try:
            if (isFirst):
                send_Img(client_socket)
                # open image
                # myfile = open(filename, 'rb')
                # bytes = myfile.read()
                # size = len(bytes)
                # send image size to server
                # client_socket.sendall(("SIZE %s" % size).encode('utf-8'))
                # answer = client_socket.recv(1024)
                # print(answer)
                isFirst = False
            data = client_socket.recv(1024).decode()  # receive response
            event = data.split()
            if event[0] == 'LClick':
                x = int(data.split(' ')[1])
                y = int(data.split(' ')[2])
                pg.click(x, y,button='left')
                isFirst = True
            elif event[0] == 'del':
                pg.typewrite(['backspace'])
                isFirst = True
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
                isFirst = True
            elif event[0] =='RClick':
                x = int(data.split(' ')[1])
                y = int(data.split(' ')[2])
                pg.click(x,y,button='right')
                isFirst = True
            elif event[0] =='dclick':
                pg.click(clicks=2)
                isFirst = True
            elif event[0] =='nl':
                pg.typewrite(['enter'])
                isFirst = True
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)  # show in terminal
                isFirst = False
        except:
            pass
