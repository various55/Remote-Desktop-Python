import cv2
import pyautogui 
from PIL import ImageGrab,Image
import socket
import io
host = '192.168.43.151'
port = 9050
bufferSize = 999999
size = 1920,1080

def getScreen():
    img = ImageGrab.grab()
    img.thumbnail(size, Image.ANTIALIAS)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.connect((host,port))
    print('connected server...')
    sk.sendall(getScreen())
    while True:
        take = sk.recv(1024)
        data = take.decode('utf-8')
        if data:
            try:
                evt = data.split(',')
                if evt[0] == 'mousemove':
                    pyautogui.moveTo(int(evt[1]),int(evt[2]))
                    print(evt[1],evt[2])
                elif evt[0] == 'mouseclick':
                    if evt[1] == '1':
                        pyautogui.click()
                    elif evt[1] == '2':
                        pyautogui.click(button='middle')
                    else:
                        pyautogui.click(button='right')
                elif evt[0] == 'mousedrag':
                    print(evt[1], evt[2])
                    pyautogui.dragTo(int(evt[1]), int(evt[2]), button='left')
                elif evt[0] == 'mousewheel':
                    print('scroll',evt[1])
                    pyautogui.scroll(int(evt[1]))
                elif evt[0] == 'keypress':
                    pyautogui.press(evt[1])
            except ValueError as e:
                pass
            finally:
                sk.sendall(getScreen())
            
