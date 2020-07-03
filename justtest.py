

#https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_recon/service_discovery/index.html
import random
from scapy.all import ICMP, IP, sr1, TCP
from socket import gethostbyname
# Define end host and TCP port range
#host = 'scanme.nmap.org'
https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_recon/service_discovery/index.html
host = 'hackthissite.org'
ipdom = 137.74.187.104
print(ipdom)


# VARIABLES
src = '160.40.49.165'

dst = ipdom
sport = random.randint(1024,65535)
dport = 80

syn_packet = IP(dst='137.74.187.104')/TCP(dport=80,flags='S')
resp = sr1(syn_packet)
resp.sprintf('%TCP.src% \t %TCP.sport% \t %TCP.flags%')

 iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 137.74.187.104 -j DROP