import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    sum = 1
    for i in range (1,int(data)+1):
        sum = sum * i
    Data = str(int(sum))
    print "received message:", Data
    