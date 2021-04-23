#Project: Remote Desktop - Python
#Author: Trương Việt Anh
#Description: Chương trình kết nối client - server viết bằng python với những chức năng cơ bản như 
lăng nghe request, gửi ảnh client-server, các điều khiển di chuột,click,scroll và các phím điều khiển,
phóng to nhỏ..
#Usage:
	Cài đặt những lib cần thiết cho project như pyautogui,Pillow,tkinter
	- pip: python -m pip install --upgrade pip
	- pyautogui : pip install pyautogui
	- Pillow : pip install pillow
	- Tkinter: pip install tk
	Chạy chương trình
	- Chỉnh thông số host,port phù hợp với máy của mình server,client
	- Máy server: Mở màn hình cmd -> ipconfig -> Wireless LAN adapter Wi-Fi -> ipV4
	- Đổi thông số host ở ở server và client theo ip vừa lấy được