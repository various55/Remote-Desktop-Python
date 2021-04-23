import socket
import tkinter as tk
host = '192.168.1.3'
port = 9091
label = None
img_copy = None


def sendData(data):
    conn.send(data.encode())
    getImage()

def getImage():
    img_bytes = conn.recv(999999)
    print('Image form client')
    image = tk.PhotoImage(data=img_bytes)
    label.configure(image=image)
    label.image = image

def motion(event):
    x, y = event.x, event.y
    data = str(x)+' '+str(y)
    sendData(data)

def mouseEvent(event):
    print(event)
    x, y = event.x, event.y
    data = str(event.num) + ' ' + str(x) + ' ' + str(y)
    sendData(data)

def scroll(event):
    print('Scroll',event)
    delta = event.delta
    data = 'Scroll '+str(delta)
    sendData(data)
def key(event):
    msg = event.char
    code = event.keycode
    if(code == 13):
        msg = 'enter'
    elif (code == 32):
        msg = 'space'
    print(event)
    data = 'Key ' + msg
    sendData(data)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)
    #Giao dien
    root = tk.Tk()
    root.title('Python Remote Trackpad')
    root.geometry('1920x1080')

    root.bind('<Motion>', motion)
    root.bind("<Button-1>", mouseEvent)
    root.bind("<Button-3>", mouseEvent)
    root.bind("<MouseWheel>", scroll)
    root.bind("<Key>",key)
    print('Waiting ......')
    while True:
        try:
            conn, address = server_socket.accept()
            print("Connection from: " + str(address))
            img_bytes = conn.recv(999999)
            image = tk.PhotoImage(data = img_bytes)
            label = tk.Label(root,image = image)
            label.place(x=0,y=0)
            label.pack()
            root.mainloop()
        except:
            pass
        finally:
            conn.close()

