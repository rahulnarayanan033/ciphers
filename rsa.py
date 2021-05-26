import random
def checkPrime(num):
    if num>1:
        for i in range(2 , num):
            if(num % i)==0:
                return False
        else:
            return True
    else:
        return False

def gcd(e,phi):
    while(phi):
        e , phi = phi , e%phi
    return e

def mulInv(e,phi):
    for i in range(1,phi):
        if((e*i)%phi == 1):
            return i
    return 1

p = int(input("Enter any prime number:"))
q = int(input("Enter any prime number:"))
if(not(checkPrime(p) and checkPrime(q))):
    raise ValueError('Both numbers must be prime')
elif p==q:
    raise ValueError('p and q caonnot be equal')

n=p*q
p1=p-1
q1=q-1
phi=p1 * q1

e = random.randrange(1,phi)
g = gcd(e,phi)
while g!=1:
    e=random.randrange(1,phi)
    g=gcd(e,phi)

d=mulInv(e,phi)
pub_key=(e,n)
priv_key=(d,n)

print('The public key is:',pub_key)
print('The private key is:',priv_key)

msg = input("Enter a message:")
cp=0
#encryption
e,n = pub_key
cip=[]
m=0
for i in msg:
    m=ord(i)-97
    c=(m**e)%n
    cip.append(c)
print('The ecnrypted data is:',cip)

#decryption
d,n = priv_key
plain=''
for i in cip:
    m=(int(i)**d)%n
    m+=97
    c=chr(m)
    plain+=c
print('The decrypted data is:',plain)
    
