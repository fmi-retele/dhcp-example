'''
Stub to capture DHCP messages
'''
import scapy
from scapy.sendrecv import sendp, sniff

# TODO: write a filter to capture DHCP
filter_message=''
pkts = sniff(count=2, filter=filter_message)
print "Captured {} packets".format(len(pkts))
