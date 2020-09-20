import string
plainText =input("What is your plaintext? ")
plaintext=plainText.lower() #FOR UPPER THE FORMULA CHANGES WITH 65
print(plaintext)

n=int(input("enter the shift: "))
cipherText=""
for i in plaintext:
    if(ord(i)==32):
        cipherText = cipherText + ' '
    else:
        cipherText=cipherText+chr((ord(i)-n-97)%26 + 97)
plaintext=""

for j in cipherText:
    plaintext=plaintext+chr(ord(j)-n)


print("Encryption=",cipherText)
print("Decryption=",plainText)
