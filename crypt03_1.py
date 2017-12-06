# Single Byte Cipher

def singleByteXorBrute(in1):
    possible_results = []
    for brute_byte in range(256):
        chrs = ''
        for each_chr in in1:
            cipher_out = chr(ord(each_chr) ^ brute_byte)
            chrs += cipher_out
        possible_results.append((chrs,chr(brute_byte)))
    return possible_results

# Test inputs for cryptopals s1-c3 PART 1/2
#x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print singleByteXorBrute(x.decode('hex'))