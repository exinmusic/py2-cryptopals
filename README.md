# 🔐 Cryptopals Challenge
### 🐍 in Python 2.7

## Challenge Set 1
- [x] Convert hex to base64
- [x] Fixed XOR
- [x] Single-byte XOR cipher
- [x] Detect single-character XOR
- [x] Implement repeating-key XOR
- [ ] Break repeating-key XOR
- [ ] AES in ECB mode
- [ ] Detect AES in ECB mode

## Last Completed Problem
Set1 Challenge5 - Repeating Key Exclusive Or
```python
def repeatingByteXor(in1, key1):
    chrs = ''
    keyCount = 0
    keyCap = len(key1)-1
    for each_char in in1:
        cipher_out = chr(ord(each_char) ^ ord(key1[keyCount])).encode('hex')
        chrs += cipher_out
        if keyCount < keyCap:
            keyCount += 1
        else:
            keyCount = 0
    return chrs


# Test inputs for cryptopals s1-c5

in1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key1 = 'ICE'
print repeatingByteXor(in1,key1)
```