#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list=[]
n=int(input("The Size Of List:"))
for i in range(n):
    s=input("The Element:")
    list.append(s)
    print("Current List: ",list)
    
def fun():    
    print("\n\nWhat Do you want Now?\n","Press 1 for Update\n","Press 2 for Delete\n","Press 3 for Edit\n","Press 4 for Search\n","Press 5 for Sort\n","Press 6 for Delete All\n")

    press=int(input("Select:"))
    if press==1:
        update=input("Enter New Data: ")
        list.append(update)
        print(list)
    elif press==2:
        dl=input("Value to delete:")
        list.remove(dl)
        print(list)
    elif press==3:
        poss=int(input("Enter possition value"))
        edit=input("Enter Value:")
        list[poss]=edit
        print(list)
    elif press==4:
        item=input("Search:")
        if item in list:
            print("The Item ","'",item,"'", " Exists in ",list)
        else:
            print("The item Not Found")
    elif press==5:
        list.sort()
        print(list)
    elif press==6:
        del list[:]
        print(list)
        print("The List Deleted Successfully")
    fun()
fun()



# 
