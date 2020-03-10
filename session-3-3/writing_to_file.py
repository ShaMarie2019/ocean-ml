# to do 

from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so'] 
pressure_3d = np.zeros((31,80,27)) 
density = sw.dens(salinity[0,:,:,:],temperture[0,:,:,:],pressure_3d)
density = density - 1000
#density_onetime = density[100,:,:,:]
density_onetime = density
#print(density_onetime.shape)

call= open('call.txt','w')

for item in range(0,31):
	for sat in range(0,80):
		for love in range(0,27):
			call.write(str(density_onetime[item,sat,love]) + "\n")
call.close()

