import tkinter as tk
import cv2
import pyautogui
import PIL
import socket
host = '192.168.43.139'
port = 9050
bufferSize = 999999
socket_client = None
addr = None
background = None

def CreateSocket():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind((host, port))
    sk.listen(10)
    return sk


def WriteSceen():
    data = socket_client.recv(bufferSize)
    img2 =  tk.PhotoImage(data=data)
    background.configure(image = img2)
    background.image = img2

def motion(event):
    data = 'mousemove,'+str(event.x)+','+str(event.y)
    socket_client.sendall(data.encode('utf-8'))
    WriteSceen()
def MouseEventCLick(event):
    data = 'mouseclick,'+str(event.num)+','+str(event.x)+','+str(event.y)
    socket_client.sendall(data.encode('utf-8'))
def onLeftDrag(event):
    data = 'mousedrag,'+str(event.x)+','+str(event.y)
    socket_client.sendall(data.encode('utf-8'))
    WriteSceen()
def onMouseWheel(event):
    data = 'mousewheel,'+str(event.delta)
    socket_client.sendall(data.encode('utf-8'))
    WriteSceen()
def KeyPress(event):
    data =  'keypress,'+str(event.char)+','+str(event.state)
    print(data)
    socket_client.sendall(data.encode('utf-8'))
    WriteSceen()
if __name__ == '__main__':
    sk = CreateSocket()
    print('lisening client connect ....')
    while True:
        try:
            socket_client,addr = sk.accept()
            print('client : {}'.format(addr)+' connected')
            data = socket_client.recv(bufferSize)
            # receivByte = base64.b64decode(data)
            root = tk.Tk()
            # event control
            #mouse move 
            root.bind('<Motion>', motion)
            #mouse click
            root.bind('<Button-1>', MouseEventCLick)
            root.bind('<Button-2>', MouseEventCLick)
            root.bind('<Button-3>', MouseEventCLick)
            root.bind('<Button-4>', MouseEventCLick)
            root.bind('<Button-5>', MouseEventCLick)

            #mouse drag
            root.bind('<B1-Motion>', onLeftDrag) 
            root.bind('<MouseWheel>', onMouseWheel) 
            #key event
            root.bind('<Key>', KeyPress)

            root.geometry("1920x1080")
            bg = tk.PhotoImage(data = data)
            background = tk.Label(root,image = bg)
            background.place(x=0, y=0)
            root.mainloop()
        except Exception as e:
            print(e)
        finally:
            socket_client.close()