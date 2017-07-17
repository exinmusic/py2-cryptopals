# 🔐 Cryptopals Challenge
### 🐍 in Python 2.7

## Challenge Set 1
- [x] Convert hex to base64
- [x] Fixed XOR
- [x] Single-byte XOR cipher
- [ ] Detect single-character XOR 
- [ ] Implement repeating-key XOR
- [ ] Break repeating-key XOR
- [ ] AES in ECB mode
- [ ] Detect AES in ECB mode

## Last Completed Problem
Set1 Challenge3
```python
from crypt03_1 import SingleByteXorBrute as xorbrute

def englishDetection(s):

    f ={'a': 0.06517,'b': 0.01242,
        'c': 0.02173,'d': 0.03498,
        'e': 0.10414,'f': 0.01979,
        'g': 0.01586,'h': 0.04929,
        'i': 0.05581,'j': 0.00090,
        'k': 0.00505,'l': 0.03315,
        'm': 0.02021,'n': 0.05645,
        'o': 0.05963,'p': 0.01377,
        'q': 0.00086,'r': 0.04976,
        's': 0.05158,'t': 0.07294,
        'u': 0.02251,'v': 0.00829,
        'w': 0.01713,'x': 0.00137,
        'y': 0.01460,'z': 0.00078,
        ' ': 0.19181} # http://www.data-compression.com/english.html

    brute_results,english_results = s,[]

    for each_result in brute_results:
        englishness = 0
        for each_letter in each_result:
            low_letter = each_letter.lower()
            if low_letter in f:
                englishness += f[low_letter]
        rating_combo = (englishness,each_result)
        english_results.append(rating_combo)
    return sorted(english_results)[-10:]

# Test inputs for cryptopals s1-c3 PART 2/2
x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print englishDetection(xorbrute(x.decode('hex')))
```