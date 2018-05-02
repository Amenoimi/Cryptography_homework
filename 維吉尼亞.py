import numpy as np
import random
from itertools import combinations
           

 
def StoI(s,key):
    if ord(s)>=ord("a") and ord(s)<=ord("z") :
        b=ord(s)-ord("a")
        b=(b+(ord(key)-ord("a"))) % 26
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


def GAN(s2):
    
    while 1:
        key_len=2
        c=[]
        p1=0
        p2=0
        p3=0

        for j in range(len(s2)):
            if j%key_len==0:
                c.append(ord(s2[j])-ord("a"))
        print("tab：")
        print(c)
        for i in range(26):
            for j in range(26):
                if int(c[0])-int(c[1])==i-j:
                    p1=i
                    p2=j
                    break
      #          if int(c[0])+int(c[1])==i+j:
       #             p1=i
        #            p2=j
         #           break 
                    
        for j in range(26):
            if int(c[0])-int(c[2])==p1-j:
                    p3=j
                    break 
   #         if int(c[0])+int(c[2])==p1+j:
    #                p3=j
     #               break 
                    
        
        
        if c[1]-c[2]==p2-p3:
            print("ANS:"+chr((p1)+ord("a"))+"\t"+chr((p2)+ord("a"))+"\t"+chr((p3)+ord("a"))+"\t")        
            break            
#        if c[1]+c[2]==p2+p3:
 #           print("ANS:"+chr((p1)+ord("a"))+"\t"+chr((p2)+ord("a"))+"\t"+chr((p3)+ord("a"))+"\t")        
  #          break            
        
        print(chr((p1)+ord("a"))+"\t"+chr((p2)+ord("a"))+"\t"+chr((p3)+ord("a"))+"\t")        
                 
    

def BOOM(s2):
    ml=[]
    b=s2
    g=""
    aii='abcdefghijklmnopqrstuvwxyz'
    out=[]
    for h in aii:
         g+=h+" "
    
    f = open('QUQ.txt', 'w', encoding = 'UTF-8')   
    
    for j in range(len(b)):
        ml+=list(combinations(g.split(),j+1))

    for j in range(len(ml)):
        #out.append( QUQ(ml[j],b))
        f.write( QUQ(ml[j],b))
    f.close()
    
    return -1
    
def QUQ(key,ciphertext):

    ascii='abcdefghijklmnopqrstuvwxyz'

    keylen=len(key)

    ctlen=len(ciphertext)

    plaintext = ''

    i = 0

    while i < ctlen:

        j = i % keylen

        k = ascii.index(key[j])

        m = ascii.index(ciphertext[i])

        if m < k:

            m += 26

        plaintext += ascii[m-k]

        i += 1



    return plaintext





mod=int(input("模式(1>加密，2>暴力解密(O(n!))，3>暴力解密(測試)："))

if mod==1:

    q=input("明文：")
    
    key=input("key：")
    out=""
    i=0
    for ans in q:
        if i>(len(key)-1) :
            i=0
        out+=StoI(ans,key[i])
        i=i+1
        
        
        
    print("密文："+out)

elif mod==2:
    q=input("密文：")
    #key=input("key：")
    
    out=""

    #out=BOOM(q)
    #QUQ(key,q)  
    BOOM(q)
    #print(out)


elif mod==3:
    q=input("密文：")
    GAN(q)

