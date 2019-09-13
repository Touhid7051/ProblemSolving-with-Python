#!/usr/bin/env python
# coding: utf-8

# In[35]:


txt=input("Input a Text:")

if txt.isalnum()==True:
    print("This is an AlphaNumeric Text")
    if txt.islower()==True:
        print("The Text Contains Lowercase Charectar")
        print(txt,end=" in Upper Case: ")
        print(txt.upper())
    if txt.isnumeric()==True:
        print("This Text Contains only Possitive Number")
    if txt.isupper()==True:
        print("All are the Upper case charecters")
        print(txt,end=" in Lower Case: ")
        print(txt.lower())
    if txt.istitle()==True:
        print("This is a title")
elif txt.isspace()==True:
    print("Blank Input")

else:
    print("The Text contains Symbol",end=" ")
    num=int(txt)
    if num<0:
        print("Minus(-)")
        print("These is a Negative Number") 
        print("Number in absolute form:",abs(num))
        
print("The Input Length is:",len(txt))
    


# In[ ]:





# In[ ]:





# In[ ]:




