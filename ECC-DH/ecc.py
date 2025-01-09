import random


def isPrime(n):
    if(n>1):
        for i in range(2,n):
            if (n%i == 0):
                return False
        return True
    else :
        return False

# function to get the largest prime from p

def largestPrime(p):
    largest = 0
    for i in range (2,p):
        if isPrime(i):
            largest = i

    if largest == 0 :
        return None
    else :
        return largest


# generating a and b randomly ps : there will be also function where the user is able to chose them by hiself
def generateAB(P):
    a = random.randint(P)
    b = random.randint(P)
    return (a,b)


#test if the curve is valid achived if the discriminant of the curve -16(4a^3 + 27 b² )  != 0

def IsValidCurve(a,b):
    dis = -16*(4*(a**3)+27*(b**2))
    if dis == 0 :
        return False
    else :
        return True


def chooseCurve():
    a = int(input("choose a : "))
    b = int(input("choose b : "))
    if IsValidCurve(a,b):
        return (a,b)
    else :
        return "error"


# in the next function the x[0] represent x1  and x[1] represent x2   same for y1 and y2
def inverse(x,y,P):
    bool = False
    i = 0
    if(x == y):#case where x = y
        while (i<P and bool == False):
            if(((2*x[1]*i)) % P == 1):
                bool = True
            else :
                i = i+1
    else :#case where p!=y
        while (i<P and bool == False):
            if(((y[0]-x[0])*i) % P == 1):
                bool = True
            else :
                i = i+1
    if(bool == True):
        return(i)
    else:
        return(-1)


def addPoint (x,y,P,a):
    if x == (None,None):
        x = y
    if y == (None,None):
        y = x
    i = inverse(x,y,P)
    if i == -1:
        result=(None,None)
    else:
        if(x == y):
            s = (((3*(x[0]**2)+a)%P) * i )%P
        else :
            s = ((y[1]-x[1]) * i )%P
        #print(s)
        x3 = (s**2)-x[0]-y[0]
        x3 = x3%P
        y3 = s*(x[0]-x3)-x[1]
        y3 = y3%P
        result = (x3,y3)
    return (result)

def onCurve(x,P,a,b):
    rs1 = (x[1]**2)%P
    rs2 = (x[0]**3 + a*x[0] + b) % P
    print("y = ",rs1)
    print("rest of equation = ",rs2)

    if rs1 == rs2 :
        return True
    else :
        return False


#calculating P + 2P + 3P .... until finding the neutral element after  adding P to it"s inverse -p

def multCurve(x,R,P,a):#this one to find inverse and neutral element
    i = 2
    print ("1P = ",R)
    while(R != (None,None)):
        R = addPoint(x,R,P,a)
        print(i,"P = ",R)
        i = i+1
    print("the ",i-1,"element is the neutral element and the ",i-2,"P is inverse  and the next element will represent P ")


def multiple(x,R,P,a,prv):#this one is to do multiple
    for i in range (prv):
        R = addPoint(x,R,P,a)
        #print(R)
    #print(R)
    return R


#from here we will implement ECDH protocol

# 1 choosing the prime P and the elliptic curve (we already made function for both of them)

#2 choosing  a primitive element X=(xp,yp)

#  #1 and #2     are  the domain parameters








P = largestPrime(100) #this will generaate  largest prime from number introduced
#P = 17 # ann example

print("choosed prime number is : ",P)

curve = (2,2)

print("our curve is :  Y^2 = X^3 - ",curve[0],"X + ",curve[1])

x = (5,1)
y = (5,1)

class user :

    prv = None
    pub = None
    secretkey = None


alice = user()
bob = user()


#choosing their private keys a from {2 - #E - 1}

alice.prv = random.randint(2,P-1)
bob.prv = random.randint(2,P-1)

print("alice private key is : ",alice.prv)
print("bob private key is : " ,bob.prv)
#computing the public keys for both alice and bob   Kpub = aX = prv*X = point on curve we suppose that our point is x = (5,1)

R = (5,1) # to test the example


#calculating public keys for alice and bob
alice.pub = multiple(x,R,P,curve[0],alice.prv)
bob.pub = multiple(x,R,P,curve[0],bob.prv)

print("alice public key is :",alice.pub)
print("bob public key is :  ",bob.pub)



#after generating each one's public and private key we have now to establish the shared  secret key
alice.secretkey = multiple(R,bob.pub,P,curve[0],alice.prv)
bob.secretkey = multiple(R,alice.pub,P,curve[0],bob.prv)

print("the secret shared key for alice is :",alice.secretkey)
print("the secret shared key for bob is :",bob.secretkey)






#R = addPoint(x,y,P,curve[0])

#print(R)


# for i in range (50):
#     R = addPoint(x,R,P,curve[0])
#     print(R)


#multCurve(x,R,P,curve[0])
#print("checking if it's on curve : ")

#oncurve = onCurve(R,P,curve[0],curve[1])

#print(oncurve)
# a = IsValidCurve(3,3)
# print(a)