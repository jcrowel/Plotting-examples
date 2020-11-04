#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point


# In[2]:


#Identify the path to the data, and the file name
path='/shared/subx/forecast/weekly/20181011/data/'
fname='fcst_20181011.anom.pr_sfc.nc'


# In[3]:


#open the file, this can be called anything
ds=xr.open_dataset(path+fname)


# In[4]:


#checking to see what is in the file
ds


# In[5]:


#this plot is just the data, to see if you can plot whats in the file.
#a stepping stone for whats below.
#The *86400 is to change it to seconds instead of hours
plt.contourf(ds['CCSM4'][0,:,:]*86400)
plt.colorbar()


# In[6]:


# Make the figure larger
fig = plt.figure(figsize=(11,8.5))

# Set the axes using the specified map projection
ax=plt.axes(projection=ccrs.PlateCarree())

# Make a filled contour plot
ax.contourf(ds['lon'], ds['lat'], ds['CCSM4'][0,:,:]*86400,
            transform = ccrs.PlateCarree())

# Add coastlines
ax.coastlines()


# In[7]:


# Make the figure larger
fig = plt.figure(figsize=(11,8.5))

# Set the axes using the specified map projection
ax=plt.axes(projection=ccrs.PlateCarree())

#Because the above plot has a line through the middle, this will fix that
# Add cyclic point to data
data=ds['CCSM4'][0,:,:]*86400
data, lons = add_cyclic_point(data, coord=ds['lon'])


# Make a filled contour plot
cs=ax.contourf(lons, ds['lat'], data,
            transform = ccrs.PlateCarree(),cmap='PRGn',extend='both')

# Add coastlines
ax.coastlines()

# Define the xticks for longitude
ax.set_xticks(np.arange(-180,181,60), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)

# Define the yticks for latitude
ax.set_yticks(np.arange(-90,91,30), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

# Add colorbar
cbar = plt.colorbar(cs)

# Add title
plt.title('NCAR-CCSM4 Week 1 Precip anom')


# In[8]:


#this is identifying a new section of the map to plot
dim=ds.sel(lat=slice(25,60),lon=slice(180,300))


# In[9]:


#re-plotting with out anything added, to ensure the above statement works
plt.contourf(dim['CCSM4'][0,:,:]*86400)
plt.colorbar()


# In[14]:


#the dimensions selected below define the lat and lon plotted
dim=ds.sel(lat=slice(25,60),lon=slice(181,300))
lon= 300
minlon= -20 +lon
maxlon = +50 +lon
#here I have the extent to define where the map can go 
#The lat is different than what is defined above because this will get rid of white space 
extent=[minlon,maxlon, 11, 39]

# Make the figure larger
fig = plt.figure(figsize=(11,8.5))

# Set the axes using the specified map projection
ax=plt.axes(projection=ccrs.PlateCarree())

# Add cyclic point to data
data=dim['CCSM4'][0,:,:]*86400
data, lons = add_cyclic_point(data, coord=dim['lon'])


# Make a filled contour plot
ax.contourf(lons, dim['lat'], data,
            transform = ccrs.PlateCarree())

# Add coastlines
ax.coastlines()



# In[ ]:




