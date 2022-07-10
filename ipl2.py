#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("D:\python\matches.csv")
# df.head()


# In[4]:


df.shape


# In[5]:


df.isnull().sum()


# In[6]:


df.drop(columns=["umpire3"],inplace=True)


# In[7]:


df=df.dropna()
df.reset_index(inplace=True)

fig=plt.figure(figsize=(8,10))
sns.countplot(y=df["venue"],order=df['venue'].value_counts(ascending=False).index)
st.pyplot(fig)

# In[13]:



st.write("""

# IPL MATCH PREDICTION!

""")


# In[14]:


t1=st.text_input("enter team 1 name: ")
t2=st.text_input("enter team 2 name: ")


# In[17]:


def result(t1,t2):
    te1=[]
    team1_wins=0
    team2_wins=0
    for i in range(len(df)):
        if df["team1"][i].lower()==t1.lower() or df["team2"][i].lower()==t1.lower() and df["team1"][i].lower()==t2.lower() or df["team2"][i].lower()==t2.lower():
            if df["winner"][i]==t1:
                team1_wins=team1_wins+1
            else:
                team2_wins=team2_wins+1
                te1.append(df["team1"][i]) 
    data_1 = {"total matches played":len(te1),"team one wins":team1_wins,"team two wins":team2_wins}
    if team1_wins>team2_wins:
        data_1 = {"total matches played":len(te1),"team one wins":team1_wins,"team two wins":team2_wins,"winning probability":t1}
    else:
         data_1 = {"total matches played":len(te1),"team one wins":team1_wins,"team two wins":team2_wins,"winning probability":t2}
    result = pd.DataFrame(data_1, index=[0])
    return result
        


# In[20]:


out=result(t1,t2)
st.write(out)


# In[ ]:




