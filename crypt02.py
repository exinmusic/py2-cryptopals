# Exclusive OR Hex Combiner

def heXOR(h1, h2):
    d1,d2 = int(h1, 16),int(h2, 16)
    return hex(d1 ^ d2)

# Test inputs for cryptopals s1-c2
#print heXOR('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')[2:][:-1]