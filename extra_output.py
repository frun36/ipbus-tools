from ipbus_parser.transaction import Transaction, TransactionWord
from register_map import RegisterMap
from enum import Enum

class DisplayMode(Enum):
    FULL = 0
    OMIT_REGISTERS_DESC = 1
    MINIMAL = 2

class ExtraOutput:
    @classmethod
    def transaction_word(cls, mode, trans_word: TransactionWord, type, infoCode):
        if infoCode != 0xf:
            return None        
        match mode:
            case 0:
                match type:
                    case 0x0 | 0x2 | 0x6: # Read | Non-incrementing read | Configuration space read
                        return RegisterMap.describe_read(trans_word.word)
                    case 0x1 | 0x3 | 0x7 : # Write | Non-incrementing write | Configuration space write
                        return RegisterMap.describe_write(trans_word.word)
                    case 0x4: # RMWbits
                        return None
                    case 0x5: # RMWsum
                        return None

    @classmethod
    def transaction(cls, mode, transaction: Transaction):
        if transaction.header.info_code != 0xf:
            return None 
        match mode:
            case 0:
                match transaction.header.type_id:
                    case 0x0 | 0x2 | 0x6: # Read | Non-incrementing read | Configuration space read
                        return None
                    case 0x1 | 0x3 | 0x7 : # Write | Non-incrementing write | Configuration space write
                        return None
                    case 0x4: # RMWbits
                        words = []
                        for w in transaction.words:
                            words.append(w.word)
                        return RegisterMap.describe_RMWbits(words)
                    case 0x5: # RMWsum
                        for w in transaction.words:
                            words.append(w.word)
                        return RegisterMap.describe_RMWsum(words)