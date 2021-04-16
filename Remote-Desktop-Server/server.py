from win32api import GetSystemMetrics
import socket # For network connections
from tkinter import  *
import tkinter as tk # To create a graphical user interface
from PIL import Image

host = '127.0.0.2'
port = 9091
fileName = 'screenshot.png'
label = None
def getImage():
    img_bytes = conn.recv(9999999)
    print('Image form client')
    #data = conn.recv(1024)
    # myFile = open(fileName, 'wb')
    # if not img_bytes:
    #    myFile.close()
    # myFile.write(img_bytes)
    # myFile.close()
    bg = PhotoImage(data=img_bytes)
    label.configure(image=bg)
    label.image = bg
    # set image


def motion(event):
    x, y = event.x, event.y
    data = str(x*2)+' '+str(y*2)
    conn.send(data.encode())
    getImage()

def leftClick(event):
    x, y = event.x, event.y
    data = 'LClick '+str(x * 2) + ' ' + str(y * 2)
    conn.send(data.encode())
def rightClick(event):
    print('Right Click')
    x, y = event.x, event.y
    data = 'RClick '+str(x * 2) + ' ' + str(y * 2)
    conn.send(data.encode())

if __name__ == '__main__':

    global x, y, data
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)
    print('Waiting ......')
    while True:
        try:
            conn, address = server_socket.accept()
            print("Connection from: " + str(address))
            root = tk.Tk()
            # title
            root.title('Python Remote Trackpad')
            # set full màn hình
            # root.attributes("-fullscreen", True)
            # size máy
            ###
            # width = GetSystemMetrics(0)
            # height = GetSystemMetrics(1)
            root.geometry('1280x960')
            img_bytes = conn.recv(9999999)
            bg = PhotoImage(data = img_bytes)
            label = tk.Label(root,image = bg )
            label.place(x=0,y=0)
            root.bind('<Motion>', motion)
            root.bind("<Button-1>", leftClick)
            root.bind("<Button-3>", rightClick)
            root.mainloop()
        finally:
            conn.close()

