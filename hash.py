import hashlib
 
# initializing string
str = "HashingTechniques"
 

result = hashlib.md5(str.encode())
 

print("The hexadecimal equivalent of md5 is : ")
print(result.hexdigest())
 
print ("\r")
 
str = "HashingTechniques"
result = hashlib.sha384(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
 
print ("\r")
 

str = "HashingTechniques"
result = hashlib.sha224(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
 
print ("\r")
str = "HashingTechniques"
result = hashlib.sha512(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
 
print ("\r")
 
# initializing string
str = "HashingTechniques"
result = hashlib.sha1(str.encode())
 
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
