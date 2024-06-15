def bytes_to_le_word(bytes):
    if len(bytes) % 4 != 0:
        raise ValueError("Length of byte array should be a multiple of 4")
    
    for i in range(0, len(bytes), 4):
        word_bytes = bytes[i:i + 4]
        word = int.from_bytes(word_bytes, byteorder='little')
        yield word