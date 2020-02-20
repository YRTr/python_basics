#!/usr/bin/env python
# coding: utf-8

# In[118]:


class Dog():
    def __init__(self, name):
        self.name=name
        print("It's a dog")
    def speak(self):
        return self.name+ ' says WOOF!'


# In[119]:


class Cat():
    def __init__(self, name):
        self.name=name
        print("It's a cat")
    def speak(self):
        return self.name+ ' says MEOW!'


# In[120]:


rocky=Dog('rocky')
sam=Cat('sam')
    


# In[121]:


for pet in [rocky,sam]:
    print(pet.speak())


# In[ ]:




