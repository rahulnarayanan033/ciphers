plaintext = input("What is your plain text?")
autokey = input("Enter the autokey: ")
letters = 'abcdefghijklmnopqrstuvwxyz'

plaintext = plaintext.lower()
autokey = autokey.lower()

plaintext = "".join(plaintext.split())
print("Plaintext is: ",plaintext)

for i in plaintext:
    if(i not in letters):
        print('plaintext should be only characters')
        break
else:
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
        res = (letters.index(plaintext[i]) + letters.index(keystream[i]))%26
        cipherText = cipherText + letters[res]
    print('Encrypted text: ',cipherText)

    #decryption
    res=0
    text=''
    for i in range(len(cipherText)):
        res = (letters.index(cipherText[i]) - letters.index(keystream[i]))%26
        text = text + letters[res]
    print('Decrypted text: ' , text)


        
