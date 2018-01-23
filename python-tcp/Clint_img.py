import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5333
BUFFER_SIZE = 2048
img = open('icon.png','rb')
image = img.read()
img.close()
MESSAGE = (image)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
newimg = open('sever_icon.png','wb')
newimg.write(data)
newimg.close()

s.close()


