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
- [x] AES in ECB mode
- [x] Detect AES in ECB mode

## Last Completed Problem
Set1 Challenge8 - Detect AES in ECB mode
```python
# AES in ECB mode
import urllib2
import collections
from crypt06_2 import listChunk

def ecbSence(in1):
	chunkedLists,scores,ecbDetected = [],[],[]
	for eachLine in in1:
		chunkedLists.append(listChunk(eachLine,16))
	for eachList in chunkedLists:
		if collections.Counter(eachList).most_common(1)[0][1] > 1:
			scores.append(collections.Counter(eachList).most_common(1)[0])
	for score in scores:
		for eachLine in in1:
			if score[0] in eachLine:
				ecbDetected.append((eachLine))
	return ecbDetected
# Test inputs for cryptopals s1-c8
chlng8 = urllib2.urlopen('https://cryptopals.com/static/challenge-data/8.txt').readlines()
print ecbSence(chlng8)
```

## Set 1 Writeups
### Challenge 1 - Convert hex to base64
Hex to base64 can be done a number of ways in Python. Importing libraries will be reasonably avoided in these challenges, so this is solved using the string encode/decode function. 
```python
def hexTo64(h):
    dcode = h.decode('hex').encode('base64')
    return dcode
```
### Challenge 2 - Fixed XOR
The follow strings simply need to get coverted to base 16 `'1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965'` and the exlusive or function `^` is used to on the two results.
```python
def heXOR(h1, h2):
    d1,d2 = int(h1, 16),int(h2, 16)
    return hex(d1 ^ d2)
```
### Challenge 3 - Single-byte XOR cipher
While not entirely necessary, I chose to solve this challenge in two parts. We are provided with this string `1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736` and the knowledge that it's to be XOR'd against a single character to break the cipher. The message that is encoded is mentioned to be in english.
The first step was defining the single byte XOR brute force in crypt03_1. The following function returns a list of 256 strings, one for every possible ASCII character XOR's against each character in the input string.
```python
def singleByteXorBrute(in1):
    possible_results = []
    for brute_byte in range(256):
        chrs = ''
        for each_chr in in1:
            cipher_out = chr(ord(each_chr) ^ brute_byte)
            chrs += cipher_out
        possible_results.append((chrs,chr(brute_byte)))
    return possible_results
```
While a list of 256 strings isn't impossible to sift through for the one english string, it's encouraged to automate.
In crypt03_2 the english detection function is defined using character frequency statistics from http://www.data-compression.com/english.html to score each string in the input list.
```python
 f={'a': 0.06517,'b': 0.01242,
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
    ' ': 0.19181}
```
The following function takes a list of strings and returns one string with the higest "english score".
```python
def englishDetection(s):
    brute_results,english_results = s,[]
    for each_result in brute_results:
        englishness = 0
        for each_letter in each_result[0]:
            low_letter = each_letter.lower()
            if low_letter in f:
                englishness += f[low_letter]
        rating_combo = (englishness,each_result)
        english_results.append(rating_combo)
    return max(english_results)
```
### Challenge 4 - Detect single-character XOR
Detecting a string that's been single character XOR'd from a list takes the previous challenge's defined functions and interates them over a list of strings.
```python
def xorEngHandler(in1):
    decrypted_lists = []
    rated_list = []
    for each_line in in1:
        decrypted_lists.append(xorbrute(each_line.decode('hex')))
    for  each_list in decrypted_lists:
        rated_list.append(engdetec(each_list))
    return max(rated_list)
```
### Challenge 5 - Implement repeating-key XOR
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
```
### Challenge 6 - Break repeating-key XOR
Took this one in two parts. Part one was creating a function that calculated hamming distance.
```python
def hammingDistance(in1,in2):
    dist_count = 0
    pairedIns = zip(bytearray(in1),bytearray(in2))
    for each_1,each_2 in pairedIns:
        dist_count += bin(each_1^each_2).count('1')
    return dist_count
```
In the second part, two more funcitons get defined. hammingDistance, listChuck, and keySizeCalc are all then applied in the breakRepeatingKeyXor funciton.
```python 
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
```
### Challenge 7 - AES in ECB mode
AES encryption is quite easy in Python due to all its libraries, and for this challenge using a library seemed encouraged.
```python
import urllib2
from Crypto.Cipher import AES

# Test inputs for cryptopals s1-c7
chlng7 = urllib2.urlopen('https://cryptopals.com/static/challenge-data/7.txt').readlines()
chlng7 = ''.join(chlng7)
chlng7 = chlng7.decode('base64')

# Uses python's Crypto library to decrypt string data
cipher =  AES.new("YELLOW SUBMARINE",AES.MODE_ECB)
print cipher.decrypt(chlng7)
```
### Challenge 8 - Detect AES in ECB mode
Detecting AES in "electronic code book" can be as simple as finding key sized repeats in the encrypted text. This function outputs a list of imputs that have repeating keysized segments in them.
```python
def ecbSence(in1):
	chunkedLists,scores,ecbDetected = [],[],[]
	for eachLine in in1:
		chunkedLists.append(listChunk(eachLine,16))
	for eachList in chunkedLists:
		if collections.Counter(eachList).most_common(1)[0][1] > 1:
			scores.append(collections.Counter(eachList).most_common(1)[0])
	for score in scores:
		for eachLine in in1:
			if score[0] in eachLine:
				ecbDetected.append((eachLine))
	return ecbDetected
```