# Takes an IP address and runs a SYN scan on all ports

from scapy.all import IP, ICMP, TCP, sr1
import sys

# ICMP packet to check whether host is online
def icmp_probe(ip):
    icmp_packet = IP(dst=ip) / ICMP()
    resp_packet = sr1(icmp_packet, timeout=10) # Sends and receives one packet only
    return resp_packet != None

# Send a SYN packet and check the response
def syn_scan(ip, port):
    return IP(dst=ip) / TCP(dport=port, flags='S')

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]

    if icmp_probe(ip):
        syn_ack_packet = syn_scan(ip, port)
        # No response, port is probably closed
        # If response, check it contains a TCP packet with SYN and ACK flags set
        #   SYN -> Value of TCP packet is \0x02
        #   ACK -> Value of TCP packet is \x10
        #   SYN, ACK -> Value of TCP packet is \0x12
        syn_ack_packet.show()
        # Can check the packet's flags
        # resp_packet.getlayer('TCP').flags == 0x12
    else:
        print("ICMP Probe Failed")