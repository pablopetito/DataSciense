#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[2]:


import pandas as pd
import os
import csv


# In[9]:


miPath = "C:/Users/User/Documents/Udemy-Cursos/DataScience-Python/python-ml-course/datasets"
miArchivo ="/titanic/titanic3.xls"
miArchivo2 ="/titanic/titanic3.xlsx"


# In[10]:


titanic3 = pd.read_excel(miPath + "/" + miArchivo, "titanic3")
titanic2 = pd.read_excel(miPath + "/" + miArchivo2, "titanic3")


# In[11]:


titanic2.head()


# In[ ]:





# In[12]:


titanic3.to_csv(miPath + "/titanic/archivo-Titanic-CSV.csv")

