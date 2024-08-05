# IPbus tools
## About
This repository contains tools for analyzing IPbus communication, to help with moving from IPbus to SWT for the FIT DCS.

## Tools
### `ipbus_parser`
Module providing parsing of binary data into IPbus packet and transaction data structures. 

### `interceptor.py` and `eavesdropper.py`
The interceptor intercepts the communication from Control Server entirely, functioning as an echo server. The eavesdropper only listens to the communication with the electronics, registering packets traveling in both directions. 

Packets get saved in the `packets` directory.

### `viewer.py`
Allows for viewing parsed packets and analyzing their contents.

To run simply use
```
./viewer.py [-f]
```
or if that doesn't work
```
python3 viewer.py [-f]
```
like a regular Python script.

The `-f` flag allows you to view packets from the `filtered_packets` directory (instead of `packets`).

### `filter.py`
Filters known Control Server packets and copies all unknown requests from `packets` to `filtered_packets`. Run like a regular Python script.

### `swt`
This module allows for converting raw IPbus packets into corresponding FIT-SWT sequences. To run use
```
python3 -m swt.swt [-h] filename
```
while in the `ipbus-tools` directory.

## Notes
Depending on your system (AGH's FLP), the following might be required:
- running everything with `python3.12`
- running `eavesdropper.py` with `sudo` to have permissions to the interface
- change interface `IPBUS` in `eavesdropper.py` to `eno4`
- a `config.ini` file in the directory from which you run `eavesdropper.py`, with contents like:
```
[tshark]
tshark_path = /usr/local/bin/tshark

[dumpcap]
dumpcap_path = /usr/local/bin/dumpcap
```