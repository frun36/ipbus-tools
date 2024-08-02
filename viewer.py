#!/usr/bin/env python3

import glob

from ipbus_parser import Packet, PacketType, TransactionInfoCode, TransactionType, PacketTagger
import curses
from reg_info import RegInfo, DisplayMode

import argparse

class ViewerSettings:
    display_mode = DisplayMode.FULL.value
    filename_label = "Filename:"
    labels_padding = 5
    first_transaction = 0

    @classmethod
    def first_trans_up(cls):
        if cls.first_transaction != 0:
            cls.first_transaction -= 1
    @classmethod 
    def first_trans_down(cls):
        cls.first_transaction += 1

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return bytearray(data)

def display_packet(stdscr, filename, packet):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()

    header_color = curses.color_pair(4) if filename[-7:] == "req.bin" else curses.color_pair(5)

    # Upper bar
    stdscr.addstr(0, 0, ' ' * (max_x - 1), header_color)
    stdscr.addstr(0, 0, f"{ViewerSettings.filename_label} {filename}"[:max_x], header_color)
    
    # Label
    if packet.label:
        stdscr.addstr(0, len(filename) + len(ViewerSettings.filename_label ) + ViewerSettings.labels_padding, f"Label: {packet.label}"[:max_x], header_color)

    curr_line = 2
    
    # Packet header
    stdscr.addstr(curr_line, 
                  0, 
                  f"ID: {packet.header.packet_id} | {PacketType(packet.header.packet_type)}"[:max_x], 
                  curses.color_pair(2))


    # Transactions
    curr_line += 2
    all_shown = True
    line_idx = -1
    for transaction in packet.transactions:
        # Header
        line_idx += 1
        if line_idx < ViewerSettings.first_transaction:
            continue
        if curr_line >= max_y:
            all_shown = False
            break 
        stdscr.addstr(curr_line, 
                      0, 
                      f"ID: {transaction.header.transaction_id} | {TransactionType(transaction.header.type_id)} {transaction.header.words} | {TransactionInfoCode(transaction.header.info_code)}"[:max_x], 
                      curses.color_pair(3))
        curr_line += 1

        # Words
        idx = 0
        for word in transaction.words:
            if curr_line >= max_y:
                all_shown = False
                break
            stdscr.addstr(curr_line, 0, repr(word)[:max_x])
            match transaction.header.type_id :
                case 0x0 | 0x2:
                    curr_line, all_shown = reg_info_word(stdscr, curr_line, max_y, all_shown, word, transaction)
                case 0x1 | 0x3 | 0x4 | 0x5:
                    if idx == 0:
                        curr_line, all_shown = reg_info_word(stdscr, curr_line, max_y, all_shown, word, transaction)
                        curr_line, all_shown = reg_info_transaction(stdscr, curr_line, max_y, all_shown, transaction)
                case _:
                    pass
            idx += 1
            curr_line += 1
        #curr_line, all_shown = reg_info_transaction(stdscr, curr_line, max_y, all_shown, transaction)
        curr_line += 1

    # Bottom bar
    stdscr.addstr(max_y - 1, 0, ' ' * (max_x - 1), curses.color_pair(1))
    stdscr.addstr(max_y - 1, 0, f"{'All lines shown' if all_shown else 'Resize for more'}; q - quit; r - refresh file list; m - change display mode", curses.color_pair(1))

    stdscr.refresh()

def reg_info_word(stdscr, curr_line, max_y, all_shown,  word, transaction):
    extra_word = RegInfo.transaction_word(ViewerSettings.display_mode, word, transaction.header.type_id, transaction.header.info_code)
    if extra_word:
        for line in extra_word:
            curr_line += 1
            if curr_line >= max_y:
                all_shown = False
                break 
            stdscr.addstr(curr_line, 0, f"-> {line}", curses.color_pair(6))
    return curr_line, all_shown

def reg_info_transaction(stdscr, curr_line, max_y, all_shown, transaction):
    extra_word = RegInfo.transaction(ViewerSettings.display_mode,transaction)
    if extra_word:
        curr_line += 1
        for line in extra_word:
            if curr_line >= max_y:
                all_shown = False
                break 
            stdscr.addstr(curr_line, 0, f"-> {line}", curses.color_pair(6))
            curr_line += 1
    return curr_line, all_shown

def reparse_and_display(stdscr, file):
    data = read_file(file)
    try:
        packet = Packet.from_bytes(data)
        PacketTagger.tag_packet(packet)
    except ValueError as e:
        packet = f"Value error: {e}"

    display_packet(stdscr, file, packet)

def get_file_list(input_dir):
    file_list = glob.glob(input_dir + "/*.bin")
    file_list.sort()
    return file_list

def main():
    parser = argparse.ArgumentParser(description="Allows for displaying IPbus packets saved as raw bytes")
    
    parser.add_argument('-f', '--filtered', action='store_true', help='Show packets from `filtered_packets` directory (instead of `packets`)')

    args = parser.parse_args()

    file_list = get_file_list("filtered_packets" if args.filtered else "packets")
    
    if not file_list:
        print("No .bin files found.")
        return
    
    index = len(file_list) - 1  # Start with the most recent file
    reparse = True

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(False)

    # Curses color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN) # for app menus
    curses.init_pair(2, curses.COLOR_CYAN, -1) # for packet headers
    curses.init_pair(3, curses.COLOR_MAGENTA, -1) # for transaction headers
    curses.init_pair(6, curses.COLOR_YELLOW, -1) # for register info

    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_MAGENTA) # for request packets
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_CYAN) # for response packets

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
            ViewerSettings.first_transaction = 0
            reparse = True
        elif key == curses.KEY_LEFT:
            if index <= 0:
                curses.beep()
                continue
            index -= 1
            ViewerSettings.first_transaction = 0
            reparse = True
        elif key == curses.KEY_DOWN:
            ViewerSettings.first_trans_down()
            reparse = True
        elif key == curses.KEY_UP:
            ViewerSettings.first_trans_up()
            reparse = True
        elif key == ord('r'):
            file_list = get_file_list()
        elif key == ord('m'):
            ViewerSettings.display_mode = DisplayMode.next_mode(ViewerSettings.display_mode)
            reparse = True
        elif key == ord('q'):  # Quit on 'q' key press
            break
    
    stdscr.clear()
    stdscr.refresh()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.curs_set(True)
    curses.endwin()
            

if __name__ == "__main__":
    main()