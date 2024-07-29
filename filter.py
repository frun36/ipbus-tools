#!/usr/bin/env python3

import glob
import shutil
import re
import os

from ipbus_parser import Packet, PacketTagger

def get_file_list(input_dir):
    file_list = glob.glob(input_dir + "/*.bin")
    file_list.sort()
    return file_list

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return bytearray(data)

def main():
    file_list = get_file_list("packets")

    for filename in file_list:
        bytes = read_file(filename)
        try:
            packet = Packet.from_bytes(bytes)
            PacketTagger.tag_packet(packet)
            print(filename, packet.label)

            if not re.search("_res\\.bin", filename) and packet.label == "":
                shutil.copyfile(filename, 'filtered_packets/' + os.path.basename(filename))
        except ValueError as ve:
            print(f'ValueError while parsing packet: {ve}')





if __name__ == '__main__':
    main()