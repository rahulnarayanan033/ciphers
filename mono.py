from random import shuffle
from string import ascii_letters , digits

plaintext = input("Enter the plaintext:")

comb = ascii_letters + digits
org_comb = list(comb)
print(comb)
shuf_comb = list(comb)
shuffle(shuf_comb)
d=dict(zip(org_comb , shuf_comb))

encrypt=[]
for i in plaintext:
    encrypt.append(d.get(i))
print(''.join(encrypt))

inverse={}
for i,j in d.items():
    inverse[j] = i

decrypt=[]
for i in encrypt:
    decrypt.append(inverse.get(i))
print(''.join(decrypt))




