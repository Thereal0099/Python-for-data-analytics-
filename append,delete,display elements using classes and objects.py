#!/usr/bin/env python
# coding: utf-8

# In[4]:


class list_manager:
    def __init__(self):
        self.list=[]
    def insert(self,element):
        self.list.append(element)
    def remove(self,element):
        if element in self.list:
            self.list.remove(element)
        else:
            print("element not found")
    def display(self):
        print("the elements are:",self.list)
ele=list_manager()
while True:
    print("\n 1.append 2.Delete 3.Display 4.Exit" )
    choice=int(input("enter your choice"))
    if(choice==1):
        element=int(input("enter the element to be inserted"))
        ele.insert(element)
    elif(choice==2):
        element=int(input("enter the element to be deleted"))
        ele.remove(element)
    elif(choice==3):
        ele.display()
    elif(choice==4):
        print("exiting program")
        break
    else:
        print("enter the correct choice:")


# In[ ]:




