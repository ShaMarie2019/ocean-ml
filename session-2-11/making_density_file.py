from netCDF4 import Dataset
import numpy as np

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

# first step: iomport the data and get temp, salinity pressure 

pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so']

print(pressure.shape)
print(temperture.shape)
print(salinity.shape)

#second step: make the pressure data 3 dimensional 

pressure_3d = np.zeros((31,80,27))

for i in pressure:
	pressure_3d[i,:,:]

	
# to do: 

#imputs: salinity, tempature, pressure in form of netcdf file 

