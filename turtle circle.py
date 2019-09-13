#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
def square(sl):
    for i in range(4):
        turtle.forward(sl)
        turtle.left(90)
c=0
while c<90:
    square(100)
    turtle.right(4)
    c+=1
turtle.exitonclick()


# In[13]:





# In[ ]:




