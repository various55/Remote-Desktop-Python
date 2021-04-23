from PIL import ImageGrab
import pyautogui as pg
import socket
import io
host = '127.0.0.1'
port = 9091

def send_Img(socket):
    print('Send')
    img = ImageGrab.grab()
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    socket.send(img_bytes.getvalue())
if __name__ == '__main__':
    isFirst = True
    client_socket = socket.socket()
    client_socket.connect((host, port))

    while True:
        try:
            if(isFirst) :
                send_Img(client_socket)
                isFirst = False
            data = client_socket.recv(1024).decode()
            data = data.split()
            if data[0] == '1':
                x = int(data[1])
                y = int(data[2])
                pg.click(x, y,button='left')
            elif data[0] == '3':
                x = int(data[1])
                y = int(data[2])
                pg.click(x,y,button='right')
            elif data[0] == 'Scroll':
                delta =  int(data[1])
                pg.scroll(delta)
            elif data[0] == 'del':
                pg.typewrite(['backspace'])
            elif data[0] == 'Key':
                msg = data[1]
                if(msg == 'enter'):
                    pg.press('enter')
                elif (msg == 'space'):
                    pg.press('space')
                    #test alo
                else:
                    pg.typewrite(msg)
            else:
                x = int(data[0])
                y = int(data[1])
                pg.moveTo(x, y)  # show in terminal
                print('Move ',x,y)
        except:
            pass
        finally:
            send_Img(client_socket)

