import cv2

camera = cv2.VideoCapture(0)
i = 0
while i < 3:
    input('Nhấn Enter để chụp ảnh')
    return_value, image = camera.read()
    cv2.imwrite('img' + str(i) + '.png', image)
    i += 1
del (camera)