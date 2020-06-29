
import socket
import threading
import queue
import time


target = socket.gethostbyname(input("Target to scan ->"))
#target = 'hackthissite.org'
Nports= int(input("Number of ports ->"))




def portscan(target,port):
  try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(10)
    con = sock.connect((target,port))
    #print("port{} is open".format(port))
    #con.close()
    return True
  except:
    return False


def port_worker():
    while not q.empty():
        port = q.get()
        if portscan(target,port):
            open_ports.append(port)
        else:
            closed_ports.append(port)



#ip = socket.gethostbyname(target)
#print(ip)
if __name__ == "__main__":

  print(target)
  threads = []
  open_ports = []
  closed_ports = []


  q = queue.Queue()


  for port in range(1,Nports):
    q.put(port)

  start_time = time.time() 
  for i in range(1,200):
    t = threading.Thread(target=port_worker)
    threads.append(t)



  for t in threads:
    t.daemon = True
    t.start()

  for t in threads:
    t.join()
  print("the runtime is:", float(time.time()-start_time))
  print('open ports',open_ports)
  print('closed ports',closed_ports)








