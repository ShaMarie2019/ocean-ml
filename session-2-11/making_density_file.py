from netCDF4 import Dataset
import numpy as np
<<<<<<< HEAD
import seawater as sw 

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

# first step: iomport the data and get temp, salinity pressure 

pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so']



print(pressure.shape)
print(temperture.shape)
print(salinity.shape)

#second step: make the pressure data 3 dimensional 

pressure_3d = np.zeros((31,80,27)) # this is a empty array that is created using the lon and lat 

# lvl_1 = np.repeat(10,80*27)

# lvl_2 = np.repeat(20,80*27)

for depth_level in pressure:
	print(np.repeat(depth_level,80*27).reshape((80,27)))
	

for i in range(0,31):
	#print(np.repeat(pressure[i],80*27).reshape((80,27)))
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))
	print(pressure_3d[i,:,:])

density = sw.dens(salinity[:],temperture[:],pressure_3d)
print(density)
# to do: 

#imputs: salinity, tempature, pressure in form of netcdf file 
=======
import seawater as sw

dataset = Dataset(r'/Users/helenfellow/Documents/cnn_paper/data/dataset-armor-3d-rep-weekly_1574699840388.nc')
# first step: import the data and get temp, salinity pressure
temperature = dataset['to']
salinity = dataset['so']
pressure = dataset['depth']

print(temperature.shape)
print(salinity.shape)
print(pressure.shape)

print(pressure[:])
#second step: make the pressure data 3 dimenional


pressure_3d = np.zeros((31,80,27))

# first_layer = np.repeat(10,80*27).reshape(80,27)

# second_layer = np.repeat(20,80*27).reshape(80,27)

 # for depth_level in pressure[:]:
 # 	print(np.repeat(depth_level,80*27).reshape((80,27)))
#print(pressure[:])
for i in range(0,31):
	pressure_3d[i,:,:] = np.repeat(pressure[i],80*27).reshape((80,27))

#salinity = float(salinity)
#temperature = float(temperature)

density = sw.dens(salinity[:],temperature[:],pressure_3d)

print(density)
# to do: 

# inputs: salinity, temperature, pressure in form of netcdf file
>>>>>>> 507f30019f87660c645769be8cfa1ccf9f91eb74

