colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'end_color': '\033[0m'
}

class Packet:
    def __init__(self, header, transactions) -> None:
        self.header = header
        self.transactions = transactions

    def __repr__(self) -> str:        
        result = colors['red'] + '-' * 8 + f" BEGIN PACKET 0x{self.header.packet_id:04x} " + '-' * 8 + colors['end_color'] + "\n\n"
        result += repr(self.header) + "\n\n"
        for (i, transaction) in enumerate(self.transactions):
            result += f"{colors['purple']}Transaction 0x{i:02x}:{colors['end_color']}\n{repr(transaction)}\n"
        result += colors['red'] + '-' * 8 + f" END PACKET 0x{self.header.packet_id:04x} " + '-' * 8 + colors['end_color'] + "\n"
        return result

    @classmethod
    def from_le_bytes(cls, bytes):
        header = PacketHeader.from_le_bytes(bytes[0:4])
        transactions = []

        curr_index = 4
        while curr_index < len(bytes):
            transaction = Transaction.from_le_bytes(bytes[curr_index:])
            transactions.append(transaction)
            curr_index += 4 * transaction.get_total_words()

        return cls(header, transactions)
    
    @staticmethod
    def bytes_to_le_word(bytes):
        if len(bytes) % 4 != 0:
            raise ValueError("Length of byte array should be a multiple of 4")
        
        for i in range(0, len(bytes), 4):
            word_bytes = bytes[i:i + 4]
            word = int.from_bytes(word_bytes, byteorder='little')
            yield word

class PacketHeader:
    def __init__(self, protocol_version, rsvd, packet_id, byte_order_qualifier, packet_type) -> None:
        self.protocol_version = protocol_version
        self.rsvd = rsvd
        self.packet_id = packet_id
        self.byte_order_qualifier = byte_order_qualifier
        self.packet_type = packet_type
    
    def __repr__(self) -> str:
        return colors['yellow'] + \
               f"Protocol Version: 0x{self.protocol_version:01x} | " \
               f"RSVD: 0x{self.rsvd:01x} | " \
               f"Packet ID: 0x{self.packet_id:04x} | " \
               f"Byte Order Qualifier: 0x{self.byte_order_qualifier:01x} | " \
               f"Packet Type: 0x{self.packet_type:01x}" + colors['end_color']

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
    
class Transaction:
    def __init__(self, header, words, word_labels) -> None:
        self.header = header
        self.words = words
        self.word_labels = word_labels

    def __repr__(self) -> str:
        result = str(self.header) + "\n"
        for (word_label, word) in zip(self.word_labels, self.words):
            result += f"{word_label:.<32}0x{word:08x}\n"
        return result

    @classmethod
    def from_le_bytes(cls, bytes):
        header = TransactionHeader.from_le_bytes(bytes[0:4])
        word_labels = header.get_payload_fields()
        last_byte = 4 + len(word_labels) * 4
        words = Packet.bytes_to_le_word(bytes[4:last_byte])
        return cls(header, words, word_labels)
    
    def get_total_words(self):
        return 1 + len(self.word_labels)

class TransactionHeader:
    def __init__(self, protocol_version, transaction_id, words, type_id, info_code) -> None:
        self.protocol_version = protocol_version
        self.transaction_id = transaction_id
        self.words = words
        self.type_id = type_id
        self.info_code = info_code
    
    def __repr__(self) -> str:
        return colors['cyan'] + \
               f"Protocol Version: 0x{self.protocol_version:01x} | " \
               f"Transaction ID: 0x{self.transaction_id:03x} | " \
               f"Words: 0x{self.words:02x} | " \
               f"Type ID: 0x{self.type_id:01x} | " \
               f"Info code: 0x{self.info_code:01x}" + colors['end_color']

    @classmethod
    def from_le_bytes(cls, bytes):
        info_code = bytes[0] & 0x0f
        type_id = bytes[0] >> 4
        words = bytes[1]
        transaction_id = bytes[2] + ((bytes[3] & 0x0f) << 8)
        protocol_version = bytes[3] >> 4
        return cls(protocol_version, transaction_id, words, type_id, info_code)
    
    def get_request_payload_fields(self) -> list[str]:
        match self.type_id:
            case 0x0 | 0x2 | 0x6: # Read | Non-incrementing read | Configuration space read
                return ["BASE_ADDRESS"]
            case 0x1 | 0x3 | 0x7 : # Write | Non-incrementing write | Configuration space write
                return ["BASE_ADDRESS"] + [f"Data for BASE_ADDRESS + {i}" for i in range(self.words)]
            case 0x4: # RMWbits
                return ["BASE_ADDRESS", "AND term", "OR term"]
            case 0x5: # RMWsum
                return ["BASE_ADDRESS", "Addend"]
            case _:
                raise ValueError(f"Invalid type ID value 0x{self.type_id:01x} for transaction ID 0x{self.transaction_id:03x}")
    
    def get_response_payload_fields(self) -> list[str]:
        match self.type_id:
            case 0x0 | 0x2 | 0x6: # Read | Non-incrementing read | Configuration space read
                return [f"Data read from BASE_ADDRESS + {i}" for i in range(self.words)]
            case 0x1 | 0x3 | 0x7 : # Write | Non-incrementing write | Configuration space write
                return []
            case 0x4: # RMWbits
                return ["Data in BASE_ADDRESS before"]
            case 0x5: # RMWsum
                return ["Data in BASE_ADDRESS before"]
            case _:
                raise ValueError(f"Invalid type ID value 0x{self.type_id:01x} for transaction ID 0x{self.transaction_id:03x}")

    def get_payload_fields(self) -> list[str]:
        match self.info_code:
            case 0xf: # Request
                return self.get_request_payload_fields()
            case 0x0: # Response
                return self.get_response_payload_fields()
            case 0x1 | 0x4 | 0x5 | 0x6 | 0x7: # Response - error
                return [] # Not sure if should really be empty?
            case _:
                raise ValueError(f"Invalid info code value 0x{self.info_code:01x} for transaction ID 0x{self.transaction_id:03x}")
    
# print(Packet.from_le_bytes([0xf0, 0x00, 0x00, 0x20, 0x4f, 0x01, 0x00, 0x20, 0x0e, 0x00, 0x00, 0x00, 0xff, 0xfc, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x1f, 0x01, 0x01, 0x20, 0x66, 0x00, 0x00, 0x00, 0xb4, 0x25, 0x00, 0x00, 0x1f, 0x01, 0x02, 0x20, 0x64, 0x00, 0x00, 0x00, 0x33, 0x26, 0x00, 0x00, 0x1f, 0x01, 0x03, 0x20, 0x68, 0x00, 0x00, 0x00, 0xb2, 0x26, 0x00, 0x00, 0x1f, 0x01, 0x04, 0x20, 0x62, 0x00, 0x00, 0x00, 0x31, 0x27, 0x00, 0x00, 0x1f, 0x01, 0x05, 0x20, 0x60, 0x00, 0x00, 0x00, 0xb0, 0x27, 0x00, 0x00]))

# test_transaction = Transaction.from_le_bytes([0x4f, 0x01, 0x00, 0x20, 0x0e, 0x00, 0x00, 0x00, 0xff, 0xfc, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00])

# print(test_transaction)