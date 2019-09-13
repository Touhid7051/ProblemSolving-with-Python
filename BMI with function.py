#!/usr/bin/env python
# coding: utf-8

# In[1]:


#name="Touhid"
#height_m=2
#weight_kg=100


def fun(name,height_m,weight_kg):
    bmi=weight_kg/(height_m ** 2)
    print("BMI: ")
    print(bmi)
    if bmi<25:
        return name+" is Under weight"
    
    
    elif bmi>=25 and bmi<=45:
        return name+" is Normal"

    else:
        return name+" is Over Weight"
fun("Ajom Khan",2,90)
    


# In[ ]:


result1=fun("harun",2,56)


# In[ ]:


print(result)


# In[ ]:


result


# In[3]:


def milestokm(miles):
    km = 1.6 * miles
    return km

f=milestokm(45)
print(f)
    


# In[ ]:




