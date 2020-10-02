import binhex
import binascii
# dont have space between object and value. Ex: dont 'x1': [0]
codebook = {
    'x1':[0],
    'x2':[1,0,0],
    'x3':[1,0,1],
    'x4':[1,1]
}
class PrefixCodeTree(): 
#  inside each def have to 'self' params
    def __init__(self): 
        self.codebook = [] 
        self.message = []
          
    def insert(self, codeword, symbol): 
        self.codebook.append({symbol: codeword})

    def getLen(self, symbol):
        for sym in self.codebook:
            for i in sym:
                if i==symbol:
                    return len(sym[i])
        
    def search(self, code):
        if len(code)>=0:
            for symbol in self.codebook:
                for i in symbol:
                    length = len(symbol[i])
                    firstPartCode = []
                    for idx in range(length):
                        firstPartCode.append(int(code[idx]))
                    if symbol[i] ==firstPartCode:
                        return i
        else:
            return 0


    def decode(self,encodedData, datalen):
        hexString = binascii.hexlify(encodedData)
        h2b = bin(int(hexString, 16))
        binString = str(h2b).split('b',1)[1]
        message = []
        x = slice(0,datalen)
        binString = binString[x]

        m=self.search(binString)
        lm1 = 0
        lm2 = 0

        for i in range(0,4):
            lm1 = len(message)
            print('lm1', lm1)
            message.append(m)
            l=self.getLen(m)
            x=slice(l,datalen-l)
            binString = binString[x]
            m=self.search(binString)
            print('m',m)
            lm2 = len(message)
            print('lm2', lm2)

        return message

test = PrefixCodeTree()
for symbol in codebook:
    test.insert(codebook[symbol], symbol)

print(test.decode(b'\xd2\x9f\x20', 21))