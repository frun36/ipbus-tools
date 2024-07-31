from swt.swt_word import *
from swt.swt_sequence import *
import ipbus_parser as ipb

import argparse
import sys

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return bytearray(data)

def main():
    parser = argparse.ArgumentParser(description="Converts an IPbus packet into the corresponding SWT sequence")
    
    parser.add_argument('filename', type=str, help='The IPbus packet filename')
    parser.add_argument('-s', '--seq', action='store_true', help='Convert to FRED .sqc file format')

    args = parser.parse_args()
    
    # Read the content of the input file
    try:
        packet_bytes = read_file(args.filename)
    except FileNotFoundError:
        print(f"Error: The file '{args.filename}' could not be found")
        sys.exit(1)

    packet = ipb.Packet.from_bytes(packet_bytes)

    seq = SwtSequence.from_ipbus_packet(packet)
    if args.seq:
        print(repr(seq))
    else:
        print(str(seq))
    
if __name__ == '__main__':
    main()

# packet_bytes = read_file("packets/20240617_172134026620_req.bin")
# packet_bytes = read_file("packets/20240617_172134063481_req.bin")


# header = ipb.TransactionHeader(2, 0, 2, ipb.TransactionType.WRITE.value, ipb.TransactionInfoCode.REQUEST.value)
# transaction = ipb.Transaction(header, [ipb.TransactionWord('test', 0), ipb.TransactionWord('test', 1), ipb.TransactionWord('test', 2)])
# print(transaction)

# seq = SwtSequence.from_ipbus_transaction(transaction)
