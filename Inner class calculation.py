#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Calculate:
    def __init__(self):
        self.a=int(input("1st:"))
        self.b=int(input("2nd:"))
        self.c = 0
        self.Add=self.Add(self)
        self.Mul=self.Mul(self)
        self.Div=self.Div(self)
        self.Sub=self.Sub(self)


    class Add:

        def __init__(self,outher):
            self.Calculate=outher

        def add(self):
            self.Calculate.c=self.Calculate.a+self.Calculate.b
            print("Summation is:",self.Calculate.c)



    class Mul:

        def __init__(self,outher):
            self.Calculate=outher

        def mul(self):
            self.Calculate.c=self.Calculate.a*self.Calculate.b
            print("Multiplication is",self.Calculate.c)

    class Div:

        def __init__(self,outher):
            self.Calculate=outher

        def div(self):
            self.Calculate.c=self.Calculate.a/self.Calculate.b
            print("Division is",self.Calculate.c)

    class Sub:

        def __init__(self,outher):
            self.Calculate=outher

        def sub(self):
            self.Calculate.c=self.Calculate.a-self.Calculate.b
            print("Differance is",self.Calculate.c)

if __name__=="__main__":
    cal=Calculate()
    cal.Add.add()
    cal.Mul.mul()
    cal.Div.div()
    cal.Sub.sub()





# In[ ]:




