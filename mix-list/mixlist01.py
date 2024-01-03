#!/usr/bin/env python3

# display only the IP addresses to the screen.
iplist = [ 22, "80", 55, "10.0.0.1", "10.20.30.1", "ssh", "http" ]

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("Port:", iplist[1], ", and", iplist[0])

# example 3 - use an 'f-string'
print(f"port name: {iplist[5]}, and {iplist[6]}")

