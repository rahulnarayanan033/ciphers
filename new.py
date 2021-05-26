import random
plaintext = input("Enter the plaintext:")
plaintext=plaintext.lower()
plaintext = plaintext.replace(' ','') #removes all the spaces
characters = 'abcdefghijklmnopqrstuvwxyz@.,?0123456789'
ef=''

#key generation
for i in range(len(plaintext)): #shifting the plaintext by random number
    shift = random.randrange(1 , 100)
    index = characters.index(plaintext[i])
    crypt = (index + shift)%40
    ef = ef + characters[crypt]
key=''
for char in range(len(plaintext)):
    r = (characters.index(plaintext[char]) ^ characters.index(ef[char]))%40 #xoring the key with plaintext
    key = key + characters[r]

print('key:',key)

#encryption
s=len(plaintext) + len(key)
n=random.randrange(1,s)
cipherText = ""
for i in range(len(plaintext)):
    if i%2==0: #adding plaintext with key on even position
        res = (characters.index(plaintext[i]) + characters.index(key[i]))%40
        cipherText = cipherText + characters[res]
    else: #subtracting plaintext with key and adding a random number
        index = characters.index(plaintext[i])
        crypt = (index - characters.index(key[i]) + n)%40
        cipherText = cipherText + characters[crypt]
        
print('Encrypted text:',cipherText)

#decryption
text = ""
for j in range(len(cipherText)):
    if j%2==0:
        res = (characters.index(cipherText[j]) - characters.index(key[j]))%40
        text = text + characters[res]
    else:
        res=(characters.index(cipherText[j]) + characters.index(key[j]) - n)%40
        text=text+characters[res]

print()
print('Decrypted text:',text)

