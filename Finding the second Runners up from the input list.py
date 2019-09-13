#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import OrderedDict
ss=[]
n=int(input())
for i in range(n):
    s=input().split()
    ss.append(s)

ss=list(dict.fromkeys(ss))
j=max(ss)
ss.remove(j)
r=max(ss)
print(r)



# ### 
