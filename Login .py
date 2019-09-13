#!/usr/bin/env python
# coding: utf-8

# In[28]:


class user:
    name = ''
    email = ''
    password = ''
    login=False

    def sum(self):
        email=input('enter mail: ')
        password=input('enter password: ')

        if email==self.email and password==self.password:
            login=True
            print('login successful!!')
        else:
            print('login failed')

user1 = user()
user1.name='tareq'
user1.email='sunday@gmail.com'
user1.password='12345'

user1.sum()


# In[ ]:





# In[ ]:




