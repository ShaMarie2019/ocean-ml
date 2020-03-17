# to do 
from netCDF4 import Dataset
import numpy as np
import seawater as sw 
import datetime as td
import interpolate
import tricubic

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset ['depth']
temperture = dataset['to']
salinity = dataset['so'] 
pressure_3d = np.zeros((31,80,27)) 
density = sw.dens(salinity[:,:,:,:],temperture[:,:,:,:],pressure_3d)
density = density - 1000
time = dataset["time"]
#density_onetime = density[100,:,:,:]
#density_onetime = density
#print(density_onetime.shape)
#print(density.shape) = (1356, 31, 80, 27)

start = td.date(1950,1,1)

for i in range(0,1356):
	hours = td.timedelta(hours = int(time[i]))
	after = start + hours 
	date = after.strftime("%y") + after.strftime("%m") + after.strftime("%d")
	date = open('date_' + str(date) +  '.txt','w')
	density_at_time = interp(density[i,:,:,:])

	for item in range(0,30):
		for sat in range(0,80):
			for love in range(0,27):
				date.write(str(density[item,sat,love]) + "\n")
	date.close()

