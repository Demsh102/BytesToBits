#goes through a list of 8 bits.  Multiplies each 1 by the correct power of 2
#to get the correct byte value
def bitsToBytes(n):
    result = 0
    for i in range (8,0,-1):
        if (n[i-1]==1):
            result = result + 2**(8-i)

    yield result

#Shifts byte one bit to the right
#if the resulting number is even, then the lost right shifted bit was 0
#If not, it was 1.  In this way, the bits of a byte are obtained
def bytesToBits(n):
    res = []
    preShift = n
    while (preShift != 0): 
        postShift = preShift>> 1
        yield preShift%2
        preShift >>= 1
    yield 0

#takes in one word as input
my_str = "TylerDemshki"
#converts string to bytes (couldn't find way to do this without python method)
bytes = str.encode(my_str)
result = []
reverseResult = []
#Goes through all the bytes in the word
#prints it, converts it to an 8 string of bits, and then converts back to bytes
for i in range (0,len(my_str)):
    preShift = bytes[i]
    print('Byte: ', preShift)
    g = bytesToBits(preShift)
    for x in range (0,8):
        result.append(next(g))
    result.reverse()
    print('Bits: ', result)
    f = bitsToBytes(result)
    a = next(f)
    print('Back to Bytes: ', a)
    del result[:]
