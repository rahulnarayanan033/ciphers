plaintext = input("What is your plain text?")
keyword = input("Enter the keyword: ")
letters = 'abcdefghijklmnopqrstuvwxyz'

plaintext = plaintext.lower()
keyword = keyword.lower()
length = len(plaintext)
plaintext = "".join(plaintext.split())
print("Plaintext is: ",plaintext)

for i in plaintext:
    if(i not in letters):
        print('plaintext should be only characters')
        break
else:
    keyword = list(keyword)
    if(len(keyword) == len(plaintext)):
        keyword = keyword
    else:
        for i in range(len(plaintext) - len(keyword)):
            keyword.append(keyword[i])

    res=0
    #encryption
    cipherText = ''
    for i in range(len(plaintext)):
        res = (letters.index(plaintext[i]) + letters.index(keyword[i]))%26
        cipherText = cipherText + letters[res]
    print('Encrypted text: ',cipherText)

    #decryption
    res=0
    text=''
    for i in range(len(cipherText)):
        res = (letters.index(cipherText[i]) - letters.index(keyword[i]))%26
        text = text + letters[res]
    print('Decrypted text: ' , text)


        
