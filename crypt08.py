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