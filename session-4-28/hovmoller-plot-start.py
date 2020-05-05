from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

dataset = Dataset(r'/Users/brownscholar/Desktop/fortran_files/omega.nc')
w = dataset['w']
lat = dataset['latitude']
depth = dataset['depth']
#print(w.shape)
#depth = 0
latitude = 25.375
first_plot = w[:, latitude, :, 0]
first_plot = np.swapaxes(first_plot, 0, 1)
print(first_plot.shape)
#plt.pcolormesh(first_plot, cmap='PiYG') 
plt.title("Hovmoller Diagram at latitude " + str(lat[latitude]))
#plt.colorbar()
#plt.show()

top = cm.get_cmap('Blues_r')
bottom = cm.get_cmap('Reds')
newcolors = np.vstack((top(np.linspace(0, 1, 10)),
                       bottom(np.linspace(0, 1, 10))))
newcmp = ListedColormap(newcolors, name='RedBlue')

plot_one =  w[:,0,:,0]
plot_one = np.swapaxes(plot_one, 0, 1)

plot_two = w[:,0,:,15]
plot_two = np.swapaxes(plot_two, 0, 1)

plot_three = w[:,0,:,29]
plot_three = np.swapaxes(plot_three, 0, 1)

_min = -10
_max = 10

fig, ax = plt.subplots(3,1)
ax[0].pcolormesh(plot_one,cmap=newcmp,vmin = _min, vmax = _max)
ax[0].set_title("plot_one" + str(depth[0]))
ax[1].pcolormesh(plot_two,cmap=newcmp,vmin = _min, vmax = _max)
ax[1].set_title("plot_two" + str(depth[15]))
ax[2].pcolormesh(plot_three,cmap=newcmp,vmin = _min, vmax = _max)
ax[2].set_title("plot_three" + str(depth[29]))
plt.show()


# The higher the number like 60, 70 it makes it so that we can see the lines better






