#!/usr/bin/env python
# coding: utf-8

# In[6]:


N=int(input())
if N%2!=0:
    print("Weird")
else:
    if N>2 and N<5:
        print("Not Weird")
    elif N>6 and N<=20:
        print("Weird")
    else:
        print("Not Weird")


# In[ ]:



