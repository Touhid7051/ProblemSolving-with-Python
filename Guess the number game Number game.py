#!/usr/bin/env python
# coding: utf-8

# In[9]:


from random import*
number = randint(1,9)
guess = int(input('Enter a Number Between 1 to 9 : '))
if guess == number:
# New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
# New block ends here
elif guess < number:
# Another block
    print('No, it is a little higher than that')
# You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
# you must have guessed > number to reach here
print('Number is:',number)
# This last statement is always executed,
# after the if statement is ex


# In[ ]:




