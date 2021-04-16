import cv2
import pyautogui
import PIL
import socket
import io
import base64,json
host = '127.0.0.1'
port = 9050
bufferSize = 999999

def getScreen():
    image = pyautogui.screenshot("screen.png")
    base64_encode = None
    with open('screen.png', "rb") as f:
        image_binary = f.read()
        base64_encode = base64.b64encode(image_binary)
    return base64_encode

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
                evt = json.loads(data)
                if evt['key'] == 'mousemove':
                    # pyautogui.moveTo(evt['data']['x'],evt['data']['y'])
                    print(evt['data']['x'],evt['data']['y'])
                    sk.sendall(getScreen())
                elif evt['key'] == 'mouseclick':
                    print(evt['data']['btn'],evt['data']['x'],evt['data']['y'])
                    if evt['data']['btn'] == 1:
                        pyautogui.click()
                    elif evt['data']['btn'] == 2:
                        pyautogui.click(button='middle')
                    else:
                        pyautogui.click(button='right')
            except ValueError as e:
                print(e)
            
