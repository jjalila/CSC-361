import random, sys, datetime, time
from socket import *

if(len(sys.argv) != 3):
    print("Enter host ip address and port number please")
    sys.exit()

clientSocket = socket(AF_INET, SOCK_DGRAM)
d = datetime.datetime(2020, 3, 06)

host = sys.argv[1]
port = int(sys.argv[2])
address = (host, port)


for i in range(100):
 
        sendingtime = d.utcnow()
        message = "ping {} {}".format(i+1, sendingtime)
        clientSocket.sendto(message, address)

	newmsg, newaddr = clientSocket.recvfrom(1024)

	#newmsg is uppercase, no need for retransmission
	if newmsg != message:
		rtt = (d.utcnow() - sendingtime).total_seconds()
        	print(newmsg + " RTT: {}s".format(rtt))

	else: 
		while newmsg == message:
			print("Retransmitting Ping " + str(i+1))		
			sendingtime = d.utcnow()
	       		message = "ping {} {}".format(i+1, sendingtime)
			clientSocket.sendto(message, address)
			newmsg, newaddr = clientSocket.recvfrom(1024)
			rtt = (d.utcnow() - sendingtime).total_seconds()
			print(newmsg + " RTT: {}s".format(rtt))
			
	

		
	
