<<<<<<< HEAD
# to do 

=======
>>>>>>> 507f30019f87660c645769be8cfa1ccf9f91eb74
from netCDF4 import Dataset
import numpy as np
import seawater as sw 

<<<<<<< HEAD
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

=======
dataset = Dataset(r'/Users/brownscholar/Desktop/dataset-armor-3d-rep-weekly_1581373134952.nc')

pressure = dataset['depth']
temperture = dataset['to']
salinity = dataset['so']

print(pressure.shape)
print(temperture.shape)
print(salinity.shape)

pressure_3d = np.zeros((31,80,27))

# for depth_level in pressure:
# 	print(np.repeat(depth_level,80*27).reshape((80,27)))


for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
	#print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
density = density-1000

print(density.shape)

for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			print(i,j,k)
>>>>>>> 507f30019f87660c645769be8cfa1ccf9f91eb74
