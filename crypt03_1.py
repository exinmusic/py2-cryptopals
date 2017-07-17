# Single Byte Cipher

def SingleByteXorBrute(in1):
    possible_results = []
    for brute_byte in range(256):
        chrs = ''
        for each_chr in in1:
            cipher_out = chr(ord(each_chr) ^ brute_byte)
            chrs += cipher_out
        possible_results.append(chrs)
    return possible_results