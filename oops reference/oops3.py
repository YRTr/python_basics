#!/usr/bin/env python
# coding: utf-8

# In[39]:


class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    def getCircumference(self):
        return self.radius*self.pi*2


# In[41]:


a=Circle(2)


# In[42]:


a.getCircumference()

