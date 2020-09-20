text = input("What is your plaintext? ")
rail = int(input("Number of rails: "))
plaintext = text.lower() #can also done with upper case
#ENCRYPTION
encrypt=[]
for i in range(rail):
    encrypt.append([])
    for j in range(len(plaintext)):
        encrypt[i].append(0)
boolean = False
i = 0
for j in range(len(plaintext)):
    encrypt[i][j] = plaintext[j]
    #for going top and bottom
    if(i==0) or (i==rail-1):  
        boolean = not boolean
    if boolean:
        i = i + 1
    else:
        i = i - 1
print('The encrypted text is:' , end='')
for i in range(rail):
    for j in range(len(plaintext)):
        if(encrypt[i][j]!=0):
            print(encrypt[i][j] , end='')
print('\n')

#DECRYPTION
n=len(encrypt[0])*len(encrypt)
decrypt=[0]*n
dec=[]
boolean = False
i=0
for j in range(len(encrypt[0])):
    decrypt[i] = encrypt[i][j]
    dec.append(decrypt[i])
    if(i==0) or (i==rail-1):
        boolean = not boolean
    if boolean:
        i = i + 1
    else:
        i = i - 1
print('The decrypted text is:' , end='')
for i in range(len(dec)):
    print(dec[i],end='')


    

        
