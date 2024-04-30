import piexif
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import shutil

from datetime import datetime

adate = datetime.now()
cdate = adate.strftime("%Y%m%d%H%M")

# Open a dialog box to select a file
Tk().withdraw()
directory = askdirectory()

#directory = r"C:\Users\josh\Desktop\testpops"

ctr = 0
numimg = 0

listlat = []
listlon = []
listdate = []
listfile = []
listDate = []

errorsYN = False

# To center map fill these coords last
vLastLat = 11.11
vLastLon = 11.11


# Iterate the directory and move bad GPS into a folder
for filename in os.listdir(directory):
    if filename.endswith((".jpg", ".JPG")):
        fName = os.path.join(directory, filename)
        # Load exif dictionary for our image
        exif_dict = piexif.load(fName)
        exifTest = ""
        for ifd in ("0th", "Exif", "1st", "GPS"):
            for tag in exif_dict[ifd]:
                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLatitudeRef":
                    exifTest =exif_dict[ifd][tag].decode('UTF-8')
        if exifTest == "":
            if not os.path.exists(directory + '/no-gps'):
                os.makedirs(directory + '/no-gps')
            shutil.move(fName, directory + '/no-gps/' + filename)

# Pull up the directory and iterate through all .JPG files for GPX
for filename in os.listdir(directory):
    if filename.endswith((".jpg", ".JPG")):
        fName = os.path.join(directory, filename)
        sName = filename

        # Load exif dictionary for our image
        exif_dict = piexif.load(fName)
        numimg = numimg + 1
        for ifd in ("0th", "Exif", "1st", "GPS"):
            vLatRef = ""
            vLonRef = ""
            for tag in exif_dict[ifd]:

                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLatitudeRef":
                    vLatRef = exif_dict[ifd][tag].decode('UTF-8')

                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLongitudeRef":
                    vLonRef = exif_dict[ifd][tag].decode('UTF-8')

                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLatitude":
                    vGPSLat = float(exif_dict[ifd][tag][0][0]) + (float(exif_dict[ifd][tag][1][0]) / 600) / 1000

                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLongitude":
                    vGPSLon = float(exif_dict[ifd][tag][0][0]) + (float(exif_dict[ifd][tag][1][0]) / 600) / 1000

                if (piexif.TAGS[ifd][tag]["name"]) == "DateTimeOriginal":
                    vDateT = str(exif_dict[ifd][tag].decode('utf-8'))
                    vDateT = datetime.strptime(vDateT, "%Y:%m:%d %H:%M:%S").isoformat()

            if vLatRef == "S":
                vGPSLat = vGPSLat * -1

            if vLonRef == "W":
                vGPSLon = vGPSLon * -1

        listfile.append(sName)
        listlat.append(vGPSLat)
        listlon.append(vGPSLon)
        listdate.append(vDateT)

        vLastLat = vGPSLat
        vLastLon = vGPSLon

# Load waypoints from .waypoints file into

from os.path import basename

newname = basename(directory).replace(" ", "-")

output_fname = directory + '/_gps' + newname + '.gpx'

import io

file = io.open(output_fname, "w+", encoding="utf-8", newline="\n")
file.write("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n""")
file.write("""<gpx xmlns="http://www.topografix.com/GPX/1/1" version="1.1" creator="Prius Intelli">\n""")

for lat in range(0, len(listlat)):
    ctr = ctr + 1
    file.write(
        '    <wpt lon="' + str(float(listlon[int(lat) - 1])) + '" lat="' + str(float(listlat[int(lat) - 1])) + '">\n')
    file.write("        <name>" + str(listfile[int(lat) - 1]) + "</name>\n")
    file.write('        <time>' + str(listdate[int(lat) - 1]) + "</time>\n")
    file.write('    </wpt>\n')
file.write("</gpx>\n")
file.close()

print('Output file: ' + output_fname)
