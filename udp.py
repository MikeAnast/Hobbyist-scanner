
from socket import * 

host = "hackthissite.org"            


def udpscan(target,port):
  try:
	udpsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	udpsock.sendto("packet example",(target,port))
	#udpcon = udpsock.connect((target,port))
	print("the {} port is open".format(port))
	return True
  except:
	print("false")
	return False




for port in range(1,10000):
	udpscan(host,port)
	
							