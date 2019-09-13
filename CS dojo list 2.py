#!/usr/bin/env python
# coding: utf-8

# In[ ]:


g=[5,4,4,3,1]

t=0
i=0
while i<len(g) and g[i]>0:
    t+=g[i]
    i+=1
print(t)


# In[ ]:


j=[5,4,4,3,1,-2,-3,-5]
tot=0
for e in j:
    if e>=0:
        break
    tot+=e
print(tot)


# In[ ]:


j=[5,4,4,3,1,-2,-3,-5]
p=0
i=0
while j[i]<0:
    p+=j[i]
    i+=1
print(p)
        
    


# In[17]:


a = ["apple","banana","republic"]

for i in a:
    print(i)


# In[ ]:




