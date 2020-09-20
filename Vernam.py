import string
import random
def VernamCipher(plaintext, key):
      result = "";
      ptr = 0;
      for char in plaintext:
            result = result + chr(ord(char) ^ ord(key[ptr]))
            ptr = ptr + 1
            if ptr == len(key): #if the key is smaller than it repeats it
                  ptr = 0
      return result

key = ''
while True:
      plaintext = input("\nEnter Text To Encrypt:\t")
      for i in range(len(plaintext)):
            key = key + random.choice(string.ascii_letters) #key will be different for each iteration
      print('key: ' , key)
      encryption = VernamCipher(plaintext, key)
      print("\nEncrypted Text:\t" + encryption)
      decryption = VernamCipher(encryption, key)
      print("\nDecrypted Text:\t" + decryption)
      key=''
