'''
Sample script to send a DHCP discover
'''
import scapy
from scapy.sendrecv import sendp, sniff
from scapy.all import DHCP, ARP, BOOTP, Ether, UDP, TCP, IP

# data link layer
ethernet = Ether()
ethernet.show()
ethernet.dst = 'ff:ff:ff:ff:ff:ff'

# network layer
ip = IP()
ip.show()
ip.dst='255.255.255.255'

# transport layer
udp = UDP()
udp.show()
udp.sport = 68
udp.dport = 67

# application layer
bootp = BOOTP()
bootp.show()
bootp.flags = 1

dhcp = DHCP()
dhcp.show()
dhcp.options = [("message-type", "discover"), "end"]

packet = ethernet / ip / udp / bootp / dhcp

sendp(packet)


