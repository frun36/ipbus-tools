#!/usr/bin/env python3

import socket
import sys
import datetime

import pyshark
import ipbus_parser
UDP_IP = "172.20.75.180"
UDP_PORT = 50001

capture = pyshark.LiveCapture(interface="IPBUS", bpf_filter=f"host {UDP_IP}")

for packet in capture.sniff_continuously():
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
        packet_bytes = bytes.fromhex(packet.data.data)
        print(ipbus_parser.Packet.from_bytes(packet_bytes)) # This assumes little endianness
        print(f"{packet.ip.src}")
        if packet.ip.src == UDP_IP:
            filename = f"packets/{timestamp}_res.bin"
        else:
            filename = f"packets/{timestamp}_req.bin"
        with open(filename, 'ab') as f:
            f.write(packet_bytes)
    except ValueError as e:
        print("Value error:", e, file=sys.stderr)
    except AttributeError as e:
        print("Attribute error:", e, file=sys.stderr)
