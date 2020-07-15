import socket
import threading
import queue
import argparse
from scapy.all import *


target = socket.gethostbyname(input("Target to scan ->"))
#target = 'hackthissite.org'
Nports= int(input("Number of ports ->"))

def udpscan(target,port):
	sport = RandShort()
	udpsock = sr1(IP(dst=target)/UDP(sport=port, dport=port), timeout=10, verbose=0)
	if udpsock.haslayer(ICMP):
		print(port, "Closed")
	elif udpsock.haslayer(UDP):
		print(port, "Open / filtered")
	else:
		print(port, "Unknown")
		print(udpsock.summary())






if __name__ == "__main__":

	print(target)
	threads = []
	open_ports = []
	closed_ports = []
	for port in range(1,Nports):
		udpscan(target,port)
		#if flag:
		#	print("port {} is open".format(port))




