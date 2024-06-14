#!/usr/bin/env python3

import glob

import ipbus_parser
import curses

file_list = glob.glob("packets/*.bin")
file_list.sort()

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return bytearray(data)

def display_packet(stdscr, filename, packet):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    
    stdscr.addstr(0, 0, ' ' * (max_x - 1), curses.color_pair(1))
    stdscr.addstr(0, 0, f"Filename: {filename}"[:max_x], curses.color_pair(1))

    stdscr.addstr(2, 0, repr(packet.header), curses.color_pair(2))
    curr_line = 4
    all_shown = True
    for transaction in packet.transactions:
        if curr_line >= max_y:
            all_shown = False
            break 
        stdscr.addstr(curr_line, 0, repr(transaction.header)[:max_x], curses.color_pair(3))
        curr_line += 1
        for word in transaction.words:
            if curr_line >= max_y:
                all_shown = False
                break 
            stdscr.addstr(curr_line, 0, repr(word)[:max_x])
            curr_line += 1
        curr_line += 1

    stdscr.addstr(max_y - 1, 0, ' ' * (max_x - 1), curses.color_pair(1))
    stdscr.addstr(max_y - 1, 0, f"{'All lines shown' if all_shown else 'Resize for more'}; q - quit", curses.color_pair(1))

    stdscr.refresh()


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    # Curses color pairs
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN) # for app menus
    curses.init_pair(2, curses.COLOR_CYAN, -1) # for packet headers
    curses.init_pair(3, curses.COLOR_MAGENTA, -1) # for transaction headers

    file_list = glob.glob("packets/*.bin")
    file_list.sort()
    
    if not file_list:
        stdscr.addstr(0, 0, "No .bin files found.")
        stdscr.refresh()
        stdscr.getch()
        return
    
    index = len(file_list) - 1  # Start with the most recent file
    reparse = True

    while True:
        if reparse:
            data = read_file(file_list[index])
            try:
                packet = ipbus_parser.Packet.from_bytes(data)
            except ValueError as e:
                packet = f"Value error: {e}"
            reparse = False
       
            display_packet(stdscr, file_list[index][8:], packet)
        
        key = stdscr.getch()
        
        if key == curses.KEY_RIGHT:
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
        elif key == ord('q'):  # Quit on 'q' key press
            break
            

if __name__ == "__main__":
    curses.wrapper(main)