# to do 

from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so'] 
pressure_3d = np.zeros((31,80,27)) 

# for i in range(0,31):
# 	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
density = density - 1000
print(density.shape)

# for i in range(0,10):
# 	for j in range(0,10):
# 		for k in range(0,10):
# 			#print(i,j,k)