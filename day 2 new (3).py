#!/usr/bin/env python
# coding: utf-8

# ## list and its defaults functions
# 

# In[2]:


lst=["sahil",27,86.6,[1,2,3,4]]


# In[3]:


lst


# In[4]:


lst.append("syed")


# In[5]:


lst


# In[6]:


lst1=lst.copy()


# In[7]:


lst1


# In[8]:


lst2=["shahbaz",55]


# In[9]:


lst2


# In[10]:


lst1.extend(lst2)


# In[11]:


lst1


# In[13]:


lst1.index(55)


# In[14]:


lst1.insert(2,72)


# In[15]:


lst1


# # # dictionary and its defaults functions
# 

# In[55]:


dict={"name":"syedsahil","age":"twenty","year":2020}


# In[56]:


dict


# In[59]:


dict1=dict.copy()


# In[60]:


dict1


# In[61]:


dict.fromkeys("name")


# In[62]:


dict.get("age")


# In[63]:


dict.items()


# In[64]:


dict.keys()


# In[65]:


dict.pop("name")


# In[66]:


dict


# In[70]:


dict.popitem()


# In[72]:


dict.setdefault(0)


# In[73]:


dict


# In[84]:


dict.update({"course":"python"})


# In[85]:


dict


# In[86]:


dict.values()


# # # sets and its default function

# In[87]:


set={1.0,'hello',(1,2,3)}


# In[88]:


set


# In[89]:


set.add(55)


# In[90]:


set


# In[91]:



set1=set.copy()


# In[92]:


set1


# In[93]:


set2={(1,2,3,),27,'sahil'}


# In[94]:


set1.difference(set2)


# In[97]:


set1.difference_update(set2)


# In[98]:


set2


# In[99]:


set1


# In[100]:


set1.discard(1.0)


# In[101]:


set1


# In[156]:


set1.intersection(set2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[108]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # # Tuple & explore default methods

# In[129]:


tuple=("sahil","a","shahbaz","b")


# In[130]:


tuple


# In[132]:


tuple.count('a')


# In[137]:


tuple.index('b')


# 
# # # string & explore defaults methods 

# In[138]:


string="MY NAME IS SYED SAHIL"


# In[139]:


string.capitalize()


# In[144]:


string.center(28,'#')


# In[148]:


string.count('my')


# In[149]:


string.encode()


# In[ ]:




