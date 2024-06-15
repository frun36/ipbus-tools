from .known_packets import KnownPackets
from .parameters import Endianness
from .transaction import Transaction

class Packet:
    def __init__(self, header, transactions, endianness, label) -> None:
        self.header = header
        self.transactions = transactions
        self.endianness = endianness
        self.label = label

    def __repr__(self) -> str:        
        result = '-' * 8 + f" BEGIN PACKET 0x{self.header.packet_id:04x} " + '-' * 8 + "\n\n"
        result += repr(self.header) + "\n\n"
        for (i, transaction) in enumerate(self.transactions):
            result += f"Transaction 0x{i:02x}:\n{repr(transaction)}\n"
        result += '-' * 8 + f" END PACKET 0x{self.header.packet_id:04x} " + '-' * 8 + "\n"
        return result

    @classmethod
    def from_bytes(cls, bytes):
        print(type(bytes))
        if bytes[3] & 0xf0 == 0xf0:
            endianness = Endianness.BIG
            for i in range(0, len(bytes), 4):
                bytes[i:i+4] = reversed(bytes[i:i+4])
        else:
            endianness = Endianness.LITTLE
        
        return cls.from_le_bytes(bytes, endianness)


    @classmethod
    def from_le_bytes(cls, bytes, endianness=Endianness.LITTLE):
        header = PacketHeader.from_le_bytes(bytes[0:4])
        type = KnownPackets.check_packet(bytes)
        transactions = []
        label = KnownPackets.check_packet(bytes)
        curr_index = 4
        while curr_index < len(bytes):
            transaction = Transaction.from_le_bytes(bytes[curr_index:])
            transactions.append(transaction)
            curr_index += 4 * transaction.get_total_words()

        return cls(header, transactions, endianness, label)

class PacketHeader:
    def __init__(self, protocol_version, rsvd, packet_id, byte_order_qualifier, packet_type) -> None:
        self.protocol_version = protocol_version
        self.rsvd = rsvd
        self.packet_id = packet_id
        self.byte_order_qualifier = byte_order_qualifier
        self.packet_type = packet_type
    
    def __repr__(self) -> str:
        return f"Protocol Version: 0x{self.protocol_version:01x} | " \
               f"RSVD: 0x{self.rsvd:01x} | " \
               f"Packet ID: 0x{self.packet_id:04x} | " \
               f"Byte Order Qualifier: 0x{self.byte_order_qualifier:01x} | " \
               f"Packet Type: 0x{self.packet_type:01x}"
    def __bytes__(self):
        return bytes([self.packet_type, self.byte_order_qualifier, self.packet_id, self.rsvd, self.protocol_version])

    @classmethod
    def from_le_bytes(cls, bytes):
        packet_type = bytes[0] & 0x0f
        byte_order_qualifier = bytes[0] >> 4
        if byte_order_qualifier != 0xF:
            raise ValueError(f"Invalid byte order qualifier 0x{byte_order_qualifier:01x} - perhaps the packet is big endian?")
        
        packet_id = bytes[1] + (bytes[2] << 8)
        rsvd = bytes[3] & 0x0f
        protocol_version = bytes[3] >> 4
        return cls(protocol_version, rsvd, packet_id, byte_order_qualifier, packet_type)