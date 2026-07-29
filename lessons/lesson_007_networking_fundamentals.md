# Lesson 007: Networking Fundamentals

## Overview

This lesson covers the basic information a device needs to communicate on a network:

- IP address
- Subnet mask
- Default gateway
- DNS server
- MAC address

## IP Address

An IP address identifies a device on a network.

Example:

```text
192.168.1.25

The IP address tells the network where the device is located logically.
Subnet Mask
A subnet mask tells the device which part of an IP address identifies the network and which part identifies the individual 
device.
Example:
IP address:  192.168.1.25
Subnet mask: 255.255.255.0
With this subnet mask, devices beginning with 192.168.1 are usually considered part of the same local network.
Examples:
192.168.1.10
192.168.1.25
192.168.1.200
Default Gateway
The default gateway is the device that sends traffic outside the local network.
In most home networks, the default gateway is the router.
Example:
192.168.1.1
A device first asks:
Is the destination on my local network?

If yes, it communicates directly.
If no, it sends the traffic to the default gateway.
DNS Server
DNS translates human-readable names into IP addresses.
Example:
google.com → an IP address
Without DNS, users would need to remember IP addresses instead of website names.
MAC Address
A MAC address identifies a network interface on the local network.
Example:
A4:5E:60:12:34:56
IP addresses are used for logical routing between networks.
MAC addresses are used for local delivery on the current network.
Basic Communication Flow
When a computer opens a website:
The computer asks DNS for the website’s IP address.
It compares the destination IP with its subnet mask.
It determines whether the destination is local or remote.
If remote, it sends the traffic to the default gateway.
The router forwards the traffic toward the destination.
The response travels back to the computer.
Security+ Connection
These concepts relate to:
Network segmentation
DNS attacks
ARP spoofing
IP conflicts
Man-in-the-middle attacks
Firewall rules
Routing
Network troubleshooting
Key Takeaway
The IP address identifies the device.
The subnet mask defines the local network.
The default gateway provides a path outside the local network.
DNS translates names into IP addresses.
The MAC address handles local network delivery.
