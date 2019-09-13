#!/usr/bin/env python
# coding: utf-8

# In[12]:


import re

str=input("enter:")
up=''
low=''
n=''
e=''


for i in str:
    if i.isupper():
        up=up+i

    if i.islower():
        low=low+i
    if i.isnumeric():
        n=n+i
    if i == re.compile('[@_!#$%^&*()<>?/\|}{~:]'):
        e+=i
        
        
print(up)
print(low)
print(n)
print(e)
    


# In[ ]:





# In[ ]:





# In[ ]:




