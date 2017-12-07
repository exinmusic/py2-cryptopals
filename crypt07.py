# AES in ECB mode
import urllib2
from Crypto.Cipher import AES

# Test inputs for cryptopals s1-c7
chlng7 = urllib2.urlopen('https://cryptopals.com/static/challenge-data/7.txt').readlines()
chlng7 = ''.join(chlng7)
chlng7 = chlng7.decode('base64')

# Uses python's Crypto library to decrypt string data
cipher =  AES.new("YELLOW SUBMARINE",AES.MODE_ECB)
print cipher.decrypt(chlng7)