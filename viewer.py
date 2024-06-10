#!/usr/bin/env python3

import glob

import ipbus_parser
import curses
import culour

file_list = glob.glob("packets/*.bin")
file_list.sort()

def read_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data

def display_packet(stdscr, filename, packet):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    packet_str = str(packet)
    
    stdscr.addstr(0, 0, f"Filename: {filename}")

    # Truncate the string if it's too long to fit on the screen
    for i, line in enumerate(packet_str.splitlines()):
        if i+1 >= max_y:
            break
        culour.addstr(stdscr, i+1, 0, line[:max_x])
        # stdscr.addstr(i, 0, line[:max_x])
    stdscr.refresh()


def main(stdscr):
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