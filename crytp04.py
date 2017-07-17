from crypt03_2 import englishDetection as engdetec
from crypt03_1 import SingleByteXorBrute as xorbrute
import urllib2


# Test inputs for cryptopals s1-c4
crypto = urllib2.urlopen("https://cryptopals.com/static/challenge-data/4.txt").read()
x = crypto
print engdetec(xorbrute(crypto))