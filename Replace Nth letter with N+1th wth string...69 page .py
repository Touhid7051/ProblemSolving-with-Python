#!/usr/bin/env python
# coding: utf-8

# In[2]:


string=input("A String:")
for i in range(1,len(string),2):
    result=string[i]+string[i-1]
    print(result,end="")
   


# In[ ]:




