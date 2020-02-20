#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Book():
    purpose='knowledge'
        
    def __init__(self,volume,author):
        self.volume = volume
        self.author = author


# In[30]:


read=Book(volume='3rd', author='Tim Berners Lee')


# In[32]:


read.volume


# In[34]:


read.purpose


# In[58]:


class Car():
    brand='Audi'
    def __init__(self,model,color,availability,speedlimit):
        self.model=model
        self.color=color
        self.availability=availability
        self.speedlimit=speedlimit
    def release(self):
        print("The {} {} is released in {} with a maximum speedlimit of {}".format(self.brand, self.model, 2014, self.speedlimit))


# In[63]:


my_car=Car('A7','Classice Red Pearl',True,'350kph')


# In[64]:


my_car.release()


# In[65]:


my_car.color


# In[66]:


my_car.availability

