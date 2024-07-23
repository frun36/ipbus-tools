# IPbus tools
## About
This repository contains tools for analyzing IPbus communication, to help with moving from IPbus to SWT for the FIT DCS.

## Tools
### `ipbus_parser`
Module providing parsing of binary data into IPbus packet and transaction data structures. 

### `viewer.py`
Allows for viewing parsed packets and analyzing their contents.

To run simply use
```
./viewer.py
```
or if that doesn't work
```
python3 viewer.py
```

### `interceptor.py` and `eavesdropper.py`
The interceptor intercepts the communication from Control Server entirely, functioning as an echo server. The eavesdropper only listens to the communication with the electronics, registering packets traveling in both directions. 

Packets get saved in the `packets` directory.

### `swt`
This module allows for converting raw IPbus packets into corresponding FIT-SWT sequences. To run use
```
python3 -m swt.swt
```
while in the `ipbus-tools` directory.