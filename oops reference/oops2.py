#!/usr/bin/env python
# coding: utf-8

# In[25]:


class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi


# In[26]:


a=Circle(radius=4)


# In[27]:


a.area


# In[28]:


a.pi

