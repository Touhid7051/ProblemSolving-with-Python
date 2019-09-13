#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input())
b=int(input())
c=int(input())
if a < b and b > c:
    if a<c:
        print(a,c,b)
        
    else:
        print(c,a,b)
        
if b < a and a > c:
    if b<c:
        print(b,c,a)
    else:
        print(c,b,a)
        
if a < c and c>b:
    if a<b:
        print(a,b,c)
    else:
        print(b,a,c)
print()
print(a,b,c)

        
    


# In[ ]:





# In[ ]:




