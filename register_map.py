from ipbus_parser import Transaction
from ipbus_parser import TransactionHeader

class RegisterMap:
        _register_map={
        0x0: {
            "brief": "A-side phase delay",
            (0, 15): "A-side phase delay"
        },
        0x01: {
            "brief": "C-side phase delay",
            (0, 15): "C-side phase delay"
        },
        0x02: {
            "brief": "Laser phase delay",
            (0, 15): "Laser phase delay"
        },
        0x03: {
            "brief": "Attenuator",
            (0, 13): "Position setting",
            (14, 14): "Busy",
            (15, 15): "Not found"
        },
        0x04: {
            "brief": "Switches",
            (4, 4): "Switches"
        },
        0x05: {
            "brief": "Board temperature",
            (0, 15): "Board temperature"
        },
        0x07: {
            "brief": "Board ID",
            (0, 1): "Board type (subdetector)",
            (2, 7): "Unknown field",
            (8, 15): "Board serial number"
        },
        0x08: {
            "brief": "Vertex Time low threshold",
            (0, 9): "Vertex Time low threshold"
        },
        0x09: {
            "brief": "Vertex Time high threshold",
            (0, 9): "Vertex Time high threshold"
        },
        0x0A: {
            "brief": "SemiCentral level A | Nchannels level",
            (0, 15): "SemiCentral level A | Nchannels level"
        },
        0x0B: {
            "brief": "SemiCentral level C | InnerRings level",
            (0, 15): "SemiCentral level C | InnerRings level"
        },
        0x0C: {
            "brief": "Central level A | Charge level",
            (0, 15): "Central level A | Charge level"
        },
        0x0D: {
            "brief": "Central level C | OuterRings level",
            (0, 15): "Central level C | OuterRings level"
        },
        0x0E: {
            "brief": "Mode",
            (0, 0): "C-side delay + 25ns",
            (1, 2): "Sides combination mode",
            (3, 3): "Extended readout mode",
            (4, 7): "Correlation counter select",
            (8, 8): "SemiCentral evaluation mode",
            (9, 9): "Triggers mode",
            (10, 10): "Reset per-BC trigger counters"
        },
        0x0F: {
            "brief": "Board status, reset commands",
            (0, 0): "PLL lock C",
            (1, 1): "PLL lock A",
            (2, 2): "System restarted",
            (3, 3): "Actual clock source",
            (4, 4): "GBT Rx ready",
            (5, 5): "GBT Rx error detected",
            (6, 6): "GBT Rx phase error",
            (7, 7): "BCID sync lost",
            (8, 8): "Dropping hits",
            (9, 9): "Reset counters",
            (10, 10): "Force local clock",
            (11, 11): "Reset system",
            (12, 12): "PMA0 status has changed",
            (13, 13): "PMA1 status has changed",
            (14, 14): "PMA2 status has changed",
            (15, 15): "PMA3 status has changed",
            (16, 16): "PMA4 status has changed",
            (17, 17): "PMA5 status has changed",
            (18, 18): "PMA6 status has changed",
            (19, 19): "PMA7 status has changed",
            (20, 20): "PMA8 status has changed",
            (21, 21): "PMA9 status has changed",
            (22, 22): "PMC0 status has changed",
            (23, 23): "PMC1 status has changed",
            (24, 24): "PMC2 status has changed",
            (25, 25): "PMC3 status has changed",
            (26, 26): "PMC4 status has changed",
            (27, 27): "PMC5 status has changed",
            (28, 28): "PMC6 status has changed",
            (29, 29): "PMC7 status has changed",
            (30, 30): "PMC8 status has changed",
            (31, 31): "PMC9 status has changed"
        },
        0x10: {
            "brief": "PMA 0 link status",
            (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
        },
        0x11: {
            "brief": "PMA 1 link status",
            (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
        },
        0x12: {
            "brief": "PMA 2 link status",
            (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
        },
        0x13: {
            "brief": "PMA 3 link status",
            (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
        },
        0x14: {
                "brief": "PMA 4 link status",

                 (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x15: {
                "brief": "PMA 5 link status",
                 (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x16: {
                "brief": "PMA 6 link status",
                 (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x17: {
                "brief": "PMA 7 link status",
                 (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x18: {
                "brief": "PMA 8 link status",
                 (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x19: {
                "brief": "PMA 9 link status",

               (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x1A: {
        "brief": "Side A status, channel mask",
        (0, 9): "channel mask",
        (10, 16): "BITS_NOT_USED",
        (17,17): "sync error in channel A0",
        (18,18): "sync error in channel A1",
        (19,19): "sync error in channel A2",
        (20,20): "sync error in channel A3",
        (21,21): "sync error in channel A4",
        (22,22): "sync error in channel A5",
        (23,23): "sync error in channel A6",
        (24,24): "sync error in channel A7",
        (25,25): "sync error in channel A8",
        (26,26): "sync error in channel A9",
        (27,27): "master link delay error",
        (28,28): "side A enabled",
        (29,29): "delay range error",
        (30,30): "ready bit (31) changes state",
        (31,31): "side A links OK, ready"
        },
        0x1B: {
        "brief": "Laser control",
        (0, 23): "divider",
        (24): "once per N orbits mode",
        (25, 29): "BITS_NOT_USED",
        (30): "laser enabled",
        (31): "laser actuation source"
        },
        0x1C: {
        "brief": "Laser pattern (32 LSB)",
        (0, 31): "Laser pattern (32 LSB)"
        },
        0x1D: {
        "brief": "Laser pattern (32 MSB)",
        (0, 31): "Laser pattern (32 MSB)"
        },
        0x1E: {
        "brief": "Bitmask of PM link enabled by SPI",
        (0, 20): "Bitmask of PM link enabled by SPI",
        (21, 31): "BITS_NOT_USED"
        },
        0x1F: {
        "brief": "Triggers suppression control",
        (0, 5): "Delay",
        (6, 7): "Duration",
        (8, 31): "BITS_NOT_USED"
        },
        0x20: {
        "brief": "Average time for each side",
        (0, 15): "Side A average time",
        (16, 31): "Side C average time"
        },
        0x30:{
                "brief": "PMC 0 link status",

                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x31:{
                "brief": "PMC 1 link status",

                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x32:{
                "brief": "PMC 2 link status",

                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x33:{
                "brief": "PMC 3 link status",
                
                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x34:{
                "brief": "PMC 4 link status",
                
               (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x35:{
                "brief": "PMC 5 link status",
                
                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x36:{
                "brief": "PMC 6 link status",
                
                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x37:{
                "brief": "PMC 7 link status",
                
                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x38:{
                "brief": "PMC 8 link status",
                
                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x39:{
                "brief": "PMC 9 link status",
                
                (0, 4): "Line 0 delay",
            (5, 5): "Signal 0 lost",
            (6, 6): "Signal 0 stable",
            (7, 7): "BITS_NOT_USED",
            (8, 12): "Line 1 delay",
            (13, 13): "Signal 1 lost",
            (14, 14): "Signal 1 stable",
            (15, 15): "BITS_NOT_USED",
            (16, 20): "Line 2 delay",
            (21, 21): "Signal 2 lost",
            (22, 22): "Signal 2 stable",
            (23, 23): "Bit positions OK",
            (24, 28): "Line 3 delay",
            (29, 29): "Signal 3 lost",
            (30, 30): "Signal 3 stable",
            (31, 31): "Link OK"
              },
        0x3A: {
        "brief": "Side C status, channel mask",
        (0, 9): "channel mask",
        (10, 16): "BITS_NOT_USED",
        (17, 17): "sync error in channel C0",
        (18, 18): "sync error in channel C1",
        (19, 19): "sync error in channel C2",
        (20, 20): "sync error in channel C3",
        (21, 21): "sync error in channel C4",
        (22, 22): "sync error in channel C5",
        (23, 23): "sync error in channel C6",
        (24, 24): "sync error in channel C7",
        (25, 25): "sync error in channel C8",
        (26, 26): "sync error in channel C9",
        (27, 27): "master link delay error",
        (28, 28): "side C enabled",
        (29, 29): "delay range error",
        (30, 30): "ready bit (31) changes state",
        (31, 31): "side C links OK, ready"
        },
        0x50: {
                "brief": "Counters read interval",
                (0, 2): "Counters read interval",
                (3, 31): "BITS_NOT_USED"
        },
        0x60: {
                "brief": "Trigger 5 signature",
                (0, 13): "Trigger 5 signature",
                (14, 31): "BITS_NOT_USED"
        },
        0x61: {
                "brief": "Trigger 5 random rate",
                (0, 31): "Trigger 5 random rate"
        },
        0x62:{
                "brief": "Trigger 4 signature",
                (0,13):  "Trigger 4 signature",
                (14,32): "BITS_NOT_USED"
            },
        0x63:{
                "brief":"Trigger 4 random rate",
                (0, 31): "Trigger 4 random rate"
            },
        0x64:{
                "brief": "Trigger 2 signature",
                (0,13):  "Trigger 2 siganture",
                (14,32): "BITS_NOT_USED"
            },
        0x65:{
                "brief": "Trigger 2 random rate",
                (0, 31):  "Trigger 2 random rate"
            },
        0x66:{
                "brief": "Trigger 1 signature",
                (0,13):  "Trigger 1 signaturee",
                (14,32): "BITS_NOT_USED"
            },
        0x67:{
                "brief": "Trigger 1 random rate",
                (0, 31):  "Trigger 1 random rate"
            },
        0x68:{
                "brief": "Trigger 3 signature",
                (0,13):  "Trigger 3 siganture",
                (14,32): "BITS_NOT_USED"
            },
        0x69:{
                "brief": "Trigger 3 random rate",
                (0, 31):  "Trigger 3 random rate"
            },
        0x6A:{
                "brief": "Triggers output mode",
                (0,1):  "Trigger 5 output mode",
                (2,2):  "Trigger 5 output enabled",
                (3,4):  "Trigger 4 output mode",
                (5,5):  "Trigger 4 output enabled",
                (6,7):  "Trigger 2 output mode",
                (8,8):  "Trigger 2 output enabled",
                (9,10):  "Trigger 1 output mode",
                (11,11):  "Trigger 1 output enabled",
                (12,13):  "Trigger 3 output mode",
                (14,14):  "Trigger 3 output enabled",
                (15,31):  "BITS_NOT_USED"
            },
        0x70:{
                "brief": "Trigger 5 counter: OrA | FV0 Or",
                (0,31): "Trigger 5 counter: OrA | FV0 Or" 
            },
        0x71:{
                "brief": "Trigger 4 counter: OrC | OuterRings",
                (0,31): "Trigger 4 counter: OrC | OuterRings"
            },
        0x72:{
                "brief": "Trigger 2 counter: SemiCentral | Nchannels",
                (0,31): "Trigger 2 counter: SemiCentral | Nchannels"
            },
        0x73:{
                "brief": "Trigger 1 counter: Central | Charge",
                (0,31): "Trigger 1 counter: Central | Charge" 
            },
        0x74:{
                "brief":  "Trigger 3 counter: Vertex | InnerRings",
                (0,31): "Trigger 3 counter: Vertex | InnerRings"
            },
        0x75:{
                "brief": "Background 0 counter: NoiseA | Noise",
                (0,31):  "Background 0 counter: NoiseA | Noise"
            },
        0x76:{
                "brief": "Background 1 counter: NoiseC | (not used)",
                (0,31):  "Background 1 counter: NoiseC | (not used)"
            },
        0x77:{
                "brief": "Background 2 counter: Total noise | Noise",
                (0,31):  "Background 2 counter: Total noise | Noise"
            },
        0x78:{
                "brief": "Background 3 counter: CB-OrA | CB-Or",
                (0,31): "Background 3 counter: CB-OrA | CB-Or"
            },
        0x79:{
                "brief": "Background 4 counter: CB-OrC | (not used)",
                (0,31): "Background 4 counter: CB-OrC | (not used)"
            },
        0x7A:{
                "brief": "Background 5 counter: Interaction | (not used)",
                (0,31):  "Background 5 counter: Interaction | (not used)"
            },
        0x7B:{
                "brief": "Background 6 counter: CB-Interaction | (not used)",
                (0,31): "Background 6 counter: CB-Interaction | (not used)"
            },
        0x7C:{
                "brief": "Background 7 counter: CB-Vertex | CB-InnerRings",
                (0,31): "Background 7 counter: CB-Vertex | CB-InnerRings"
            },
        0x7D:{
                "brief": "Background 8 counter: BackgroundA | (not used)",
                (0,31):  "Background 8 counter: BackgroundA | (not used)"
            },
        0x7E:{
                "brief": "Background 9 counter: BackgroundC | BackgroundC",
                (0,31): "Background 9 counter: BackgroundC | BackgroundC"
            },
        0xD8:{
                "brief": "Mode settings, commands",
                (0,3): "Data emulation mode",
                (4,7): "Triggers emulation mode",
                (8,8): "Reset orbit sync",
                (9,9): "Reset data counters",
                (10,10): "Reset start of emulation",
                (11,11): "Reset Rx error",
                (12,12): "Reset GBT",
                (13,13): "Reset Rx phase error",
                (14,14): "Reset readout FSM",
                (15,15): "Reset error report FIFO",
                (16,19): "CTP emulation run type",
                (20,20): "HB response",
                (21,21): "Bypass mode",
                (22,22): "Force idle",
                (23,23): "HB reject",
                (24,24): "Shift Rx phase",
                (25,25): "EMU orbit jump",
                (26,31): "BITS_NOT_USED" 
            },
        0xD9:{
                "brief": "Trigger respond mask",
                (0,31): "Trigger respond mask" 
            },
        0xDA:{
                "brief": "Emulated data pattern",
                (0,3): "Number of words in event 0",
                (4,7):  "Number of words in event 1",
                (8,11): "Number of words in event 2",
                (12,15): "Number of words in event 3",
                (16,19): "Number of words in event 4",
                (20,23): "Number of words in event 5",
                (24,27): "Number of words in event 6",
                (28,31): "Number of words in event 7"
            },
        0xDC:{
                "brief": "Emulated triggers pattern LSB",
                (0,31): "Emulated triggers pattern LSB"
            },
        0xDD:{
                "brief": "Emulated triggers pattern MSB",
                (0,31): "Emulated triggers pattern MSB"
            },
        0xDE:{
                "brief": "Emulated triggers value",
                (0,31): "Emulated triggers value" 
            },
        0xDF:{
                "brief": "Emulation rate",
                (0,15): "Data",
                (16,31): "Triggers" 
            },
        0xE0:{
                "brief": "Generators frequency offset",
                (0,11): "Data generator",
                (12,15): "BITS_NOT_USED",
                (16,27): "Triggers generator",
                (28,31): "Emulated HBr triggers rate"
            },
        0xE3:{
                "brief": "BCID offset",
                (0,11): "BCID shift to compensate signal processing delay" 
            },
        0xE4:{
                "brief": "Data select trigger mask",
                (0,31):  "Data select trigger mask - event data with trigger's  BCID is sent (only for triggered mode)"
            },
        0xE8:{
                "brief": "Modes, status",
                (0,0): "Phase aligner CPLL lock",
                (1,1): "Rx wordclk ready",
                (2,2): "Rx frameclk ready",
                (3,3): "MGT link ready",
                (4,4): "Tx reset done",
                (5,5): "Tx FSM reset done",
                (6,6): "GBT Rx ready",
                (7,7): "GBT Rx error",
                (8,8): "GBT Rx error latch",
                (9,9): "Rx phase error",
                (10,15): "BITS_NOT_USED",
                (16,19): "Board run mode",
                (20,23): "BCID sync mode",
                (24,27): "Rx phase",
                (28,31): "CRU run mode" 
            },
        0xE9:{
                "brief": "CRU orbit",
                (0,31): "CRU orbit" 
            },
        0xEA:{
                "brief": "CRU BC",
                (0,11): "CRU BC",
                (12,31): "BITS_NOT_USED" 
            },
        0xEB:{
                "brief": "FIFO count",
                (0,15): "Raw",
                (16,31): "Selector" 
            },
        0xEC:{
                "brief": "Selector first hit dropped orbit",
                (0,31): "Selector first hit dropped orbit" 
            },
        0xED:{
                "brief": "Selector last hit dropped orbit",
                (0,31): "Selector last hit dropped orbit" 
            },
        0xEE:{
                "brief": "Selector hits dropped",
                (0,31): "Selector hits dropped" 
            },
        0xEF:{
                "brief": "Readout rate",
                (0,15): "Readout rate",
                (16,31): "BITS_NOT_USED" 
            },
        0xF7:{
                "brief": "ATX mega128a3u microcode timestamp":
                (0,5): "Second",
                (6,11): "Minute",
                (12,16): "Hour",
                (17,22): "Year",
                (23,26): "Month",
                (27,31): "Day" 
            },
        0xF8:{
                "brief": "Register for FW upgrade in normal mode",
                (0,31): "Register for FW upgrade in normal mode"
            },
        0xF9:{
                "brief": "Register for FW upgrade in normal mode",
                (0,31): "Register for FW upgrade in normal mode"
            },
        0xFA:{
                "brief": "Register for FW upgrade in normal mode",
                (0,31): "Register for FW upgrade in normal mode"
            },
        0xFB:{
                "brief": "Register for FW upgrade in normal mode",
                (0,31): "Register for FW upgrade in normal mode"
            },
        0xFC:{
                "brief": "FPGA temperature",
                (0,31): "FPGA temperature" 
            },
        0xFD:{
                "brief": "1V power",
                (0,31): "1V power" 
            },
        0xFE:{
                "brief":  "1.8V power",
                (0,31): "1.8V power"
            },
        0xFF:{
                "brief": "FPGA firmware timestamp",
                (0,31): "FPGA firmware timestamp" 
            },
        0x100:{
                "brief": "TCM counters values readout",
                (0,31): "TCM counters values readout" 
            },
        0x101:{
                "brief": "TCM counters FIFO load",
                (0,31):  "TCM counters FIFO load"
            }

        }
    
        def __init__(self):
                pass
        @classmethod
        def read_params(cls, reg_info, bit_start, len):
              if (bit_start, bit_start+len-1) in reg_info:
                    return reg_info[(bit_start, bit_start+len-1)]
              else:
                    start_aligned = False
                    params = []
                    for key, desc in reg_info.items():
                          if key == "brief": 
                                continue
                          if key[0] < bit_start: 
                                continue
                          if key[0] == bit_start:
                                start_aligned = True
                          if key[0] > bit_start + len-1:
                                break
                          if key[1] > bit_start + len:
                                params.append("Operation is not aligned with register layout")
                                break
                          if start_aligned == False:
                                params.append("Operation is not aligned with register layout")
                                break
                          elif desc != "BITS_NOT_USED":
                                params.append(f"[{key[0]}, {key[1]}]  {desc}")
                    return params
              

        UnknownRegisterLabel = "Unknown register"
        @classmethod
        def get_register(cls, address, bit_start, len):
            if address in cls._register_map:
                reg = cls._register_map[address]
                params = [reg["brief"]] + cls.read_params(reg, bit_start, len)
                return params
            else:
                return [f"{cls.UnknownRegisterLabel:.<45}0x{address:08x}"]

        @classmethod 
        def describe_read(cls, address):
            return cls.get_register(address, 0,32)
           
        @classmethod
        def describe_write(cls, address):
            return cls.get_register(address,0,32)
        
        @classmethod
        def describe_RMWbits(cls, words):
            address = words[0]
            bit_start = cls.find_first_zero_bit_position(words[1], 32)
            len = cls.find_last_zero_bit_position(words[1],32) - bit_start + 1
            return cls.get_register(address, bit_start, len)
        
        @classmethod
        def describe_RMWsum(cls, words): 
             address = words[0]
             return cls.get_register(address, 0, 31)
              
        @classmethod
        def find_first_zero_bit_position(cls, mask: int, bit_length: int) -> int:
            for i in range(bit_length):
                if (mask & (1 << i)) == 0:
                    return i
            return -1
        
        @classmethod
        def find_last_zero_bit_position(cls, mask: int, bit_length: int) -> int:
            last_zero_position = -1
            for i in range(bit_length - 1, -1, -1):
                if (mask & (1 << i)) == 0:
                    last_zero_position = i
                    break
            return last_zero_position


#print(RegisterMap.get_register(0x6A, 0, 4))
