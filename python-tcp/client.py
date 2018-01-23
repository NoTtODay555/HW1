import socket

TCP_IP = '169.254.195.86'
TCP_PORT = 16
BUFFER_SIZE = 1024

MESSAGE = (str(input('Enter your number : ')))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
