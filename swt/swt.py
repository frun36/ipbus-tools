from enum import Enum

class TransactionType(Enum):
    READ = 0b000
    WRITE = 0b001
    READ_OR = 0b010
    WRITE_AND = 0b011
    READ_SUM = 0b100

class SwtWord:
    def __init__(self, type, address, data = 0):
        self.type = type
        self.address = address
        self.data = data
    
    def get_bytes(self):
        bytes = bytearray(10)
        # SWT ID
        bytes[0] = 0x30
        
        # Type of the transaction
        bytes[1] = self.type.value

        # Address
        bytes[2] = (self.address >> 24) & 0xff
        bytes[3] = (self.address >> 16) & 0xff
        bytes[4] = (self.address >> 8) & 0xff
        bytes[5] = self.address & 0xff

        # Data
        bytes[6] = (self.data >> 24) & 0xff
        bytes[7] = (self.data >> 16) & 0xff
        bytes[8] = (self.data >> 8) & 0xff
        bytes[9] = self.data & 0xff

        return bytes
    
    def __str__(self) -> str:
        return '0x' + ''.join(map(lambda x : f"{x:02x}", self.get_bytes()))


class SwtSequence:
    def __init__(self, *commands):
        self.commands = list(commands)

    def __str__(self) -> str:
        result = ''
        for command in self.commands:
            result += f'{command},write\n'
            match command.type:
                case TransactionType.READ | TransactionType.READ_OR | TransactionType.READ_SUM:
                    result += 'read\n' # ignores read timeouts
                case TransactionType.WRITE | TransactionType.WRITE_AND:
                    pass
                case _:
                    raise ValueError("Invalid transaction type value")
        return result

cmd1 = SwtWord(TransactionType.READ_OR, 0xbadf00db, 0xadc0ffee)
cmd2 = SwtWord(TransactionType.WRITE_AND, 0xbadf00d0)
seq = SwtSequence(cmd1, cmd2)
print(seq)
