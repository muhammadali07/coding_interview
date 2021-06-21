import scipy.io as spio
import numpy as np
import csv

on2file = 'text_classification_english_06052021.sav'   # i/p file
outfile = 'test_classification_english.csv'   # o/p file

# Read i/p file
s = spio.readsav(on2file, python_dict=True, verbose=True)

# Creating Grid
#d_lat = s["d_lat"]
#d_lon = s["d_lon"]
lat = np.arange(-90,90,1.78218)  # (101,)
lon = np.arange(-180,180,1.78218)     # (202,)
ylat,xlon = np.meshgrid(lat,lon)

on2grid = np.asarray(s["on2_grid"])
on2gridsmooth = np.asarray(s["on2_grid_smooth"])

nrows = len(on2grid)
ncols = len(on2grid[0])

xlon_grid = xlon.reshape(nrows*ncols,1)
ylat_grid = ylat.reshape(nrows*ncols,1)
on2grid_new = on2grid.reshape(nrows*ncols,1)
on2gridsmooth_new = on2gridsmooth.reshape(nrows*ncols,1)

# Concatenation
allgriddata = np.concatenate((xlon_grid, ylat_grid, on2grid_new, on2gridsmooth_new),axis=1)

# Writing o/p file
f_handle = file(outfile,'a')
np.savetxt(f_handle,allgriddata,delimiter=",",fmt='%0.3f',header="longitude, latitude, on2_grid, on2_grid_smooth")
f_handle.close()