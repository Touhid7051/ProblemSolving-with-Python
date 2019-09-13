#!/usr/bin/env python
# coding: utf-8

# In[5]:


s=input("Enter a String: ")
pal=s.replace(" ", "")
rev=pal[::-1]

if pal==rev:
    print("Original:",pal,"\n","Reverse: ",rev)
    print("This Is palindrome!")
    
else:
    print("Original:",pal,"\n","Reverse: ",rev)
    print("This is not a Palindrome!")


# In[ ]:




