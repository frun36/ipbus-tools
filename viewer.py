#!/usr/bin/env python3

import glob

from ipbus_parser import Packet, PacketType, TransactionInfoCode, TransactionType
import curses

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return bytearray(data)

def display_packet(stdscr, filename, packet):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    ui_header_height = 1

    # Upper bar
    stdscr.addstr(0, 0, ' ' * (max_x - 1), curses.color_pair(1))
    stdscr.addstr(0, 0, f"Filename: {filename}"[:max_x], curses.color_pair(4) if filename[-7:] == "req.bin" else curses.color_pair(5))
    
    # Label
    if packet.label:
        stdscr.addstr(1, 0, f"Label: {packet.label}"[:max_x], curses.color_pair(1))
        ui_header_height = 2

    curr_line = ui_header_height + 1

    # Packet header
    stdscr.addstr(curr_line, 
                  0, 
                  f"ID: {packet.header.packet_id} | {PacketType(packet.header.packet_type)}"[:max_x], 
                  curses.color_pair(2))


    # Transactions
    curr_line += 2
    all_shown = True
    for transaction in packet.transactions:
        # Header
        if curr_line >= max_y:
            all_shown = False
            break 
        stdscr.addstr(curr_line, 
                      0, 
                      f"ID: {transaction.header.transaction_id} | {TransactionType(transaction.header.type_id)} | {TransactionInfoCode(transaction.header.info_code)}"[:max_x], 
                      curses.color_pair(3))
        curr_line += 1

        # Words
        for word in transaction.words:
            if curr_line >= max_y:
                all_shown = False
                break 
            stdscr.addstr(curr_line, 0, repr(word)[:max_x])
            curr_line += 1
        curr_line += 1

    # Bottom bar
    stdscr.addstr(max_y - 1, 0, ' ' * (max_x - 1), curses.color_pair(1))
    stdscr.addstr(max_y - 1, 0, f"{'All lines shown' if all_shown else 'Resize for more'}; q - quit; r - refresh file list", curses.color_pair(1))

    stdscr.refresh()

def reparse_and_display(stdscr, file):
    data = read_file(file)
    try:
        packet = Packet.from_bytes(data)
    except ValueError as e:
        packet = f"Value error: {e}"

    display_packet(stdscr, file[8:], packet)

def get_file_list():
    file_list = glob.glob("packets/*.bin")
    file_list.sort()
    return file_list

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(False)

    # Curses color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN) # for app menus
    curses.init_pair(2, curses.COLOR_CYAN, -1) # for packet headers
    curses.init_pair(3, curses.COLOR_MAGENTA, -1) # for transaction headers

    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA) # for request packets
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_CYAN) # for response packets

    stdscr.keypad(True)

    file_list = get_file_list()
    
    if not file_list:
        stdscr.addstr(0, 0, "No .bin files found.")
        stdscr.refresh()
        stdscr.getch()
        return
    
    index = len(file_list) - 1  # Start with the most recent file
    reparse = True

    while True:
        if reparse:
            reparse_and_display(stdscr, file_list[index])
            reparse = False
       
        key = stdscr.getch()
        
        if key == curses.KEY_RESIZE:
            reparse = True
        elif key == curses.KEY_RIGHT:
            if index >= len(file_list) - 1:
                curses.beep()
                continue
            index += 1
            reparse = True
        elif key == curses.KEY_LEFT:
            if index <= 0:
                curses.beep()
                continue
            index -= 1
            reparse = True
        elif key == ord('r'):
            file_list = get_file_list()
        elif key == ord('q'):  # Quit on 'q' key press
            break
            

if __name__ == "__main__":
    curses.wrapper(main)