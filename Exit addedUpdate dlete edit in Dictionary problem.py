#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mydic={}

n=int(input("Number of data?:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter Value:")
    mydic[key]=value
    print("Current Dictionary:",mydic)
    
while True:
    
    press=int(input("\n\n 1 for Search\n 2 for Update\n 3 for Edit \n 4 for Delete \n 5 for Reset dictionary\n 6 Delete whole Dictionary\n 0 to Exit\n "))

    #global mydic
    
    if press==1:
        search=input("Search by key:")
        if search in mydic:
            print("The item is Found\nThe value of ","'",search,"'"," is","'", mydic[search],"'")
        else:
            print("The Item NOT Found!")

    elif press==2:
        nkey=input("Key to Update:")
        nvalue=input("Value to Update:")
        mydic[nkey]=nvalue
        print("Updated Dictionary: ",mydic)
    
    elif press==3:
        edit=input("Enter Key to Edit:")
        if edit in mydic:
            ekey=edit
            evalue=input("Value to Edit Dictionary")
            mydic[ekey]=evalue
            print("Edited Dictionary is:",mydic)
        else:
            print("The Item To edit does not Exist!")
            
    elif press==4:
        dlt=input("Enter Key To Delete:")
        mydic.pop(dlt)
        print("Deleted Successfully!\n",mydic)
        
    elif press==5:
        mydic.clear()
        print("Dctionary Resets!\n",mydic)
    
    elif press==6:
        del mydic
        print("The Dictionary Deleted Successfully!")
    elif press==0:
        break
        


# In[ ]:




