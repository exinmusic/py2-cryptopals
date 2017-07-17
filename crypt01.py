# Hex to base64 converter

def hexTo64(h):
    dcode = h.decode('hex').encode('base64')
    return dcode

# Test inputs for cryptopals s1-c1
hexcode = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print hexTo64(hexcode)
