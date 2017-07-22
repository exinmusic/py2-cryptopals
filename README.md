# 🔐 Cryptopals Challenge
### 🐍 in Python 2.7

## Challenge Set 1
- [x] Convert hex to base64
- [x] Fixed XOR
- [x] Single-byte XOR cipher
- [x] Detect single-character XOR
- [ ] Implement repeating-key XOR
- [ ] Break repeating-key XOR
- [ ] AES in ECB mode
- [ ] Detect AES in ECB mode

## Last Completed Problem
Set1 Challenge4
```python
from crypt03_2 import englishDetection as engdetec
from crypt03_1 import SingleByteXorBrute as xorbrute
import urllib2

def xorEngHandler(loh):
    decrypted_lists = []
    rated_list = []
    for each_line in loh:
        decrypted_lists.append(xorbrute(each_line.decode('hex')))
    for  each_list in decrypted_lists:
        rated_list.append(engdetec(each_list))
    return max(rated_list)

# Test inputs for cryptopals s1-c4
cryptos = urllib2.urlopen("https://cryptopals.com/static/challenge-data/4.txt").readlines()
cryptos = [x.strip('\n') for x in cryptos]
print xorEngHandler(cryptos)
```