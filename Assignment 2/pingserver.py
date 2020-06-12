import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 12032))

while True:
	
	 
	# Receive the client packet along with the address it is coming from 
	message, address = serverSocket.recvfrom(1024)
	
	# Generate random number in the range of 1 to 10 and if rand is less is than 4, we consider the packet lost and tell the client to retransmit
	rand = random.randint(1, 10) 

	if rand < 4:
		

		serverSocket.sendto(message.encode(), address)
		message, address = serverSocket.recvfrom(1024)
		message = message.decode().upper()
		serverSocket.sendto(message.encode(), address)
	
	else:
		
	
	# Capitalize the message from the client and send the capilized version to the client
		message = message.decode().upper()
		serverSocket.sendto(message.encode(), address)
		
    
