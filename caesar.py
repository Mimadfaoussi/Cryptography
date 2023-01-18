def xalpha(char) :
    alpha = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for x in alpha : 
        if x == char : 
            return count
        count += 1


def encode(text,key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for char in text : 
        if(char.isalpha()):
            case = 0
            if(char.isupper()):
                case = 1
            newchar = xalpha(char.lower()) + key 
            if(newchar > 25 ):
                newchar = newchar % 25 - 1
            if(case == 1):
                cipher = cipher + alpha[newchar].upper()
            else : 
                cipher = cipher + alpha[newchar]
        else :
            cipher = cipher + char 
    return (cipher)

def decode(cipher,key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    text = ""
    for char in cipher : 
        if(char.isalpha()):
            case = 0
            if(char.isupper()):
                case = 1
            newchar = xalpha(char.lower()) - key 
            if(newchar < 0 ):
                newchar = newchar + 26
            if(case == 1):
                text = text + alpha[newchar].upper()
            else : 
                text = text + alpha[newchar]
        else :
            text = text + char 
    return (text)

def bruteforce(cipher):
    key = 0
    plaintext = []
    while(key <= 25):
        text = decode(cipher,key)
        plaintext.append(text)
        key += 1 
    return plaintext

def show_bruteforce(ma_list):
    key = 1
    for x in ma_list : 
        print(f"key = {key}  plaintext = {x}")
        key +=1

def root13(plaintext):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""
    for char in plaintext : 
        if(char.isalpha()):
            case = 0
            if(char.isupper()):
                case = 1
            newchar = xalpha(char.lower()) + 13 
            if(newchar > 25 ):
                newchar = newchar % 25 - 1
            if(case == 1):
                cipher = cipher + alpha[newchar].upper()
            else : 
                cipher = cipher + alpha[newchar]
        else :
            cipher = cipher + char 
    return (cipher)


text = "this is my text FOR ABCD  Aencryption"
key = 5

print(root13(text))
#x = bruteforce(encode(text,key))
# show_bruteforce(x)