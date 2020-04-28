from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')
w = dataset['w']
lat = dataset['latitude']
#print(w.shape)
depth = 0
latitude = 25.375
w_lat = w[:, latitude, :, depth]
w_lat = np.swapaxes(w_lat, 0, 1)
print(w_lat.shape)
plt.pcolormesh(w_lat, cmap='PiYG') 
plt.title("Hovmoller Diagram at latitude " + str(lat[latitude]))
plt.colorbar()
plt.show()