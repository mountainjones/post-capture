import os
import datetime

# REQUIRES A CSV FILE WITH SIMPLE FILENAMES AND ONE HEADER LINE
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

from shutil import copyfile

# Open a dialog box to select a file
Tk().withdraw()
filename = askopenfilename(initialdir = "C:/w/",title = "Select CSV file",filetypes=[("CSV files","*.csv")])
directory = askdirectory(initialdir = "E:/calibrated-tiff/Cal-TIFF/Calibrated RGB/",title='Source Directory of Images')
destdir = askdirectory(initialdir = "C:/w/",title='Destination Directory of Images')

sfilename , sext = os.path.splitext(os.path.basename(filename))

now = datetime.datetime.now()
csvfile = filename
imgdir = directory
#newdir = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute)


rc = open(csvfile, "r")
row_count = (sum(1 for row in rc) - 1)


files = []
f = open(csvfile, "r")

f.readline()
for x in f:
    files.append(x)

print(destdir + "/" + sfilename)
os.mkdir(destdir + "/" + sfilename )

for a in range(0, len(files)):
    copyfile(imgdir + "/" + str(files[a]).rstrip('\r\n'), destdir + "/" + sfilename + "/" + str(files[a]).rstrip('\r\n'))
    print(str(a+1) + ' of ' + str(row_count), imgdir + "/" + str(files[a]).rstrip('\r\n'), destdir + "/" + str(files[a]).rstrip('\r\n'))
