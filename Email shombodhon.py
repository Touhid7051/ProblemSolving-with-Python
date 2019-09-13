#!/usr/bin/env python
# coding: utf-8

# In[36]:


import turtle
name=turtle.textinput("Name","Whats Your Name?")
name=name.lower()
if name.startswith("mr"):
    print("Dear Sir")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello maam")
else:
    name=name.capitalize()
    str="Hi "+name+"! How are You?"
    print(str)
turtle.exitonclick()
    


# 

# In[ ]:




