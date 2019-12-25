#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()
#This is importing/loading the database that is needed for the analysis to take place. df.head is used to display the first 5 values of the table.


# In[34]:


df['cars_sold'].mean()
#since the dataframe is always established in the step above, finding the mean is as simple as .mean


# In[35]:


df['cars_sold'].max()
#max cars sold in the df


# In[36]:


df['cars_sold'].min()
#min cars sold in the df


# In[37]:


pd.pivot_table(df, values=['cars_sold'], index=['gender'])
#This is creating a tableview of average cars sold by gender


# In[38]:


df[df['cars_sold']>3]['hours_worked'].mean()
#using sub select where the fact that >3 is true, avergage hours worked by employees who worked 3 hours or more 


# In[39]:


df['years_experience'].mean()
#finding the mean of years experience


# In[40]:


df[df['cars_sold']>3]['years_experience'].mean()
#cars sold using sub select more than 3 with the average years of experience 


# In[42]:


pd.pivot_table(df, values=['cars_sold'], index=['salestraining'])
#creating a table & using sales training as the index, sales training has an affect.


# In[12]:


# best indicators of a good salesman:
# years of experience = irrelevant 
# hours worked = relevant
# sales training = relevant
# gender = relevant


# In[43]:


import matplotlib.pyplot as plt 
import seaborn as sns

sns.violinplot(x=df["cars_sold"], y=df["gender"], palette="Blues",bw=.1)
plt.show()


# In[30]:


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')


# In[31]:


df.head()


# In[75]:


import matplotlib.pyplot as plt

plt.plot(df.cars_sold,'go')
plt.xlabel('Years')
plt.ylabel('Cars Sold')
plt.show()


# In[54]:


import seaborn as sb 
import matplotlib.pyplot as plt 
sb.heatmap(df.corr(),cmap='coolwarm')
plt.show()


# In[66]:


import matplotlib.pyplot as plt 
plt.plot(df.gender, df.hours_worked)
plt.show()


# In[81]:


import seaborn as sns
sns.kdeplot(df['cars_sold'], shade=True)


# In[ ]:




