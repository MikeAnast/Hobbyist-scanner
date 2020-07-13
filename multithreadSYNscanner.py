import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # Disable the annoying No Route found warning !
from scapy.all import *
from socket import gethostbyname
from pyfiglet import Figlet
import queue
import threading



logo = Figlet(font='doom')
print(logo.renderText('Rick the greek'))









'''
packet = IP header + TCP header + data
https://medium.com/@NickKaramoff/tcp-packets-from-scratch-in-python-3a63f0cd59fe
https://resources.infosecinstitute.com/port-scanning-using-scapy/#gref
https://www.binarytides.com/raw-socket-programming-in-python-linux/
'''


''' Flag values of a TCP packet
FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

'F': 'FIN',
'S': 'SYN',
'R': 'RST',
'P': 'PSH',
'A': 'ACK',
'U': 'URG',
'E': 'ECE',
'C': 'CWR',

'''


def listening(ip):
    icmp = IP(dst=ip)/ICMP()    #pinging the ip with the protocl ICMP to see if the IP is up
    resp = sr1(icmp,timeout=2)
    if resp ==None:
        return False
    else:
        return True






def SYNscanner(ip,startports,finishports):
    #conf.verb = 0
    start = time.time()
    closed_ports = []
    open_ports =[]
    close = 0
    if listening(ip):
        print("ip is:",listening(ip))
        for port in range(startports,finishports+1):
            try:
                source_port = RandShort()
                SYNpacket = IP(dst=ip)/TCP(sport=source_port, dport = port, flags='S')  #make a SYN packet
                responce = sr1(SYNpacket, timeout=10) #sending the packet
                if responce.getlayer(TCP).flags==0x12:
                    send_rst = sr(IP(dst=ip)/TCP(sport=source_port, dport=port, flags='AR'), timeout=1) #'AR'= ACK-RST 
                    open_ports.append(port)
                elif responce.getlayer(TCP).flags ==0x14:
                    closed_ports.append(port)
            except AttributeError:
                #print("port is not listening")
                closed_ports.append(port)
        timelance = time.time()- start
        return open_ports,closed_ports,timelance
        #print("open ports are:", open_ports)
        #print("scan completed in {} seconds".format(timelance))
        #print("the number of closed ports is", closed_ports)



def MultiSYNscanner(ip, port):
    closed_ports = []
    open_ports =[]
    if listening(ip):
        print("ip is:",listening(ip))
        try:
            source_port = RandShort()
            SYNpacket = IP(dst=ip)/TCP(sport=source_port, dport = port, flags='S')  #make a SYN packet
            responce = sr1(SYNpacket, timeout=10) #sending the packet
            if responce.getlayer(TCP).flags==0x12:
                send_rst = sr(IP(dst=ip)/TCP(sport=source_port, dport=port, flags='AR'), timeout=1) #'AR'= ACK-RST 
                return True
            elif responce.getlayer(TCP).flags ==0x14:
                return False        
        except:
            print("port is not listening")
            return False
        


def port_worker():
    while not q.empty():
        port = q.get()
        if MultiSYNscanner(ip,port):
            open_ports.append(port)
        else:
            closed_ports.append(port)







if __name__=='__main__':
    #ip = socket.gethostbyname(input("Target to scan ->"))
    #target = 'hackthissite.org'
    #start_ports= int(input("Number of first port ->"))
    #finish_ports = int(input("Number of last port ->"))
    ip = gethostbyname('hackthissite.org')
    print("this is correct",listening(ip))
    start_ports = 443
    finish_ports = 445
    print(ip)
    '''
    threads = []
    open_ports = []
    closed_ports = []
    q = queue.Queue()

    for port in range(start_ports,finish_ports):
        q.put(port)

    for i in range(1,10):
        t = threading.Thread(target=port_worker)
        threads.append(t)



    for t in threads:
        t.daemon = True
        t.start()

    for t in threads:
        t.join()

    print('open ports',open_ports)
    print('closed ports',closed_ports)
    '''
    scanner = SYNscanner(ip,start_ports,finish_ports)
    print("open ports are:",scanner[0])
    print("closed ports are:",scanner[1])
