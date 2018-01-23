import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 5333
BUFFER_SIZE = 2048  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
    

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    newimg = open('clint_icon.png','wb')
    newimg.write(data)
    newimg.close()
    conn.send(data)  # echo
conn.close()
