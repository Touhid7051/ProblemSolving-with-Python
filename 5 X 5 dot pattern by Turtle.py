#!/usr/bin/env python
# coding: utf-8

# In[12]:


import turtle
height=int(input("Enter Height"))
width=int()
turtle.speed(2)
turtle.penup()
for i in range(height):
    for j in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
turtle.exitonclick()


# In[ ]:




