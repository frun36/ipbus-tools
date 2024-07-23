import ipbus_parser as ipb
from swt.swt_word import *

class SwtSequence:
    def __init__(self, *commands):
        self.commands = list(commands)

    def insert_command(self, command):
        self.commands.append(command)

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
    
    def __add__(self, other):
        return SwtSequence(*(self.commands + other.commands))
    
    @classmethod
    def from_ipbus_transaction(cls, transaction):
        base_address = transaction.get_words()[0].get_value()
        seq = cls()
        match transaction.header.type_id:
            case ipb.TransactionType.READ.value:
                for i in range(transaction.header.words):
                    seq.insert_command(SwtWord(TransactionType.READ, base_address + i))
            case ipb.TransactionType.WRITE.value:
                for i in range(transaction.header.words):
                    seq.insert_command(SwtWord(TransactionType.WRITE, base_address + i, transaction.get_words()[i+1].get_value()))
            case _:
                raise ValueError(f"IPbus transaction type id {transaction.header.type_id} is unsupported")
        return seq
    
    @classmethod
    def from_ipbus_packet(cls, packet):
        if packet.header.packet_type != ipb.PacketType.CONTROL:
            ValueError(f"Packet with packet type {packet.header.packet_type} is not a control packet")
        transactions = packet.transactions
        return sum(map(lambda transaction: cls.from_ipbus_transaction(transaction), transactions))
