import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import time

tiffName = str(int(time.time())) + '.tif'  # Assign a unique value to the filename and append a "tif" suffix

Tk().withdraw()
dirx = askdirectory()

inputTiffs = ''
dirx = dirx + '/'

for filename in os.listdir(dirx):
    if filename.endswith('tif'):
        if inputTiffs != '':
            inputTiffs = inputTiffs + ' "' + dirx + filename + '"'
        else:
            inputTiffs = '"' + dirx + filename + '"'

print('gdalwarp -multi ' + inputTiffs + ' "' + dirx + tiffName + '" --config GDAL_CACHEMAX 90%% -wm 2047 -wo NUM_THREADS=ALL_CPUS')

os.system('gdalwarp -multi ' + inputTiffs + ' "' + dirx + tiffName + '" --config GDAL_CACHEMAX 90%% -wm 2047 -wo NUM_THREADS=ALL_CPUS')


