from .utils import bytes_to_le_word

class Transaction:
    def __init__(self, header, words) -> None:
        self.header = header
        self.words = words

    def __repr__(self) -> str:
        result = str(self.header) + "\n"
        for word in self.words:
            result += f"{repr(word)}\n"
        return result

    @classmethod
    def from_le_bytes(cls, bytes):
        header = TransactionHeader.from_le_bytes(bytes[0:4])
        word_labels = header.get_payload_fields()
        last_byte = 4 + len(word_labels) * 4
        words = bytes_to_le_word(bytes[4:last_byte])

        words = list(map(lambda t : TransactionWord(t[0], t[1]), zip(word_labels, words)))
        return cls(header, words)
    
    def get_total_words(self):
        return 1 + len(self.words)
    
    def get_words(self):
        return self.words

class TransactionHeader:
    def __init__(self, protocol_version, transaction_id, words, type_id, info_code) -> None:
        self.protocol_version = protocol_version
        self.transaction_id = transaction_id
        self.words = words
        self.type_id = type_id
        self.info_code = info_code
    
    def __repr__(self) -> str:
        return \
               f"Protocol Version: 0x{self.protocol_version:01x} | " \
               f"Transaction ID: 0x{self.transaction_id:03x} | " \
               f"Words: 0x{self.words:02x} | " \
               f"Type ID: 0x{self.type_id:01x} | " \
               f"Info code: 0x{self.info_code:01x}"

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

class TransactionWord:
    def __init__(self, word_label, word) -> None:
        self.word_label = word_label
        self.word = word

    def __repr__(self) -> str:
        return f"{self.word_label:.<48}0x{self.word:08x}"
    
    def get_value(self):
        return self.word