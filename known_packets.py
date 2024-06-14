from ipbus_parser import *
from enum import Enum

class PacketTypes:
    STATUS = "STATUS"
    SYNC = "SYNC"

class KnownPackets:
    status_header = bytes.fromhex("200000f1")
    headers = \
    {
        status_header: PacketTypes.STATUS
    }
    
    @classmethod
    def check_header(cls, packet_bytes):
        if packet_bytes in cls.headers:
            return cls.headers[packet_bytes]
        return None
    
    @classmethod 
    def check_packet(cls, packet):
        type = cls.check_header(packet[0:4])
        if type: return type
        return None
