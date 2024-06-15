from enum import Enum

class PacketLabels(Enum):
    STATUS = "STATUS PACKET"
    SYNC = "SYNC"
    NON = "NON"

class KnownPackets:
    status_header = "f1000020"
    headers = \
    {
        status_header: PacketLabels.STATUS.value
    }
    
    @classmethod
    def check_header(cls, header: bytes):
        if header.hex() in cls.headers:
            return cls.headers[header.hex()]
        return None
    
    @classmethod 
    def check_packet(cls, packet):
        type = cls.check_header(packet[0:4])
        if type != None: 
            return type
        return None
