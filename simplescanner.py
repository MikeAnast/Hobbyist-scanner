
import socket
import threading
import Queue


#print "Target to scan: "
#targetIP = raw_input("> ")
#print "Number of threads: "
#threads = int(raw_input("> "))

#target = "https://www.hackthissite.org"
#target = 'pythonprogramming.net'

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


def port_worker():
    while not q.empty():
        port = q.get()
        if portscan(target,port):
            print("port {} is open".format(port))
            open_ports.append(port)
        else:
            print("port {} is closed".format(port))
         

def threader(q):
    while True:
        worker = q.get()
        port_worker()
        q.task_done()



#ip = socket.gethostbyname(target)
#print(ip)
if __name__ == "__main__":
   target = 'hackthissite.org'
   Nthreads=100
   print(target)
   threads = []
   open_ports = []

   q = Queue.Queue()


   for port in range(1,100):
      q.put(port)

   for i in range(Nthreads):
      t = threading.Thread(name = "Thread id-"+str(i),target=threader,args=(q,))
      threads.append(t)
      t.start()
      threads.append(t)

   for thread in threads:
      thread.join()
   



