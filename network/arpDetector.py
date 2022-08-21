# Detects an ARP Spoofing Attack

from scapy.all import sniff

# Build ARP table
IP_MAC_Map = {}

def processPacket(packet):
    src_IP = packet['ARP'].psrc
    src_MAC = packet['Ether'].src 

    # If the packet MAP is in the table
    if src_MAC in IP_MAC_Map.keys():
        # IP address is not the same
        if IP_MAC_Map[src_MAC] != src_IP:
            try:
                old_IP = IP_MAC_Map[src_MAC]
            except:
                old_IP = "unknown"

            message = ("\n Possible ARP attack detected \n "
                    + "It is possible that the machine with IP address " + str(old_IP) + " \n"
                    + "is pretending to be " + str(src_IP) + " \n")
            return message
    else:
        IP_MAC_Map[src_MAC] = src_IP


# Continuously sniff ARP packets without storing them
sniff(count = 0, filter = "arp", store = 0, prn = processPacket)
