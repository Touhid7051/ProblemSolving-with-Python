#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
conn = sqlite3.connect('tou.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

#Creating table A


cursor.execute('''CREATE TABLE A
(CustomerNo INT PRIMARY KEY NOT NULL,
FirstName TEXT NOT NULL,
LastName TEXT NOT NULL);''')



#Creating Table B

cursor.execute('''CREATE TABLE B
(OrderNo INT PRIMARY KEY NOT NULL,
EmployeeNo INT NOT NULL,
CustomerNo REFERENCES A(CustomerNo),
Supplier TEXT NOT NULL,
Price TEXT NOT NULL);''')



cursor.execute("INSERT INTO A (CustomerNo,FirstName,LastName) VALUES (1, 'Sally','Thompson')");
cursor.execute("INSERT INTO A (CustomerNo,FirstName,LastName) VALUES (2, 'Sally','Henderson')");
cursor.execute("INSERT INTO A (CustomerNo,FirstName,LastName) VALUES (3, 'Harry','Henderson')");
cursor.execute("INSERT INTO A (CustomerNo,FirstName,LastName) VALUES (4, 'Sandra','Wellington')");



cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (1,1,42, 'Harrison', '$235' )");
cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (2,4,1, 'Ford', '$234' )");
cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (3,1,68, 'Harrison', '$415' )");
cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (4,2,112, 'Ford', '$350' )");
cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (5,3,42, 'Ford', '$234' )");
cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (6,2,112, 'Ford', '$350' )");
cursor.execute("INSERT INTO B (OrderNo,EmployeeNo,CustomerNo,Supplier,Price) VALUES (7,2,42, 'Harrison', '$235' )");
conn.commit()
conn.close()


# In[ ]:




