import socket                                                                             
import threading                                                                          
import os                                                                       
																						   
																						   
                                                             
target = input("Target to scan ->")

Nports= int(input("Number of ports ->"))                                                               
#print "Number of threads: "                                                              
#threads = int(raw_input("> "))                                                           
																						   
#target = "https://www.hackthissite.org"                                                                                                        
							
#Nports = int(Nports)

def portscan(target,port):

	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                               
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.settimeout(10)
	try:                                                                                  
		con = sock.connect((target,port))                                                 
		print("port{} is open".format(port))                                              
		con.close()                                                                       
	except:                                                                               
		return 0 


if __name__=="__main__":                                                                  
	#target = 'hackthissite.org'                                                           
	threads=[]                                                                            
	print(target)                                                                         
																	   
																					   
	for port in range(1,Nports):                                                             
		#print(port)                                                                       
		#result = portscan(target,port)                                                   
		t =threading.Thread(target=portscan,args=(target,port,))                          
		t.setDaemon(True)                                                                 
		threads.append(t)
	
	for i in range(0,Nports-1):
		threads[i].start()                                                                         
		                                                                        
																					   
	for i in range(0,Nports-1):                                                                
		threads[i].join()
	
