# Table of contents

- [IP Address](#ip-address)
    - [IPv4](#ipv4)
    - [IPv6](#ipv6)
- [Switch](#switch)
- [Router](#router)
- [DHCP (Dynamic Host Configuration Protocol)](#DHCP)
- [DNS (Domain Name System)](#DNS)
- [LAN](#lan)
- [WAN](#wan)
- [NAT](#nat)
- [OSI model](#osi-model)
- [Layer 7: Application](#layer-7)
- [Layer 6: Presentation](#layer-6)
- [Layer 5: Session](#layer-5)
- [Layer 4: Transport](#layer-4)
- [Layer 3: Network](#layer-3)
- [Layer 2: Data Link](#layer-2)
- [Layer 1: Physical](#layer-1)

# IP Address
Internet protocol address, Identifies any device on a network
Use to communicate with each other both on the internet and network

## IPv4
Address length: 32 bits
DNS host records: A records
IP addresses: 4,294,967,296

## IPv6
Address length: 128 bits
DNS host records: AAAA records
IP addresses: 340 undecillion (trillion, trillion, trillion)

# MAC Address
(Physical address) 12 character hexadecimal address, assigned to the network interface adapter (wire or wireless)

# Switch
Device that connects devices within a network and forwards data packets to and from devices
Only sends data to the single device it is intended
Managing traffic between these networks by forwarding data packets to their intended IP addresses

Network switches can operate at either OSI layer 2 (the data link layer) or layer 3 (the network layer). Layer 2 switches forward data based on the destination MAC address (see below for definition), while layer 3 switches forward data based on the destination IP address. Some switches can do both.

Layer 2 switch won't allow communication between different VLAN, Layer 3 switch allow (switch have routing)
# Router
Device that connects two or more packets-switched networks or subnetworks

# DHCP
Dynamic Host Configuration Protocol (DHCP) is a network protocol used to automate the process of configuring devices on IP networks

# DNS
DNS translates domain names to IP addresses so browsers can load Internet resources

## LAN
A LAN is a group of connected devices restricted to a specific geographic area. A LAN usually requires a single router.

## WAN
A WAN, by contrast, is a large network spread out over a vast geographic area. Large organizations and companies that operate in multiple locations across the country, for instance, will need separate LANs for each location, which then connect to the other LANs to form a WAN. Because a WAN is distributed over a large area, it often necessitates multiple routers and switches*.

## NAT
Translate private IP to public IP (remove private IP from header and attach public IP)

# OSI Model
## Layer 7
Human-computer interaction layer, where applications can access the network services
## Layer 6
Ensures that data is in a usable format and is where data encryption occurs
## Layer 5
Maintains connections and is responsible for controlling port and sessions
## Layer 4
Transmits data using Transmission protocols including TCP and UDP

Flow Control: ensures that the transmitting device does not send more data to the receiving device than it can handle
## Layer 3
Decides which physical path the data will take
## Layer 2
Defined the format of data on the network
## Layer 1
Transmits raw bit stream over the physical medium
