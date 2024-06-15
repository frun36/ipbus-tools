from enum import Enum

class Endianness(Enum):
    BIG = "big"
    LITTLE = "little"

class BaseParam(Enum):
    def __str__(self) -> str:
        return self.name

class PacketType(BaseParam):
    CONTROL = 0x0
    STATUS = 0x1
    RE_SEND = 0x2
    
class TransactionType(BaseParam):
    READ = 0x0
    WRITE = 0x1
    NON_INCREMENTING_READ = 0x2
    NON_INCREMENTING_WRITE = 0x3
    RMW_BITS = 0x4
    RMW_SUM = 0x5
    CONFIGURATION_SPACE_READ = 0x6
    CONFIGURATION_SPACE_WRITE = 0x7

class TransactionInfoCode(BaseParam):
    REQ_HANDLED_OK = 0x0
    BAD_HEADER = 0x1
    BUS_ERROR_ON_READ = 0x4
    BUS_ERROR_ON_WRITE = 0x5
    BUS_TIMEOUT_ON_READ = 0x6
    BUS_TIMEOUT_ON_WRITE = 0x7
    REQUEST = 0xf