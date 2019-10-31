from netCDF4 import Dataset
import numpy.ma as ma

# import the netcdf file using Dataset

dataset = Dataset(r'/Users/brownscholar/Desktop/Intern_Git/ocean-ml/session-10-31/ssh_1572470095877.nc')

# read in and create variable for lat:
lat = dataset['latitude']
# lon:
lon = dataset['longitude']
# adt:
adt = dataset['adt']

# print shape of the adt variable:
#print("longitude",lon.shape)
#print("latitude", lat.shape)
#print("adt", adt.shape)

# you will need this:
BATS_lat_max = 39.453
BATS_lon_max = 360 -59.648999999999994 # converting from degrees west to degrees east
BATS_lat_min = 19.663 
BATS_lon_min = 360 -66.211 #same

#print(lat[:])

lat_index = set()
index = 0

for i in lat:
	if i > BATS_lat_min and i < BATS_lat_max:
		lat_index.add(index)
	index += 1 

lon_index = set()
index_2 = 0

for i in lon:
	if i > BATS_lon_min or i < BATS_lon_max:
		lon_index.add(index_2)
	index_2 += 1 

lat_min = min(lat_index)
lat_max = max(lat_index)

lon_min = min(lon_index)
lon_max = max(lon_index)

BATS_adt = adt[:,lat_min, lat_max, lon_min, lon_max]

print(BATS_adt.shape)
print( min_lat_index, max_lat_index)
print(min_lon_index, max_lon_index)

#print(lat_index)
















