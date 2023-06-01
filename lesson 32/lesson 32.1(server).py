import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((localIP, localPort))
print("UDP server up and listening")

while (True):
    bytesAddressPair = sock.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    sock.sendto(bytesToSend, address)