# Detecs an XMas scan

from scapy.all import sniff

def processPacket(packet):
    FIN = 0x01
    PSH = 0x08
    URG = 0x20

    F = packet['TCP'].flags

    # FIN, PSH, URG flags are all set
    if F & FIN and F & PSH and F & URG:
        message = ("\n Possible XMAS scan detected \n")
        return message


# Continuously sniff TCP packets without storing them
sniff(count = 0, filter = "tcp", store = 0, prn = processPacket)