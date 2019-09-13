#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Run korar age obossoi ekta drive a testfile.txt baniye Location change kore niben


def creat1():
    a=(input("Enter 1st:"))
    file=open("C:/Users/dcL/Desktop/testfile.txt","w") #Ekhane location change korben
    file.write(a)
    file.write(' ')
    file.close()

def creat2():
    b = (input("ENter 2nd"))
    file = open("C:/Users/dcL/Desktop/testfile.txt", "a")
    file.write(b)
    file.close()


def rdandsplt():
    global word
    file = open("C:/Users/dcL/Desktop/testfile.txt","r")
    lines=file.read()
    word=lines.split()
    print(word)
    file.close()

def touhid():
    global newlst
    newlst = list(map(int, word))
    print(newlst)

def add():
    global sum
    sum=0
    for num in newlst:
        sum += num
    print("Sum:",sum)

def putsum():
    stsum=str(sum)
    file = open("C:/Users/dcL/Desktop/testfile.txt", "a")
    file.write("\nSum is:")
    file.write(stsum)
    file.close()

def minus():
    global sub
    sub=newlst[0]-newlst[-1]
    print("Sub:",sub)

def putsub():
    stsub=str(sub)
    file = open("C:/Users/dcL/Desktop/testfile.txt", "a")
    file.write("\nSub is:")
    file.write(stsub)
    file.close()

def mul():
    global mul
    mul=newlst[0]*newlst[-1]
    print("Multiplication:",mul)

def putmul():
    stmul=str(mul)
    file = open("C:/Users/dcL/Desktop/testfile.txt", "a")
    file.write("\nMultiplication is:")
    file.write(stmul)
    file.close()

def div():
    global div
    div=newlst[0]/newlst[-1]
    print("Divission:",div)



def putdiv():
    stdiv=str(div)
    file = open("C:/Users/dcL/Desktop/testfile.txt", "a")
    file.write("\nDivision is:")
    file.write(stdiv)
    file.close()


def result():
    f = open("C:/Users/dcL/Desktop/testfile.txt","r")
    rs=f.read()
    print("\nThe Whole file is:\n")
    print(rs)

try:
    creat1()
    creat2()
    rdandsplt()
    touhid()
    add()
    putsum()
    touhid()
    minus()
    putsub()
    touhid()
    mul()
    putmul()
    touhid()
    div()
    putdiv()
    result()

except:
    print("Please Chose a Valid Path of Your File testfile.txt")

#by_touhid


# In[ ]:




