import numpy as np
plaintext = input("Enter the plaintext:")
key = input("Enter the key:")
letters = 'abcdefghiklmnopqrstuvwxyz'

plaintext = plaintext.lower()
plaintext = plaintext.replace(" ","")
key = key.lower()
key = key.replace(" ","")

print('The plaintext is: ' , plaintext)
print('The key is: ' , key)

plaintext = plaintext.replace('j','i')

matrix=[]
for i in range(5):
    matrix.append([])

ptr=0

#creating key matrix
for j in key:
    res1 = j in (item for submatrix in matrix for item in submatrix)
    if res1 == False:
        matrix[ptr].append(j)
        if len(matrix[ptr]) == 5:
            ptr+=1
for i in letters:
    res2 = i in (item for submatrix in matrix for item in submatrix)
    if len(matrix[ptr]) == 5:
        ptr+=1
    if res2==False:
        matrix[ptr].append(i)

#diagraph = np.array(matrix)
print(" The key matrix is: \n",np.array(matrix))


#encryption
text=list(plaintext)
if len(text)%2!=0:   #add a letter if length is an odd number
    text.append('z')

j=1
k=0
c=0
cipherText=''
for i in range(len(text)):
    if j==len(text)+1:
        break
    a=[(index, row.index(text[k])) for index, row in enumerate(matrix) if text[k] in row] #searhes for the character in matrix
    b=[(index, row.index(text[j])) for index, row in enumerate(matrix) if text[j] in row]
    a=list(a[0])
    b=list(b[0])

    #encrypts the text according the conditions
    if a[0] == b[0]:
        if a[1] == 4:
            a[1] = 0
        else:
            a[1] = a[1] + 1
            
        if b[1] == 4:
            b[1] = 0
        else:
            b[1] = b[1] + 1
        v=a[0]
        w=a[1]
        x=b[0]
        y=b[1]
        cipherText = cipherText + matrix[v][w] + matrix[x][y]
    elif a[1] == b[1]:
        if a[0] == 4:
            a[0] = 0
        else:
            a[0] = a[0] + 1
        if b[0] == 4:
            b[0] = 0
        else:
            b[0] = b[0] + 1
        v=a[0]
        w=a[1]
        x=b[0]
        y=b[1]
        cipherText = cipherText + matrix[v][w] + matrix[x][y]
    else:
        t=0
        t=a[1]
        a[1]=b[1]
        b[1] = t
        v=a[0]
        w=a[1]
        x=b[0]
        y=b[1]
        cipherText = cipherText + matrix[v][w] + matrix[x][y]       
    k=k+2
    j=j+2


print("The encrypted text is: ",cipherText)


#decryption
text=list(cipherText)
if len(text)%2!=0:   #add a letter if length is an odd number
    text.append('z')

k=0
j=1
decipher=''
for i in range(len(text)):
    if j==len(text)+1:
        break
    a=[(index, row.index(text[k])) for index, row in enumerate(matrix) if text[k] in row] #searhes for the character in matrix
    b=[(index, row.index(text[j])) for index, row in enumerate(matrix) if text[j] in row]
    a=list(a[0])
    b=list(b[0])
    
    #decrypts the ciphertext according the conditions
    if a[0] == b[0]:
        if a[1] == 0:
            a[1] = 4
        else:
            a[1] = a[1] - 1
            
        if b[1] == 0:
            b[1] = 4
        else:
            b[1] = b[1] - 1
        v=a[0]
        w=a[1]
        x=b[0]
        y=b[1]
        decipher = decipher + matrix[v][w] + matrix[x][y]
    elif a[1] == b[1]:
        if a[0] == 0:
            a[0] = 4
        else:
            a[0] = a[0] - 1
        if b[0] == 0:
            b[0] = 4
        else:
            b[0] = b[0] - 1
        v=a[0]
        w=a[1]
        x=b[0]
        y=b[1]
        decipher = decipher + matrix[v][w] + matrix[x][y]
    else:
        t=0
        t=a[1]
        a[1]=b[1]
        b[1] = t
        v=a[0]
        w=a[1]
        x=b[0]
        y=b[1]
        decipher = decipher + matrix[v][w] + matrix[x][y]        
    k=k+2
    j=j+2

print("The decrypted text is: ",decipher)



