import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 8830
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
    

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    sum = 1
    for i in range (1,int(data)+1):
        sum = sum * i
    conn.send(str(int(sum)))  # echo
conn.close()


