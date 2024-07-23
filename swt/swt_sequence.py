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
                case TransactionType.READ | TransactionType.READ_AND | TransactionType.READ_SUM:
                    result += 'read\n' # ignores read timeouts
                case TransactionType.WRITE | TransactionType.WRITE_OR:
                    pass
                case _:
                    raise ValueError("Invalid transaction type value")
        return result
    
    def append_sequence(self, other):
        self.commands += other.commands
    
    @classmethod
    def from_ipbus_transaction(cls, transaction):
        transaction_words = list(map(lambda t: t.get_value(), transaction.get_words()))
        base_address = transaction_words[0]
        seq = cls()
        match transaction.header.type_id:
            case ipb.TransactionType.READ.value:
                for i in range(transaction.header.words):
                    seq.insert_command(SwtWord(TransactionType.READ, base_address + i))
            case ipb.TransactionType.WRITE.value:
                for i in range(transaction.header.words):
                    seq.insert_command(SwtWord(TransactionType.WRITE, base_address + i, transaction_words[i+1]))
            case ipb.TransactionType.NON_INCREMENTING_READ.value:
                for i in range(transaction.header.words):
                    seq.insert_command(SwtWord(TransactionType.READ, base_address))
            case ipb.TransactionType.NON_INCREMENTING_WRITE.value:
                for i in range(transaction.header.words):
                    seq.insert_command(SwtWord(TransactionType.WRITE, base_address, transaction_words[i+1]))
            case ipb.TransactionType.RMW_BITS.value:
                seq.insert_command(SwtWord(TransactionType.READ_AND, base_address, transaction_words[1]))
                seq.insert_command(SwtWord(TransactionType.WRITE_OR, base_address, transaction_words[2]))
            case ipb.TransactionType.RMW_SUM.value:
                seq.insert_command(SwtWord(TransactionType.READ_SUM, base_address, transaction_words[1]))
            case _:
                raise ValueError(f"IPbus transaction type id {transaction.header.type_id} is unsupported")
        return seq
    
    @classmethod
    def from_ipbus_packet(cls, packet):
        if packet.header.packet_type != ipb.PacketType.CONTROL:
            ValueError(f"Packet with packet type {packet.header.packet_type} is not a control packet")
        transactions = packet.transactions
        seq = SwtSequence()
        for transaction in transactions:
            seq.append_sequence(SwtSequence.from_ipbus_transaction(transaction))
        return seq
