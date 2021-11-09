#!/usr/bin/env python
# coding: utf-8

# <h2>PS4 - Question 0 - Topics in Pandas</h2>
# <p>For this question, please pick a topic - such as a function, class, method, <a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html">recipe or idiom</a> related to the pandas python library and create a short tutorial or overview of that topic. The only rules are below.</p>
# <ol style="list-style-type: decimal">
# <li>Pick a topic <em>not</em> covered in the class slides.</li>
# <li>Do not knowingly pick the same topic as someone else.</li>
# <li>Use bullet points and titles (level 2 headers) to create the equivalent of <strong>3-5</strong> “slides” of key points. They shouldn’t actually be slides, but please structure your key points in a manner similar to the class slides (viewed as a notebook).</li>
# <li>Include executable example code in code cells to illustrate your topic.</li>
# </ol>
# <p>You do <em>not</em> need to clear your topic with me. If you want feedback on your topic choice, please discuss with me or a GSI in office hours.</p>

# In[1]:


# Module imports
import pandas as pd
import numpy as np
from datetime import *
from IPython.core.display import display, HTML


# ## Timedeltas
# ### Overview
# - Using Timedeltas
# - Filter data with Timedelta
#     - Example - number of homework
# - Example - age
# - Arithmetic operation
# - Example - Arithmetic Operation

# ## Timedeltas
# - Timedeltas is a type that shows the difference between values of date times. For instance, the difference between years, months, days, hours, minutes, seconds, even milliseconds, and so on. Also, the result will give in the Timedelta type.
# - the form of the datetime is not restricted. It can be either mm-dd-yyyy or yyyy-mm-dd, "-" or "/".  
# - if we do not assign month or year, then it will have default value 1, which is first day and January.

# In[2]:


# Construct Timedelta by string
td0 = pd.Timedelta('1 days 7 hours 45 minutes 30 seconds')
print(td0)


# In[3]:


td2 = pd.date_range('2020-01-24', periods=7, freq='15min')
print("The frequence is ", pd.to_timedelta(td2.freq))


# In[4]:


# Construct Timedelta
to_td = pd.to_timedelta('30min')

# transform from minutes to seconds
td_second = to_td.total_seconds()

# transform from seconds to time
td_period = str(pd.Timedelta(seconds=700000))

# print results
print("seconds:", int(td_second), "s")
print("period:", td_period)


# In[5]:


td_mdy = pd.to_datetime('8-18-2021') - pd.to_datetime('12-21-2020')

td_n = pd.to_datetime('2020-12-24') - pd.to_datetime('2019')
td_ny = pd.to_datetime('2020-12-24') - pd.to_datetime('2019-1')
td_nyr = pd.to_datetime('2020/12/24') - pd.to_datetime('2019-1-1')

print("datetime in mm-dd-yyyy with assigned date:", td_mdy)
print("datetime in yyyy-mm-dd with assigned year and month:", td_ny)
print("datetime in yyyy-mm-dd with assigned year:", td_n)
print("datetime in yyyy-mm-dd with assigned date on Jan. 1st:", td_n)


# ## Filter data with Timedelta
# - We can use Timedelta to filter the date data to obtain the results we need.

# ## Example - number of homework
# - In following example, we are going to figure out the number of homework that will due in a week.
# - From the dataframe df_dues, we could see from index 1 to 3, the homework is closed.

# In[6]:


dues = {'due_date': ['2021/10/07', '2021/10/11', 
                     '2021/10/22', '2021/10/24', 
                     '2021/10/27', '2021/10/31',], 
        'hw_number': [3, 1, 2, 5, 4, 2]}
df = pd.DataFrame(dues, index=[1, 2, 3, 4, 5, 6])
display(HTML(df.to_html()))


# In[7]:


df['due_date'] = pd.to_datetime(df['due_date'])
df = df[(df['due_date'] - datetime.now()) > pd.Timedelta(days=0)]
df = df[(df['due_date'] - datetime.now()) < pd.Timedelta(days=7)]
display(HTML(df.to_html(index=False)))
print(df['hw_number'].sum(), "homework needs to be finished in one week.")


# ## Example - age
# - We could apply Timedelta to calculate the age of a person given his birth date.
# - In this example, we use Timedelta to find the age for someone born on 06/27/1998.

# In[8]:


age = int((datetime.now() 
           - pd.to_datetime('6-27-1998')) 
          / pd.Timedelta(days=365))
print("age:", age)


# ## Arithmetic Operation
# - This example shows the arithmetic operation of Timedelta. Also, a time series is constructed further on the basis of Timedelta.

# ## Example - Arithmetic Operation

# In[9]:


time = pd.date_range(start='2021-9-7', periods=7, freq='7D')
print("Time period from {} to {}".format(time.min(), time.max()))


# In[10]:


# add 5 minutes
time_plus = time + pd.Timedelta(minutes=5)

# subtract datetime(year, month, day, hour, minute)
time_minus = time - datetime(2020, 1, 21, 3, 5)

#print results
print("Addition: ", time_plus)
print("Subtraction: ", time_minus)


# In[11]:


td1 = pd.Series([pd.Timedelta(days=3*(i+1)) for i in range(7)])
df1 = pd.DataFrame(dict(date=time, period=td1))

# operations
df1['addition']=df1['date'] - df1['period']
df1['subtraction']=df1['date'] - df1['period']
display(HTML(pd.DataFrame(df1).to_html()))


# In[12]:


# Construct Time Series
ts1 = pd.Series(np.random.randn(7), index=time)
print('Time seris (Oct. 5th):', ts1['2021-10-05'])
display(HTML(pd.DataFrame(ts1).to_html()))

