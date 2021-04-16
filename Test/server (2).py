import tkinter as tk
import cv2
import pyautogui
import PIL
import socket,base64,io,json
host = '127.0.0.1'
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
    receivByte = base64.b64decode(data)
    image_result = open('screen.png', 'wb') # create a writable image and write the decoding result
    image_result.write(receivByte)
    image_result.close()
#mouse move
def motion(event):
    data = {
        "key" : "mousemove",
        "data": {
            "x":event.x,
            "y": event.y
        }
    }
    check = json.dumps(data)
    print(check)
    socket_client.sendall(check.encode('utf-8'))
    
    WriteSceen()
   
    img2 =  tk.PhotoImage(file = 'screen.png')
    background.configure(image = img2)
    background.image = img2

#mouse click
def MouseEventCLick(event):
    data ={
        'key' :'mouseclick',
        'data':{
            'btn':event.num,
            'x':event.x,
            'y':event.y
        }
    }
    check = json.dumps(data)
    print(check)
    socket_client.sendall(check.encode('utf-8'))

#key press
def KeyPress(event):
    print(event)

if __name__ == '__main__':
    sk = CreateSocket()
    print('lisening client connect ....')
    while True:
        socket_client,addr = sk.accept()
        print('client : {}'.format(addr)+'connected')
        data = None
        
        while data == None:
            data = socket_client.recv(bufferSize)
            print(len(data))
            receivByte = base64.b64decode(data)
            image_result = open('screen.png', 'wb') # create a writable image and write the decoding result
            image_result.write(receivByte)
            image_result.close()
            
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
        #key event
        root.bind('<Key>', KeyPress)

        root.geometry("1920x1080")
        #set background to frame
        bg = tk.PhotoImage(file = 'screen.png')
        background = tk.Label(root,image = bg)
        background.place(x=0, y=0)

        # img2 =  tk.PhotoImage(file = 'screen copy.png')
        # background.configure(image = img2)
        # background.image = img2
        root.mainloop()
        socket_client.close()