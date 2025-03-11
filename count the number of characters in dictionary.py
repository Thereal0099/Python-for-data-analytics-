#!/usr/bin/env python
# coding: utf-8

# In[3]:


def count_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count
string=input("enter string:")
dict_count=count_char(string)
for char,count in dict_count.items():
    print(f"{char} : {count}")    


# In[ ]:




