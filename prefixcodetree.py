# import binhex
# import binascii
# # dont have space between object and value. Ex: dont 'x1': [0]
# codebook = {
#     'x1':[0],
#     'x2':[1,0,0],
#     'x3':[1,0,1],
#     'x4':[1,1]
# }
# class PrefixCodeTree(): 
# #  inside each def have to 'self' params
#     def __init__(self): 
#         self.codebook = [] 
# # Chèn symbol và từ mã symbol
#     def insert(self, codeword, symbol): 
#         self.codebook.append({symbol: codeword})
# # Lấy chiều dài của từ mã
#     def getLen(self, symbol):
#         for sym in self.codebook:
#             for i in sym:
#                 if i==symbol:
#                     return len(sym[i])
# # Tìm trong code xem có từ mã nào ở đầu code không   
#     def search(self, code):
#         for symbol in self.codebook:
#             for i in symbol:
#                 length = len(symbol[i])
#                 firstPartCode = []
#                 for idx in range(length):
#                     firstPartCode.append(int(code[idx]))
#                 if symbol[i] ==firstPartCode:
#                     return str(i)

# # Giải mã
#     def decode(self,encodedData, datalen):
#         hexString = binascii.hexlify(encodedData)
#         h2b = bin(int(hexString, 16))
#         binString = str(h2b).split('b',1)[1]
        
#         x = slice(0,datalen)
#         m=self.search(binString[x])
#         message=m
#         print('bin:', binString[x], datalen)
#         l=self.getLen(m)
#         while l<datalen:
#             _x=slice(l,datalen)
#             _m=self.search(binString[_x])
#             l=l+self.getLen(_m)
#             message=message+_m
#         else:
#             print('message', message)
        

# test = PrefixCodeTree()
# for symbol in codebook:
#     test.insert(codebook[symbol], symbol)
# test.decode(b'\xd7\x1f\x29', 21)

x="00000010000000100000001000001001000000000000000010000010"

print(len(x))
a=0
for i in x:
    if i=='1':
        a=a+1

print(a)
b=[]
u=0
for i in range(int(len(x)/2)):
    r=u
    h=u+2
    d = slice(r,h)
    f=x[d]
    b.append(f)
    u=h

print(b)

for
    
