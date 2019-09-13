#!/usr/bin/env python
# coding: utf-8

# In[3]:


class car:
    name=""
    color=""
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def prnt(self):
        print(self.name)
        print(self.color)
    
    def start(self):
        print(self.name,"car is starting")
        
        
if __name__=='__main__':
        
    blue=car("toyota","blue")
    red=car("Marcedes","red")
    blue.prnt()
    red.prnt()
    red.start()
    blue.start()


# In[ ]:


class My:
    k=""
    
    def __init__(self,k):
        self.n=k
    def prnt(self):
        print("My Name is ",self.n)
        
new=My("ashid")

new.prnt()


# In[ ]:


class User:
    name = ""
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        print ("Hello, my name is " + self.name)
# create virtual objects
james = User("James")
david = User("David")
eric = User("Eric")
# call methods owned by virtual objects
james.sayHello()
david.sayHello()


# In[ ]:


print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")


# In[2]:


class car:
    name="premio"
    color="white"
    
    def start(self):
        print("start")
pre=car()
pre.start()
pre.name="ht"
print(pre.name)


# In[ ]:




