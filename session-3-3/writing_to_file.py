# to do 

from netCDF4 import Dataset
import numpy as np
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so'] 
pressure_3d = np.zeros((31,80,27)) 
density = sw.dens(salinity[:,:,:,:],temperture[:,:,:,:],pressure_3d)
density = density - 1000
#density_onetime = density[100,:,:,:]
#density_onetime = density
#print(density_onetime.shape)
#print(density.shape) = (1356, 31, 80, 27)

for i in range(0,1356):
	call = open('call_' + str(i) +  '.txt','w')
	for item in range(0,31):
		for sat in range(0,80):
			for love in range(0,27):
				call.write(str(density[i,item,sat,love]) + "\n")
	call.close()

