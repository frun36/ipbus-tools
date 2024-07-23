from swt.swt_word import *
from swt.swt_sequence import *
import ipbus_parser as ipb

# cmd1 = SwtWord(TransactionType.READ_OR, 0xbadf00db, 0xadc0ffee)
# cmd2 = SwtWord(TransactionType.WRITE_AND, 0xbadf00d0, 0x76543210)
# seq1 = SwtSequence(cmd1, cmd2)

# cmd3 = SwtWord(TransactionType.READ, 0x01234567)
# seq2 = SwtSequence(cmd3)
# print(seq1 + seq2)

header = ipb.TransactionHeader(2, 0, 2, ipb.TransactionType.WRITE.value, ipb.TransactionInfoCode.REQUEST.value)
transaction = ipb.Transaction(header, [ipb.TransactionWord('test', 0), ipb.TransactionWord('test', 1), ipb.TransactionWord('test', 2)])
print(transaction)

seq = SwtSequence.from_ipbus_transaction(transaction)
print(seq)