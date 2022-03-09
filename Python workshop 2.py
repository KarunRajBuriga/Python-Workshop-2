#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person():
    def __init__(self,name, designation):
        self.name = name
        self.designation = designation
    def display(self):
        print(self.name)
        print(self.designation)
    def learn(self):
        print(self.name+' Learning')
    def walk(self):
        print(self.name+' Walking')

    def eat(self):
        print(self.name+' Eating')

class Programmer(Person):
    def __init__(self,name,designation,company):
        self.company = company
        Person.__init__(self, name,designation )
    def company_name(self):
        print(self.name)
        print(self.company)
    def coding_work(self):
        print(self.name+' is doing coding')
Prg = Programmer('Rohit','coder',"CSE")
Prg.coding_work()

class Dancer(Person):
    def __init__(self,name,designation,groupName):
        self.groupName = groupName
        Person.__init__(self, name,designation )
    def group_Name(self):
        print(self.name)
        print(self.groupName)
    def dancing(self):
        print(self.name+' is dancing')
my_dancer = Dancer('Sunny','dancer',"Dancing Angels")
my_dancer.dancing()

class Singer(Person):
    def __init__(self,name,designation,bandName):
        self.bandName = bandName
        Person.__init__(self, name,designation )
    def band_Name(self):
        print(self.name)
        print(self.bandName)  
    def singing(self):
        print(self.name+' is singing')
    def play_guitar(self):
        print(self.name+' is playing guitar')
my_singer = Singer('Gandhi','Singer',"The Vocals")
my_singer.singing()
my_singer.play_guitar()


# In[2]:


import pandas as pd 


# In[3]:


df=pd.read_csv('Documents\\sales_1.csv')


# In[4]:


df


# In[5]:


df1=pd.read_csv('Documents\\sales_2.csv')


# In[6]:


df1


# In[7]:


df2=pd.concat([df,df1],axis=0)


# In[8]:


df2


# In[ ]:


df3=df2.melt(id_vars=['PRODUCT_TYPE'],var_name='SOLD_DATE',value_name='QTY_SOLD')
df3


# In[ ]:


df3.to_csv('C:\\Users\\KBuriga\\final.csv')


# In[9]:





# In[ ]:





# In[ ]:





# In[11]:


import pandas as pd
import requests
import json

data = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2017-01-01&endtime=2017-12-31&alertlevel=yellow")
data = json.loads(data.text)
a = data['features']
df = pd.DataFrame(a)
b = df.properties

time_list = []
place_list = []
type_list = []
magnitude_list = []

for i in range(len(a)):
    time_list.append(b[i]['time'])
    place_list.append(b[i]['place'])
    type_list.append(b[i]['type'])
    magnitude_list.append(b[i]['cdi'])
    i+=1


df1 = pd.DataFrame(time_list,columns = ['Time'])
df1['Place'] = place_list
df1['Type'] = type_list
df1['Magnitude'] = magnitude_list
print(df1)



# In[17]:


import pyodbc 
server = 'OTUSDPSQL'
database = 'B12022_Target_KBuriga'
username = 'B12022_KBuriga'
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


# In[18]:


cursor.execute('create table apiData(Time bigint , Place varchar(50) , Type varchar(25) , Magnitude numeric(3,1))')


# In[19]:


for index,row in df1.iterrows():
    cursor.execute("INSERT INTO dbo.apiData values(?,?,?,?)",row.Time , row.Place, row.Type , row.Magnitude)


# In[20]:


cnxn.commit()


# In[ ]:


cursor.close()


# In[21]:


cursor.execute('select top 1 * from dbo.apiData order by Magnitude desc')


# In[22]:


cnxn.commit()


# In[23]:


cursor.close()


# In[ ]:




