# 🔐 Cryptopals Challenge
### 🐍 in Python 2.7
[Cryptopals Website](https://cryptopals.com/)

## Challenge Set 1
- [x] Convert hex to base64
- [x] Fixed XOR
- [x] Single-byte XOR cipher
- [x] Detect single-character XOR
- [x] Implement repeating-key XOR
- [x] Break repeating-key XOR
- [ ] AES in ECB mode
- [ ] Detect AES in ECB mode

## Last Completed Problem
Set1 Challenge6 - Break repeating-key XOR
```python
# Break repeating-key XOR
import urllib2
from crypt06_1 import hammingDistance
from crypt03_1 import singleByteXorBrute
from crypt03_2 import englishDetection
from crypt05_more import revRepeatingByteXor

# Chop string into list of equal length chunks
def listChunk(in1,chunk_size):
    return [ in1[i:i+chunk_size] for i in range(0, len(in1), chunk_size) ]

# Calculates 5 most likely key sizes using Hamming distance as a score
def keySizeCalc(in1,loR,hiR):
    scores = []
    top5 = []
    for keySize in range(loR,hiR):
        nList = listChunk(in1,keySize)
        score = 0
        for i in range(1,5):
            score += (float(hammingDistance(nList[0],nList[i]))/float(keySize))
        scores.append((score/4,keySize))
    for i in range(5):
        top5.append(sorted(scores).pop(i))
    return top5

# Breaks a Repeating-key XOR
def breakRepeatingKeyXor(in1,loR,hiR):
    outputs,keys = [],[]
    keySizes = keySizeCalc(in1,loR,hiR)
    for keySize in keySizes:
        keySize = keySize[1]
        chunked = listChunk(in1,keySize)
        blocks,keyLetters = [],[]
        for i in range(keySize):
            blockList=[]
            for chunk in chunked:
                try:
                    blockList.append(chunk[i])
                except:
                    blockList.append('')
            blocks.append(''.join(blockList))
            keyLetters.append(englishDetection(singleByteXorBrute(blocks[i]))[1][1])
        keys.append(''.join(keyLetters))

    for key in keys:
        outputs.append((revRepeatingByteXor(in1,key),key))
    return englishDetection(outputs)

# Test inputs for cryptopals s1-c6 PART 2/2
chlng6 = urllib2.urlopen("https://cryptopals.com/static/challenge-data/6.txt").readlines()
chlng6 = ''.join(chlng6)
chlng6 = chlng6.decode('base64')

# Returns an englishDetection output with key appended, (score,"data string",key)
print breakRepeatingKeyXor(chlng6,2,41)

```