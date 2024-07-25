from datetime import datetime
import binascii

types = {
    "read":             "0",
    "write":            "1",
    "non-inc-read":     "2",
    "non-inc-write":    "3",
    "RMWbits":          "4",
    "RMWsum":           "5"
}

class PacketGenerator:
    def __init__(self, file_path):
        self.packetID = 0
        self.sizeWords = 0
        self.transactionsNumber = 0
        self.words = [binascii.unhexlify("200000f0")]  # Fixed the hexadecimal string
        self.filePath = file_path

    def addTransaction(self, type, words, wordsNumber):
        self.words.append(binascii.unhexlify(f"2{self.transactionsNumber:03x}{wordsNumber:02x}{types[type]}f"))
        for word in words:
            self.words.append(binascii.unhexlify(word))
        self.transactionsNumber += 1

    def save(self):
        with open(self.filePath, 'wb') as file:
            for word in self.words:
                file.write(word)


def main():
    now = datetime.now()
    filename = input("Packet name: ")
    packetName = f"packets/{filename}.bin"
    packet = PacketGenerator(packetName)
    while True:
        print("Choose an option: [a] - add transaction [s] - finish and save")
        choice = input("Enter your choice: ").lower()
        match choice:
            case 'a':
                type = input(f"Types: {" ".join(types.keys())}: ")
                wordsNumber = int(input("Words number: "))
                words = input("Words (space-separated, hex format without 0x): ").split()
                packet.addTransaction(type, words, wordsNumber)
                print(f"Transaction of type {type} containing {len(words)} words added")
            case 's':
                print(f"Saving as {packetName}...")
                packet.save()
                break

main()