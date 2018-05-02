import numpy as np
import random

import nltk

from nltk.corpus import wordnet

 
def StoI(s,key):
    if ord(s)>=ord("a") and ord(s)<=ord("z") :
        b=ord(s)-ord("a")
        b=(b+key) % 26
        c=b+ord("a")
        return chr(c)
    else :
        return s

def ItoS(s,key):
    if ord(s)>=ord("a") and ord(s)<=ord("z") :
        b=ord(s)-ord("a")
        b=(b-key) % 26
        c=b+ord("a")
        return chr(c)
    else :
        return s

#def BOOM(s1,s2):
def BOOM(s2):
    b=s2
    c=""

    for key in range(26):
        c=""
        for i in range(len(s2)):
            c+=ItoS(b[i],key)


        print("key："+str(key)+"\t猜測明文:"+c)
        
        #if c==s1 :
         #   return "明文:"+c+"\nkey:"+str(key)

            
def bigBOOM(s2):
    
    nltk.download('wordnet')
    nltk.download('punkt')
    
    b=s2
    c=""

    for key in range(26):
        c=""
        for i in range(len(s2)):
            c+=ItoS(b[i],key)
        dd=nltk.word_tokenize(c)
        #print(type(dd))
        cs=0
        for i in dd:
            if wordnet.synsets(i):
               cs=cs+0         
            else :
                cs=cs+1

        if cs>0:
            print("key："+str(key)+"\t猜測明文:"+c)
        
        else:
            print("key："+str(key)+"\t較肯定猜測明文:"+c)
       
        
        #if not wordnet.synsets(c):
         # print("key："+str(key)+"\t猜測明文:"+c)
        
        #else:
         # print("key："+str(key)+"\t較肯定猜測明文:"+c)

        #if c==s1 :
         #   return "明文:"+c+"\nkey:"+str(key)

    

    


mod=int(input("模式(1>加密，2>解密，3>破密，4>破密(nltk))："))

if mod==1:

    q=input("明文：")
    
    #key=int(input("key："))
    key=random.randint(0,25)
    print("key："+str(key))
    out=""

    for ans in q:
        out+=StoI(ans,key)
        
        
    print(out)

elif mod==2:
    q=input("密文：")
    key=int(input("key："))
    out=""

    for ans in q:
        out+=ItoS(ans,key)
        
        
    print(out)

elif mod==3 :
    #q1=input("明文：")
    q2=input("密文：")
        
        
    #print(BOOM(q1,q2))
    print(BOOM(q2))
else :
    #q1=input("明文：")
    q2=input("密文：")
        
        
    #print(BOOM(q1,q2))
    print(bigBOOM(q2))




