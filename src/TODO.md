#### TODO 1: 
- start [wireshark](https://www.wireshark.org/)
- capture the correct interface and filter by "udp and (port 68 or port 67)"
- run dhcp.py
- look at the structure of Discover and Offer packages

#### TODO 2: 
-	use scapy.sendrecv.sniff() to capture the Discover and Offer packages
-	finalize capture_dhcp.py
-	hint: see count and filter parameters for the sniff() function

#### TODO 3:
-	try to send the (message-type, accept)
