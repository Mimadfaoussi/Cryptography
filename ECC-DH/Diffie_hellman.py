import random
#basic DHKE consist of 2 protocols : Set up and main protocol


# 1  -  we start with  Set-up protocol :

# function to check if number is prime

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

# now we back to Set up protocol :
    # 1 -  choosing large prime number p
    # 2 -  choosing integer a from (2 .. p-2 )
    # 3 -  publish p and a  'domain parameters '




#making parameters for alice and bob

P = largestPrime(100)

print("choosed prime number is : ",P)

a = random.randint(2,P-2)

print("choosed a is : ",a)


#after the setup protocol we go for the main protocol

#function for calculate public and private keys for alice and bob

def Alice(P,a):
    prvkey = random.randint(2,P-2)
    pubkey = (a** prvkey )% P
    return (prvkey,pubkey)

def Bob(P,a):
    prvkey = random.randint(2,P-2)
    pubkey = (a** prvkey )% P
    return (prvkey,pubkey)

#establishing public and private key for alice and bob
alice = Alice(P,a)
Bob = Bob(P,a)

prv_Alice = alice[0]
pub_Alice = alice[1]

prv_Bob = Bob[0]
pub_Bob = Bob[1]


# as we see we have the same key in the end  for both alice and Bob
shared_Key_alice = (pub_Bob**prv_Alice)%P
shared_key_bob   = (pub_Alice**prv_Bob)%P


print("------shared keys--------")
print("alice", shared_Key_alice)
print("bob" ,shared_key_bob)