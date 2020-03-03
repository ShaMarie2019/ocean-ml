#to do
# create a numpy area called geopotential that is latitude x longitude x depth, contains the geopotential height 

from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')
pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so']
geo_height = dataset['zo']
pressure_3d = np.zeros((31,80,27))

# for i in range(0,31):
# 	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
# 	print(pressure_3d[i,:,:])

# density = sw.dens(salinity[:],temperture[:],pressure_3d)
# print(density)

