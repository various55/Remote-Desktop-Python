from win32api import GetSystemMetrics
import socket # For network connections
from tkinter import  *
import tkinter as tk # To create a graphical user interface

host = '127.0.0.1'
port = 9091
fileName = 'screenshot.png'
def getImage(conn, root):
    img_bytes = conn.recv(9999999)
    print('Image form client')
    # data = conn.recv(1024)
    myFile = open(fileName, 'wb')
    if not img_bytes:
        myFile.close()
    myFile.write(img_bytes)
    myFile.close()
    # set image


def setBackground(conn,root):
    def motion(event):
        x, y = event.x, event.y
        data = str(x*2)+' '+str(y*2)
        conn.send(data.encode())

    def leftClick(event):
        x, y = event.x, event.y
        data = 'LClick '+str(x * 2) + ' ' + str(y * 2)
        conn.send(data.encode())
        getImage(conn, root)
    def rightClick(event):
        print('Right Click')
        x, y = event.x, event.y
        data = 'RClick '+str(x * 2) + ' ' + str(y * 2)
        conn.send(data.encode())
        getImage(conn, root)
        print(3)
    bg = PhotoImage(file=fileName)
    label = Label(root, image=bg)
    label.place(x=-10, y=-90)
    root.bind('<Motion>', motion)
    root.bind("<Button-1>", leftClick)
    root.bind("<Button-3>", rightClick)
    root.mainloop()

if __name__ == '__main__':

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
    global x, y, data
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    while True:
        print("Connection from: " + str(address))
        try:
            setBackground(conn,root)
        finally:
            print('DONE')
    print('Alo')

