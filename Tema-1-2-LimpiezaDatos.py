#!/usr/bin/env python
# coding: utf-8

# #### Resumen de los datos: dimensiones y estructuras 

# In[2]:


import pandas as pd
import os


# In[60]:


miPath = "/Users/User/Documents/Udemy-Cursos/DataScience-Python/python-ml-course/datasets"
miArchivo = "titanic/titanic3.csv"
fullPath = os.path.join(miPath, miArchivo)

urlData = "https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/titanic/titanic3.csv"


# In[9]:


fullPath


# In[10]:


miPath


# In[62]:


# Leo los datos csv y los guardo en un archivo
data = pd.read_csv(fullPath)
data = pd.read_csv(urlData)


# In[14]:


# con HEAD() muestro las 5 primeras lineas
#            o la cantidad de lineas que desee (10)

data.head(10)


# In[18]:


data2.head(10)


# In[19]:


# saber el formato del csv
# cantidad  de lineas y columnas 
data.shape


# In[22]:


# tail() se muestran las ultimas 5 filas
#        o si quiero un cantidad especial (10)
data.tail(10)


# In[23]:


# obtener columnas y sus valores 
data.columns


# In[24]:


data.columns.values


# ##### Resumen estadisticos basicos de las variables numericas

# In[25]:


data.describe()


# In[26]:


data.dtypes


# ##### buscar faltantes de valores

# In[27]:


pd.isnull(data["body"])


# In[28]:


pd.notnull(data["body"])


# In[36]:


pd.isnull(data["body"]).values.ravel().sum()


# In[35]:


pd.notnull(data["body"]).values.ravel().sum()


# ###### los valores que faltan en data set pueden venir por dos razones
# * Extraccion de los datos 
# * Recoleccion de los datos

# In[37]:


# borrar los datos que faltan
# borrar toda la fila o toda la columna 
# dependiendo la cantidad de valores faltantes de la col
# data.dropna(axis=0, how="all") #borrar la fila con todos nan
# data.dropna(axis=0, how="any") #borrar la fila con solo tener un nan


# ###### Computo de valores faltantes ... rellenar los nan

# In[38]:


data2 = data


# In[39]:


data2.fillna(0)


# In[40]:


data4 = data
data4.fillna("sin datos")


# In[43]:


# elegir filas y columnas a cambiar 
data5 = data
data5["body"] = data5["body"].fillna(0)
data5["home.dest"] = data5["home.dest"].fillna("sin Dato")


# In[44]:


data5


# ###### rellenar los faltantes con el promedio de la columna

# In[46]:


pd.isnull(data5["age"]).values.ravel().sum()


# In[49]:


data5["age"] = data5["age"].fillna(data5["age"].mean())


# In[50]:


data5


# In[65]:


# cambia los na con los mas cerca antes o despues 
data["age"][1291]


# In[67]:


data["age"].fillna(method="ffill")[1291]


# In[69]:


data["age"].fillna(method="backfill")[1291]


# In[70]:


# leer planilla excel 
miPath = "/Users/User/Documents/Udemy-Cursos/DataScience-Python/datasets"
miArchivo = "Prorrateos-Mazro2020.xls"
fullPath = os.path.join(miPath, miArchivo)
expensas = pd.read_excel(miPath + "/" + miArchivo, "Prorrateos")


# In[73]:


expensas.tail()


# In[74]:


expensas.describe()


# In[75]:


expensas.dtypes


# In[76]:


expensas["Fecha Prorrateo"]


# In[77]:


pd.isnull(expensas).values.ravel().sum()


# In[78]:


expensas.columns


# In[79]:


expensas.columns.values


# In[80]:


expensas["Exp A"].mean()


# In[85]:


expensas["Cob Exp C"].count()


# In[86]:


expensas["Cob Exp C"]


# In[88]:


pd.isnull(expensas["Cob Exp C"]).values.ravel().sum()


# In[90]:


pd.isnull(expensas["Cob Exp C"]).values


# In[91]:


nan_rows = expensas[expensas.isnull().any(1)]


# In[92]:


nan_rows


# In[ ]:




