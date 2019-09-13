#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sub=['Python','C++','Java','Javascript']
courseId=["1101","1102","1103","1104"]
courseStatus=["Done","Learnig","Undone"]
skillStatus=["Best","Normal","Low"]
print("My Programming Courses!")
for i in sub:
    cId=input("Course ID: ")
    if cId in courseId:
        if cId == "1101":
            print("Course Name: ",sub[0])
            print("Course status: "+courseStatus[1])
            print("Skill Status: "+skillStatus[1])
            break
        elif cId == "1102":
            print("Course Name: ",sub[1])
            print("Course status: "+courseStatus[0])
            print("Skill Status: "+skillStatus[0])
            continue
        elif cId == "1103":
            print("Course Name: ",sub[2])
            print("Course status: "+courseStatus[2])
            print("Skill Status: "+skillStatus[2])
        elif cId == "1104":
            print("Course Name: ",sub[3])
            print("Cousre Status: ",courseStatus[0])
            print("Skill Status: ",skillStatus[0])
        else:
            print("Wrong year of election!")
    else:
        print("The above loop was just for demonstration purpose!")


# In[ ]:

























