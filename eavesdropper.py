#!/usr/bin/env python3

import sys
import datetime
import re

import pyshark
import ipbus_parser


UDP_IP = "172.20.75.180"
UDP_PORT = 50001

capture = pyshark.LiveCapture(interface="IPBUS", bpf_filter=f"host {UDP_IP}")

for packet in capture.sniff_continuously():
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f")
        packet_bytes = bytes.fromhex(packet.data.data)
        ipb_packet = ipbus_parser.Packet.from_bytes(packet_bytes)
        ipbus_parser.PacketTagger.tag_packet(ipb_packet)
        print(f"{packet.ip.src}")
        print(ipb_packet)

        if packet.ip.src == UDP_IP:
            filename = f"{timestamp}_res.bin"
        else:
            filename = f"{timestamp}_req.bin"
        
        with open("packets/" + filename, 'ab') as f:
            f.write(packet_bytes)
        if not re.search("_res\\.bin", filename) and ipb_packet.label == "":
            with open("filtered_packets/" + filename, 'ab') as f:
                f.write(packet_bytes)
    except ValueError as e:
        print("Value error:", e, file=sys.stderr)
    except AttributeError as e:
        print("Attribute error:", e, file=sys.stderr)
