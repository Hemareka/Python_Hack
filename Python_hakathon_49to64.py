#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns
import plotly.graph_objects as go
from matplotlib.sankey import Sankey
#from wordcloud import WordCloud,STOPWORDS
import warnings
warnings.filterwarnings("ignore")


# In[19]:


DonorDetails = pd.read_excel(r"C:\Users\hemar\OneDrive\NumpyNinja\Python Hackathon\DonorDetails.xlsx")
ReferralDetails=pd.read_excel(r"C:\Users\hemar\OneDrive\NumpyNinja\Python Hackathon\ReferralDetails.xlsx")
Outcomes=pd.read_excel(r"C:\Users\hemar\OneDrive\NumpyNinja\Python Hackathon\Outcomes.xlsx")
OPO_HospDetails=pd.read_excel(r"C:\Users\hemar\OneDrive\NumpyNinja\Python Hackathon\OPO_HospDetails.xlsx")
Yearly_Outcomes=pd.read_excel(r"C:\Users\hemar\OneDrive\NumpyNinja\Python Hackathon\Yearly_Outcomes.xlsx")


# In[21]:


DonorDetails


# In[ ]:


#Q 49. Perform an EDA of hosp_details using YDATA Profiling.


# In[22]:


Outcomes


# In[56]:


#Q 50. In how many cases were the relatives approached for consent vs how many were authorized?
Relatives_approached_for_consent = ReferralDetails[(ReferralDetails['Approached Relatives'] ==1)]

print("Relatives_approached_for_consent" + ": "+ str(Relatives_approached_for_consent['PatientID'].nunique()))


# In[54]:


Relatives_authorized= ReferralDetails[(ReferralDetails['Authorized By Family'] ==1)]

print("Relatives_authorized"+": "+str(Relatives_authorized['PatientID'].nunique()))


# In[58]:


Approached_and_Authorized= ReferralDetails[(ReferralDetails['Approached Relatives'] ==1) & (ReferralDetails['Authorized By Family'] ==1)]
print("Approached_and_Authorized" + ": "+ str(Approached_and_Authorized['PatientID'].nunique()))


# In[42]:


print(ReferralDetails.columns)


# In[26]:


ReferralDetails


# In[154]:


#Q 51. Which OPO recorded the lowest calculated deaths in any year?
Grouped_by_OPO= Yearly_Outcomes.groupby('OPO')['mean calc deaths'].sum() # group by OPO and finding the sum of 'mean calc deaths'for each OPO.
df=Grouped_by_OPO.to_frame(name='OPO with the lowest_deaths')
lowest_deaths=df.sort_values(by='OPO with the lowest_deaths').iloc[0]
print(Grouped_by_OPO)
print(lowest_deaths)


# In[82]:


Yearly_Outcomes.columns


# In[ ]:


#Q 52. Plot the Density Chart for Cause of Death- Seizure against any other variable of your choice.


# In[ ]:


#Q 53. Display a correlation matrix showing count of donors in age group vs cause of death.


# In[156]:


#Q 54. Connect to sql and write a query to find all donors who's cause of death is unknown
# SELECT * FROM [dbo].[DonorDetails] WHERE causeofdeath='unknown';

import pyodbc


# In[ ]:


#USERNAME= 'RANGAELITEBOOK\hemar'
# ;UID= {USERNAME};PWD={PASSWORD};ENCRYPT=yes


# In[196]:


# creating connection credentials
SERVER= 'RANGAELITEBOOK\SQLEXPRESS'
DATABASE= 'Organ_Donors'
USERNAME= 'RANGAELITEBOOK\hemar'


# In[208]:


connection_string=f'DRIVER={{ODBC Driver 18 for SQL server}};SERVER= {SERVER};DATABASE= {DATABASE};UID= {USERNAME};Trusted_Connection=yes;ENCRYPT=yes;TrustServerCertificate=yes'


# In[ ]:


#Q 55. Who was the youngest white donor registered?
#SELECT  top 1 * FROM [dbo].[DonorDetails] Where age is not null and race='white' order by age, PatientID ;



# In[ ]:


#Q 56. What is the average time difference between brain death and time_approached?


# In[ ]:


#Q 57. Plot a graph to show the distribution of age.


# In[ ]:


#Q 58. Plot a 3-D graph using any set of random values chosen by you.


# In[ ]:


#Q 59. What % of the dataset is male vs female?


# In[ ]:


#Q 60. How many patients of each race are listed under an Unknown cause of death?


# In[ ]:


#Q 61. Display all records where approached time is more than 2 days after referral time



# In[ ]:


#Q 62. Display a donut chart of race and explode the wedge with the maximum patients


# In[ ]:


#Q 63. Plot a graph by multiplotting on the same canvas  (Take any set of x & y values)


# In[ ]:


#Q 64. Replace all null values in 'Procured_year' to 1900

