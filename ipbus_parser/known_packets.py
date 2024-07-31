from enum import Enum
from ipbus_parser.packet import Packet
from ipbus_parser.parameters import PacketType, TransactionType, TransactionInfoCode

class PacketLabel(Enum):
    UNKNOWN = ""
    STATUS = "STATUS"
    TCM_SYNC = "TCM_SYNC"
    PM_V = "PM_V"
    PM_SYNC = "PM_SYNC"
    GBT_ERR_REPORT = "GBT_ERR_REPORT"
    TCM_COUNTERS = "TCM_COUNTERS"
    PM_COUNTERS = "PM_COUNTERS"


class PacketTagger:
    @staticmethod
    def is_status(packet):
        return packet.header.packet_type == PacketType.STATUS.value
    
    @staticmethod
    def is_tcm_sync(packet):
        if len(packet.transactions) != 8:
            return False
        
        # transaction_words = [31, 11, 1, 11, 13, 10, 1, 4] # AGH compatibility mode
        transaction_words = [33, 11, 1, 11, 13, 10, 1, 4]
        transaction_addresses = [0x00, 0x30, 0x50, 0x60, 0xd8, 0xe8, 0xf7, 0xfc]
        for i, transaction in enumerate(packet.transactions):
            if transaction.header.type_id != TransactionType.READ.value:
                return False
            if transaction.header.words != transaction_words[i]:
                return False
            if len(transaction.words) != 1 or transaction.words[0].word != transaction_addresses[i]:
                return False
        return True
        

    @staticmethod
    def is_pm_v(packet):
        if len(packet.transactions) != 1:
            return False
        transaction = packet.transactions[0]
        if transaction.header.type_id != TransactionType.READ.value:
            return False
        if transaction.header.words != 1:
            return False
        if len(transaction.words) != 1 or transaction.words[0].word % 0x0200 != 0x00fe:
            return False
        return True

    @staticmethod
    def is_pm_sync(packet):
        # if len(packet.transactions) != 5: # AGH Compatibility
        #     return False

        if len(packet.transactions) != 6:
            return False
        
        # transaction_words = [126, 64, 13, 1, 4] # AGH Compatibility
        # transaction_addresses = [0x00, 0x7f, 0xd8, 0xf7, 0xfc] # AGH Compatibility
        transaction_words = [126, 64, 13, 10, 1, 4]
        transaction_addresses = [0x00, 0x7f, 0xd8, 0xe8, 0xf7, 0xfc]
        for i, transaction in enumerate(packet.transactions):
            if transaction.header.type_id != TransactionType.READ.value:
                return False
            if transaction.header.words != transaction_words[i]:
                return False
            if len(transaction.words) != 1 or transaction.words[0].word % 0x0200 != transaction_addresses[i]:
                return False
        
        return True

    @staticmethod
    def is_gbt_err_report(packet):
        if len(packet.transactions) != 1:
            return False
        transaction = packet.transactions[0]
        if transaction.header.type_id != TransactionType.NON_INCREMENTING_READ.value:
            return False
        if transaction.header.words != 36:
            return False
        if len(transaction.words) != 1 or transaction.words[0].word % 0x0200 != 0x00f2:
            return False
        return True

    @staticmethod
    def is_tcm_counters(packet):
        if len(packet.transactions) != 1:
            return False
        transaction = packet.transactions[0]
        if transaction.header.type_id != TransactionType.READ.value:
            return False
        if transaction.header.words != 15:
            return False
        if len(transaction.words) != 1 or transaction.words[0].word != 0x0070:
            return False
        return True

    @staticmethod
    def is_pm_counters(packet):
        if len(packet.transactions) != 1:
            return False
        transaction = packet.transactions[0]
        if transaction.header.type_id != TransactionType.READ.value:
            return False
        if transaction.header.words != 24:
            return False
        if len(transaction.words) != 1 or transaction.words[0].word % 0x0200 != 0x00c0:
            return False
        return True

    @staticmethod
    def tag_packet(packet: Packet):
        if PacketTagger.is_status(packet):
            packet.label = PacketLabel.STATUS.value
        elif PacketTagger.is_tcm_sync(packet):
            packet.label = PacketLabel.TCM_SYNC.value
        elif PacketTagger.is_pm_v(packet):
            packet.label = PacketLabel.PM_V.value
        elif PacketTagger.is_pm_sync(packet):
            packet.label = PacketLabel.PM_SYNC.value
        elif PacketTagger.is_gbt_err_report(packet):
            packet.label = PacketLabel.GBT_ERR_REPORT.value
        elif PacketTagger.is_tcm_counters(packet):
            packet.label = PacketLabel.TCM_COUNTERS.value
        elif PacketTagger.is_pm_counters(packet):
            packet.label = PacketLabel.PM_COUNTERS.value
        else:
            packet.label = PacketLabel.UNKNOWN.value
