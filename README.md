# dhcp-example
##### Crafting a DHCP discover packet. 

##### Requirements:
- use any linux or use the [vbox machine](https://github.com/fmi-retele/vbox-scapy/releases/download/v1/osbox.vdi.tar.gz)
- check that you have [scapy](http://www.secdev.org/projects/scapy/) installed
- see the different protocol [headers](https://github.com/fmi-retele/dhcp-example/blob/master/scapy-protocols.md)
- follow the [dhcp tutorial](www.atoz-networking.blogspot.in/2009/09/how-dhcp-works.html)
- dhcp uses the [bootp header](http://www.networksorcery.com/enp/protocol/bootp.htm) + options 
- [homework assignment](https://github.com/fmi-retele/dhcp-example/blob/master/src/TODO.md)


### [RFC 2131](http://www.ietf.org/rfc/rfc2131.txt)     
                Server          Client          Server
            (not selected)                    (selected)

                  v               v               v
                  |               |               |
                  |     Begins initialization     |
                  |               |               |
                  | _____________/|\____________  |
                  |/DHCPDISCOVER | DHCPDISCOVER  \|
                  |               |               |
              Determines          |          Determines
             configuration        |         configuration
                  |               |               |
                  |\             |  ____________/ |
                  | \________    | /DHCPOFFER     |
                  | DHCPOFFER\   |/               |
                  |           \  |                |
                  |       Collects replies        |
                  |             \|                |
                  |     Selects configuration     |
                  |               |               |
                  | _____________/|\____________  |
                  |/ DHCPREQUEST  |  DHCPREQUEST\ |
                  |               |               |
                  |               |     Commits configuration
                  |               |               |
                  |               | _____________/|
                  |               |/ DHCPACK      |
                  |               |               |
                  |    Initialization complete    |
                  |               |               |
                  .               .               .
                  .               .               .
                  |               |               |
                  |      Graceful shutdown        |
                  |               |               |
                  |               |\ ____________ |
                  |               | DHCPRELEASE  \|
                  |               |               |
                  |               |        Discards lease
                  |               |               |
                  v               v               v
    Timeline diagram of messages exchanged between DHCP
    client and servers when allocating a new network address
