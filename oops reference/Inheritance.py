#!/usr/bin/env python
# coding: utf-8

# In[88]:


class Audi():
    def __init__(self):
        print("Finest Car in India")
    def origin(self):
        print("German automobile industry")
    def availIndia(self):
        return True


# In[89]:


class Q5(Audi):
    def __init__(self):
        Audi. __init__(self)
        print("It's AUDI Q5!")
    def price(self):
        print("Cost: 1.07 crores")
    def releaseYear(self):
        print("2018")
    


# In[90]:


my_car=Q5()


# In[91]:


my_car.price()


# In[93]:


my_car.origin()


# In[95]:


print("{}, {} released in {}. Trademark:{}".format(Q5(),my_car.price(),my_car.releaseYear(),my_car.origin()))


# In[ ]:




