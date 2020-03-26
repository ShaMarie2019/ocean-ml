# to do 
from netCDF4 import Dataset
import numpy as np
import seawater as sw 
import datetime as td
import tricubic

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/Downloads/dataset-armor-3d-rep-weekly_1574699840388.nc')

pressure = dataset ['depth'][:]
temperture = dataset['to'][:]
salinity = dataset['so'][:]
pressure_3d = np.zeros((31,80,27)) 
density = sw.dens(salinity[:,:,:,:],temperture[:,:,:,:],pressure_3d)
density = density - 1000
time = dataset["time"][:]

def interp(startgrid): #this function is created so that we can add in the number that is missing and also so that it goes by 10's
	num_depths = 30 # to avoid problems with seafloor depth
	z_step = 10 
	depth_list = [10, 20, 30, 50, 75, 100, 125, 150, 200, 250, 300, 400]

	new_depth = np.arange(z_step,(num_depths+1)*z_step,z_step) 
	new_depth_index = []
	left = 0
	right = 1
	for i in range(0,len(new_depth)):   
		target_value = new_depth[i]
		if target_value > depth_list[right]:
			right += 1
			left +=1
		left_value = depth_list[left]
		right_value = depth_list[right]
		a = target_value-left_value
		b = right_value-left_value
		new_index = a/b+left
		new_depth_index.append(new_index)
		#start grid is shape lat,lon,depth
		lat = startgrid.shape[1]
		lon = startgrid.shape[2]
		depth = startgrid.shape[0]

	interp_grid = np.zeros((len(new_depth_index),lat,lon))
	ip = tricubic.tricubic(list(startgrid),[depth,lat,lon])

	for i in range(0,lat):
		for j in range(0,lon):
			for k in range(0,len(new_depth_index)):
				res = ip.ip([new_depth_index[k],i,j])
				interp_grid[k,i,j] = res

	return interp_grid

start = td.date(1950,1,1)
geo_2 = dataset["zo"][:]


for i in range(0,1356):   # thi s for loop is being used to create files for each of the dates 
	hours = td.timedelta(hours = int(time[i]))
	after = start + hours 
	date = after.strftime("%y") + after.strftime("%m") + after.strftime("%d")
	den= open('/Users/brownscholar/Desktop/Intern_Git/files/marine_capernicus_density/density' + date +  '.gr','w')
	den.write("\t30\n\t80\t27\n")
	density_at_time = interp(density[i,:12,:,:])
	geo = open('/Users/brownscholar/Desktop/Intern_Git/files/marine_capernicus_dh/geo' + date +  '.gr','w')
	geo.write("\t30\n\t80\t27\n")
	geo_at_time = interp(geo_2[i,:12,:,:]) * 100 
	for item in range(0,30):
		for sat in range(0,80):
			for love in range(0,27):
				den.write(str(density_at_time[item,sat,love]) + "\n")
				geo.write(str(geo_at_time[item,sat,love]) + "\n")
	den.close()
	geo.close()

