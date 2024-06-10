#!/usr/bin/env python3

import glob

import ipbus_parser
import sys
import curses
# import culour

file_list = glob.glob("packets/*.bin")
file_list.sort()

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data

def display_packet(stdscr, packet):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    packet_str = str(packet)
    
    # Truncate the string if it's too long to fit on the screen
    for i, line in enumerate(packet_str.splitlines()):
        if i >= max_y:
            break
        # culour.addstr(stdscr, i, 0, line[:max_x])
        stdscr.addstr(i, 0, line[:max_x])
    
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

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
                packet = ipbus_parser.Packet.from_le_bytes(data)
            except ValueError as e:
                packet = f"Value error: {e}"
            reparse = False

            # stdscr.addstr(0, 0, f"Filename: {file_list[index]}")
        
        display_packet(stdscr, packet)
        
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