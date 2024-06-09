import random
import string

if __name__=="__main__":
    p1=string.ascii_lowercase
    p2=string.ascii_uppercase
    p3=string.digits
    p4=string.punctuation
    n=int(input("Enter the Password Length : "))
    s=[]
    s.extend(list(p1))
    s.extend(list(p2))
    s.extend(list(p3))
    s.extend(list(p4))
    print("Your PASSWORD:",end=" ")
    print("".join(random.sample(s,n)))
