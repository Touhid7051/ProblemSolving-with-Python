#!/usr/bin/env python
# coding: utf-8

# In[5]:


def prime():
    number=int(input("Enter the possitive number:"))
    if number>1:
        if number==2:
            print("This is a Prime Number")
        for i in range (2,number):
            if number%i==0:
                print("This is Not a Prime Number")
                break
            else:
                print("This is a Prime Number")
                break
    else:
        print("Obviously Not a Prime Number")


# In[6]:


prime()


# In[ ]:





# In[ ]:




