import ipbus_parser as ipb
from swt.swt_word import *

class SwtSequence:
    def __init__(self, *commands):
        self.commands = list(commands)

    def insert_command(self, command):
        self.commands.append(command)

    def __repr__(self) -> str:
        result = ''
        for command in self.commands:
            result += str(command)
            out_counter = 0
            match command.type:
               case TransactionType.READ | TransactionType.READ_AND | TransactionType.READ_SUM:
                   result += f'@OUT_{out_counter:04}\n'
                   out_counter += 1
               case TransactionType.WRITE | TransactionType.WRITE_OR:
                   result += '\n'
               case _:
                   raise ValueError("Invalid transaction type value")
        return result

    def __str__(self) -> str:
        result = ''
        for command in self.commands:
            result += str(command)
            match command.type:
               case TransactionType.READ | TransactionType.READ_AND | TransactionType.READ_SUM:
                   result += f',write\nread\n'
               case TransactionType.WRITE | TransactionType.WRITE_OR:
                   result += ',write\n'
               case _:
                   raise ValueError("Invalid transaction type value")
        return result
    
    def append_sequence(self, other):
        self.commands += other.commands
    
    @classmethod
    def from_ipbus_transaction(cls, transaction: ipb.Transaction):
        """Creates a SWT sequence from an IPbus transaction
        
        For different types of IPbus transactions:
        - READ : a series of SWT READ sequences, for each address in the block being read (incrementing)
        - WRITE : a series of SWT WRITE sequences, for each address in the block being written to (incrementing)
        - NON_INCREMENTING_READ : a series of SWT READ sequences, for base_address
        - NON_INCREMENTING_WRITE : a series of SWT WRITE sequences, for base_address
        - RMW_BITS : SWT READ_AND sequence with AND mask, SWT WRITE_OR sequence with OR mask
        - RMW_SUM : SWT READ_SUM sequence with SUM term
        """
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
        """Creates sequences from each transaction in the packet and concatenates them together"""
        
        if packet.header.packet_type != ipb.PacketType.CONTROL:
            ValueError(f"Packet with packet type {packet.header.packet_type} is not a control packet")
        transactions = packet.transactions
        seq = SwtSequence()
        for transaction in transactions:
            seq.append_sequence(SwtSequence.from_ipbus_transaction(transaction))
        return seq
