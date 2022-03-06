#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[29]:


data_country = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
print (data_country)


# In[30]:


data_India = data_country[data_country["Country"] == "India"].copy()
data_India["dt"] = pd.to_datetime(data_India["dt"])
print(data_India)


# In[20]:


data_global = pd.read_csv("GlobalTemperatures.csv")
print(data_global)


# In[31]:


data_global["dt"] = pd.to_datetime(data_global["dt"])
co2_ppm = pd.read_csv("archive.csv")
print(data_global)


# In[33]:


annual_mean_global = data_global.groupby(data_global["dt"].dt.year).mean()
reference_temperature_global = annual_mean_global.loc[1951:1980].mean()["LandAndOceanAverageTemperature"]
annual_mean_global["Anomaly"] = annual_mean_global["LandAndOceanAverageTemperature"] - reference_temperature_global
print(annual_mean_global)


# In[36]:


annual_mean_India = data_India.groupby(data_India["dt"].dt.year).mean()
reference_temperature_India = annual_mean_India.loc[1951:1980].mean()["AverageTemperature"]
annual_mean_India["Anomaly"] = annual_mean_India["AverageTemperature"] - reference_temperature_India
print(annual_mean_India)


# In[38]:


plt.figure()
plt.style.use("fivethirtyeight")
annual_mean_global.loc[1990:2015]["Anomaly"].plot(figsize = (10,5), grid=True, legend=True)
plt.title("Annual anomaly from base mean temperature (Global)")
plt.xlabel('')
plt.ylabel('Temperature Anomaly')
plt.show()


# In[40]:


plt.figure()
plt.style.use("fivethirtyeight")
annual_mean_India.loc[1990:2012]["Anomaly"].plot(figsize = (10,5), grid=True, legend=True)
plt.title("Annual anomaly from base mean temperature (India)")
plt.xlabel('')
plt.ylabel('Temperature Anomaly')
plt.show()


# In[42]:


plt.figure()
plt.style.use("fivethirtyeight")
annual_co2_ppm = co2_ppm.groupby(co2_ppm["Year"]).mean()
annual_co2_ppm.loc[1990:2015]["Carbon Dioxide (ppm)"].plot(figsize = (10,5), grid=True, legend=True)
plt.title("Global annual CO2 levels in atmosphere")
plt.ylabel("CO2 parts per million")
plt.show()


# In[43]:


annual_co2_temp = pd.merge(annual_mean_global.loc[1990:2015], annual_co2_ppm.loc[1960:2015], left_index=True, right_index=True)
annual_co2_temp = annual_co2_temp[["LandAndOceanAverageTemperature", "Anomaly", "Carbon Dioxide (ppm)"]].copy()
annual_co2_temp.corr()


# In[45]:


plt.figure(figsize=(15,8))
sns.scatterplot(x="Anomaly",y="Carbon Dioxide (ppm)", data=annual_co2_temp)


# In[ ]:




