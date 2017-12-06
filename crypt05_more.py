#Reverse Repeating Key Exclusive Or

def revRepeatingByteXor(in1, key1):
    chrs = ''
    keyCount = 0
    keyCap = len(key1)-1
    for each_char in in1:
        cipher_out = chr(ord(each_char) ^ ord(key1[keyCount]))
        chrs += cipher_out
        if keyCount < keyCap:
            keyCount += 1
        else:
            keyCount = 0
    return chrs


# Test inputs for cryptopals s1-c5 EXTRA WORK

#in1 = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
#key1 = 'ICE'

#print revRepeatingByteXor(in1.decode('hex'),key1)