#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recur_sum(n):
    if(n<=0):
        return n
    else:
        return n+recur_sum(n-1)
num=int(input("enter the number:"))
if(num<0):
    print("enter positive number")
else:
    print("sum is",recur_sum(num))


# In[ ]:




