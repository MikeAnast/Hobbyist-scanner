import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # Disable the annoying No Route found warning !
from scapy.all import *
from socket import gethostbyname
from pyfiglet import Figlet
logo = Figlet(font='graffiti')
print(logo.renderText('Rick the greek'))

#https://www.binarytides.com/raw-socket-programming-in-python-linux/

'''
packet = IP header + TCP header + data
https://medium.com/@NickKaramoff/tcp-packets-from-scratch-in-python-3a63f0cd59fe
https://resources.infosecinstitute.com/port-scanning-using-scapy/#gref
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
'''


def listening(ip):
    icmp = IP(dst=ip)/ICMP()    #pinging the ip with the protocl ICMP to see if the IP is up
    resp = sr1(icmp,timeout=2)
    if resp ==None:
        return False
    else:
        return True

def SYNscanner(ip,ports):
    #conf.verb = 0
    start = time.time()
    closed_ports = 0
    open_ports =[]
    close = 0
    if listening(ip):
        print("ip is:",listening(ip))
        for port in range(1,ports):
            try:
                source_port = RandShort()
                SYNpacket = IP(dst=ip)/TCP(sport=source_port, dport = port, flags='S')  #make a SYN packet
                responce = sr1(SYNpacket, timeout=2) #sending the packet
                if responce.getlayer(TCP).flags==0x12:
                    send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
                    open_ports.append(port)
                elif responce.getlayer(TCP).flags ==0x14:
                    close+=1
            except AttributeError:
                print("port is not listening")
        timelance = time.time()- start
        print("open ports are:", open_ports)
        print("scan completed in {} seconds".format(timelance))
        print("the number of closed ports is", close)


if __name__=='__main__':
    ip = gethostbyname('hackthissite.org')
    ports = 3
    print(ip)
    SYNscanner(ip,ports)
    
    #print(scanned)
    #print("open ports are:", scanned[0])
    #print("scan completed in {} seconds".format(scanned[1]))
    #print("the number of closed ports is", scanned[2])






