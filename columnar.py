import math
import numpy as np
message = input('Enter the message:')
key = input('Enter the key:')
cols = len(key) #length of the column
letters = 'abcdefghiklmnopqrstuvwxyz'

rows = math.ceil((len(message)/cols)) #number of rows
matrix=[]

#creating empty matrix
for i in range(rows):
    matrix.append([])

ptr=0
for j in message:
    matrix[ptr].append(j)
    if len(matrix[ptr]) == cols:
        ptr+=1
ptr=rows-1
print('m:',matrix)
for i in letters:
    res = i in (item for submatrix in matrix for item in submatrix)
    if res==False:
        matrix[ptr].append(i) 
    if len(matrix[ptr]) == cols:
        break
print('matrix:',np.array(matrix))

#encryption
k=[]
for i in key:
    k.append(int(i)-1)
ciphertext=''
#reading the data column wise
dit = {k[j] : [matrix[i][j]for i in range(len(matrix))]for j in range(len(k))} 
d=dit.items()
keys = sorted(d)
keys = dict(keys)
for i in keys.values():
    text = ''.join(i)
    ciphertext = ciphertext + text
print(ciphertext)

#decryption
dec_row=math.ceil((len(ciphertext)/cols))
decrypt=[]
plaintext=''
#creating empty matrix
for i in range(dec_row):
    decrypt.append([])
    for j in range(cols):
        decrypt[i].append(0)
k_ind=0
c_ind=0
cipher = list(ciphertext)
key_lst=sorted(k)
print('k:',key_lst)
#inserting the data columnwise
for i in range(cols):
    p_ind = k.index(key_lst[k_ind])
    for j in range(dec_row):
        decrypt[j][p_ind] = cipher[c_ind]
        c_ind+=1
    k_ind+=1

#reading the data
for i in decrypt:
    text=''.join(i)
    plaintext = plaintext + text
print(plaintext)



