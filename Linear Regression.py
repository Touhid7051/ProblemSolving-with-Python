#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/jeffheaton/aifh/master/vol1/python-examples/datasets/breast-cancer-wisconsin.csv")
df.head()
y= df['class']
x = df.drop(["class", "bare_nucleoli"], axis=1)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.33,random_state=42)
clf = LinearRegression()
clf.fit(x_train,y_train)
clf.score (x_test, y_test)


# In[7]:


import pandas as pd
df = pd.read_csv("C:\\Users\\dcL\\Desktop\\iris.csv")
df.head()


# In[8]:


y= df['species']
x = df.drop(["petal_width"], axis=1)


# In[15]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


# In[16]:


x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.33,random_state=42)


# In[17]:


clf = LinearRegression()
le = preprocessing.LabelEncoder()
le.fit(y_train)
c = le.transform(y_train)


# In[22]:


clf = LinearRegression()
clf.fit(x_train,y_train)
clf.score (x_test, y_test)


# In[ ]:




