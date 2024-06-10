class RegisterMap:
    _register_map = {
        0x0:  {
                -1: "A-side phase delay",
                0: "A-side phase delay"
                },
        0x01: {
                -1: "C-side phase delay",
                0: "C-side phase delay"
                },
        0x02: {
                -1: "Laser phase delay",
                0: "Laser phase delay"
                },
        0x03: {
                -1: "Attenuator",
                0: "Postion setting", 
                14: "Busy", 
                15: "Not found"},
        0x04: {
                -1: "Switches",
                0: "Switches"
                },
        0x05: {
                -1: "Board temperature",
                0: "Board temperature"
                },
        0x07: {
                -1: "Board ID",
                0: "Board type (subdetector)", 
                2: "Unknown field", 
                8: "Board serial number"
                },
        0x08: {
                -1: "Vertex Time low threshold",
                0: "Vertex Time low threshold"
                },
        0x09: {
                -1: "Vertex Time high threshold",
                0: "Vertex Time high threshold"
                },
        0x0A: {
                -1: "SemiCentral level A | Nchannels level",
                0: "SemiCentral level A | Nchannels level"
                },
        0x0B: {
                -1: "SemiCentral level C | InnerRings level",
                0: "SemiCentral level C | InnerRings level",
                },
        0x0C: {
                -1: "Central level A | Charge level",
                0: "Central level A | Charge level"
                },
        0x0D: {
                -1: "Central level C | OuterRings level",
                0: "Central level C | OuterRings level"
                },
        0x0E: {
                -1: "Mode",
                0: "C-side delay + 25ns", 
                1: "Sides combination mode", 
                3: "Extended readout mode", 
                4: "Correlation counter select", 
                8: "SemiCentral evaluation mode", 
                9: "Triggers mode", 
                10: "Reset per-BC trigger counters"},
        0x0F: {
                -1: "Board status, reset commands",
                0: "PLL lock C", 
               1: "PLL lock A", 
               2: "system restarted", 
               3: "actual clock source", 
               4: "GBT Rx ready", 
               5: "GBT Rx error detected", 
               6: "GBT Rx phase error", 
               7: "BCID sync lost", 
               8: "dropping hits", 
               9: "reset counters", 
               10: "force local clock", 
               11: "reset system", 
               12: "PMA0 status has changed", 
               13: "PMA1 status has changed", 
               14: "PMA2 status has changed", 
               15: "PMA3 status has changed", 
               16: "PMA4 status has changed", 
               17: "PMA5 status has changed", 
               18: "PMA6 status has changed", 
               19: "PMA7 status has changed", 
               20: "PMA8 status has changed",
               21: "PMA9 status has changed",
               22: "PMC0 status has changed",
               23: "PMC1 status has changed",
               24: "PMC2 status has changed",
               25: "PMC3 status has changed",
               26: "PMC4 status has changed",
               27: "PMC5 status has changed",
               28: "PMC6 status has changed",
               29: "PMC7 status has changed",
               30: "PMC8 status has changed",
               31: "PMC9 status has changed",
               },
        0x10: {
                -1: "PMA 0 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x11: {
                -1: "PMA 1 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x12: {
                -1: "PMA 2 link status",

                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x13: 
                {
                -1: "PMA 3 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x14: {
                -1: "PMA 4 link status",

                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x15: {
                -1: "PMA 5 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x16: {
                -1: "PMA 6 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x17: {
                -1: "PMA 7 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x18: {
                -1: "PMA 8 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x19: {
                -1: "PMA 9 link status",
                0: "line 0 delay",
                5: "signal 0 lost",
                6: "signal 0 stable",

                8: "line 1 delay",
                13: "signal 1 lost",
                14: "signal 1 stable",

                16: "line 2 delay",
                21: "signal 2 lost",
                22: "signal 2 stable",

                23: "bit positions OK",

                24: "line 3 delay",
                29: "signal 3 lost",
                30: "signal 3 stable",

                31: "link OK"
              },
        0x1A: {
                -1: "Side A status, channel mask",
                0: "channel mask",
                17: "sync error in channel A0",
                18: "sync error in channel A1",
                19: "sync error in channel A2",
                20: "sync error in channel A3",
                21: "sync error in channel A4",
                22: "sync error in channel A5",
                23: "sync error in channel A6",
                24: "sync error in channel A7",
                25: "sync error in channel A8",
                26: "sync error in channel A9",
                27: "master link delay error",
                28: "side A enabled",
                29: "delay range error",
                30: "ready bit (31) changes state",
                31: "side A links OK, ready"
              },
        0x1B:{
                -1: "Laser control",
                0:  "divider",
                24: "once per N orbits mode",
                30: "laser enabled",
                31: "laser actuaion source"
            },
        0x1C:{
                -1: "Laser pattern (32 LSB)",
                0:  "Laser pattern (32 LSB)"
            },
        0x1D:{
                -1: "Laser pattern (32 MSB)",
                0:  "Laser pattern (32 MSB)" 
            },
        0x1E:{
                -1: "Bitmask of PM link enabled by SPI",
                0:  "Bitmask of PM link enabled by SPI"
            },
        0x1F:{
                -1: "Triggers suppression control",
                0:  "Delay",
                6:  "Duration"
            },
        0x20:{
                -1: "Average time for each side",
                0:  "Side A average time",
                16: "Side C average time"
            },
        0x30:{
                -1: "PMC 0 link status",

                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x31:{
                -1: "PMC 1 link status",

                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x32:{
                -1: "PMC 2 link status",

                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x33:{
                -1: "PMC 3 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x34:{
                -1: "PMC 4 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x35:{
                -1: "PMC 5 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x36:{
                -1: "PMC 6 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x37:{
                -1: "PMC 7 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x38:{
                -1: "PMC 8 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x39:{
                -1: "PMC 9 link status",
                
                0: "Line 0 delay",
                5: "Signal 0 lost",
                6: "Signal 0 stable",

                8: "Line 1 delay",
                13: "Signal 1 lost",
                14: "Signal 1 stable",

                16: "Line 2 delay",
                21: "Signal 2 lost",
                22: "Signal 2 stable",

                23: "Bit positions OK",

                24: "Line 3 delay",
                29: "Signal 3 lost",
                30: "Signal 3 stable",

                31: "Link OK"
              },
        0x3A:{
                -1: "Side C status, channel mask",
                0: "channel mask",
                17: "sync error in channel C0",
                18: "sync error in channel C1",
                19: "sync error in channel C2",
                20: "sync error in channel C3",
                21: "sync error in channel C4",
                22: "sync error in channel C5",
                23: "sync error in channel C6",
                24: "sync error in channel C7",
                25: "sync error in channel C8",
                26: "sync error in channel C9",
                27: "master link delay error",
                28: "Side C enabled",
                29: "delay range error",
                30: "ready bit (31) changes state",
                31: "Side C links OK, ready"
              },
        0x50:{
                -1: "Counters read interval",
                0:  "Counters read interval"
            },
        0x60:{
                -1: "Trigger 5 signature",
                0:  "Trigger 5 signature"
            },
        0x61:{
                -1: "Trigger 5 random rate",
                0:  "Trigger 5 random rate"
            },
        0x62:{
                -1: "Trigger 4 signature",
                0:  "Trigger 4 signature"
            },
        0x63:{
                -1:"Trigger 4 random rate",
                0: "Trigger 4 random rate"
            },
        0x64:{
                -1: "Trigger 2 signature",
                0:  "Trigger 2 siganture"
            },
        0x65:{
                -1: "Trigger 2 random rate",
                0:  "Trigger 2 random rate"
            },
        0x66:{
                -1: "Trigger 1 signature",
                0:  "Trigger 1 signaturee"
            },
        0x67:{
                -1: "Trigger 1 random rate",
                0:  "Trigger 1 random rate"
            },
        0x68:{
                -1: "Trigger 3 signature",
                0:  "Trigger 3 siganture"
            },
        0x69:{
                -1: "Trigger 3 random rate",
                0:  "Trigger 3 random rate"
            },
        0x6A:{
                -1: "Triggers output mode",
                0:  "Trigger 5 output mode",
                2:  "Trigger 5 output enabled",
                3:  "Trigger 4 output mode",
                5:  "Trigger 4 output enabled",
                6:  "Trigger 2 output mode",
                8:  "Trigger 2 output enabled",
                9:  "Trigger 1 output mode",
                11:  "Trigger 1 output enabled",
                12:  "Trigger 3 output mode",
                14:  "Trigger 3 output enabled"

            }



    }
    
    def __init__(self):
        pass
    
    @classmethod
    def get_description(cls, register_number, bit_start):
        output = ""

        if register_number in cls._register_map:

            reg_info = cls._register_map[register_number]
            output += "Register: " + reg_info[-1]

            if bit_start in reg_info:
                output += " | Parameter " + reg_info[bit_start]
            else:
                output += " | Unknown parameter - invalid bit postion"
        else:
            output = "Unknown register address"
        
        return output

    @classmethod
    def describe_transaction(cls, transaction_type, bytes):
        reg_address = 0
        bit_position = 0
        words = cls.bytes_to_words(bytes)
        match transaction_type:
            case 0x0 | 0x2 | 0x6: # Read | Non-incrementing read | Configuration space read
                
            case 0x1 | 0x3 | 0x7 : # Write | Non-incrementing write | Configuration space write
                
            case 0x4: # RMWbits
                return ["Data in BASE_ADDRESS before"]
            case 0x5: # RMWsum
                return ["Data in BASE_ADDRESS before"]
            case _:
                raise ValueError(f"Invalid type ID value 0x{self.type_id:01x} for transaction ID 0x{self.transaction_id:03x}")

    @classmethod
    def bytes_to_words(words):
        for w in range(0, len(words), 4):
            word_bytes = bytes[w:w + 4]
            word = int.from_bytes(word_bytes, byteorder='little')
            yield word
