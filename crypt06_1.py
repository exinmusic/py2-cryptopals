# Hamming Distance Function for s1c6

def hammingDistance(in1,in2):
    dist_count = 0
    pairedIns = zip(bytearray(in1),bytearray(in2))
    for each_1,each_2 in pairedIns:
        dist_count += bin(each_1^each_2).count('1')
    return dist_count


# Test inputs for cryptopals s1-c6 PART 1/2

#x = 'this is a test'
#y = 'wokka wokka!!!'

#print hammingDistance(x,y)