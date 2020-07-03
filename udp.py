
from socket import * 

host = "hackthissite.org"            
s = socket(AF_INET, SOCK_DGRAM)

for port in range(10,65535):
	#print(port)
	try:
		data = "Hello"
		print("Try "+str(port))
		s.sendto(data,(host,port))
		s.settimeout(0)
		print ((s.recvfrom(1024)))
		break
	except:
		pass
                        