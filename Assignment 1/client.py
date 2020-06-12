import socket
import sys

serverIP = sys.argv[1] 
serverPort = sys.argv[2]
filename = sys.argv[3]

try: 
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
	print ("FAIL! Could not create socket. Error code:" + strmsg[0] + ", Error message:" + msg[1])
	sys.exist()

clientSocket.connect((serverIP, int(serverPort)))

message = "GET /" + filename + " HTTP/1.1\r\n\r\n"


try:
	clientSocket.send(message.encode())

except socket.error:

	print ('Hmm, something went wrong! Send failed!')

	sys.exit()

info = ""

serverResponse = clientSocket.recv(1024)

print ('Reply from server:')


while serverResponse:

	info = info + serverResponse.decode()
	serverResponse = clientSocket.recv(1024)

	print(info)

clientSocket.close()
