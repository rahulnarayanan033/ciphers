plaintext = input("What is your plain text?")
autokey = input("Enter the autokey: ")

plaintext = plaintext.lower()
autokey = autokey.lower()

for i in plaintext:
    key=[]
    for i in autokey:
        key.append(i)

    n = len(plaintext) - len(key)
    for i in range(0 , n):
        key.append(plaintext[i])

    keystream = ''
    keystream = keystream.join(key)
print('keystream is: ' , keystream)

res=0
#encryption
cipherText = ''
for i in range(len(plaintext)):
    print((ord(plaintext[i]) + ord(keystream[i]))%26)
    cipherText = cipherText + chr(((ord(plaintext[i]) + ord(keystream[i])) -97)%26 + 97)
print('Encrypted text: ',cipherText)

#decryption
res=0
text=''
for i in range(len(cipherText)):
    text = text + chr(((ord(cipherText[i]) - ord(keystream[i])) -97)%26 + 97)
print('Decrypted text: ' , text)


        
