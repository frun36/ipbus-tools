#!/usr/bin/env python3

import socket
import sys
import datetime

import ipbus_parser

UDP_IP = "127.0.0.1"
UDP_PORT = 50001

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
    sent = sock.sendto(data, addr)

    filename = f"packets/{timestamp}.bin"
    with open(filename, "wb") as f:
        f.write(data)

    try:
        print(ipbus_parser.Packet.from_le_bytes(data)) # This assumes little endianness
    except ValueError as e:
        print("Value error:", e, file=sys.stderr) 
    print("Sent %d bytes" % sent)

# First (status packet) is sent as big endian. Consecutive packets are little endian