#https://www.google.com/maps/@32.8147017,-97.3223419,15z
# CLEAN UP BAD GPS WITH ERROR HANDLING

import datetime
import os

import piexif
from Tkinter import Tk
from tkFileDialog import askdirectory

global vFnum
vFnum=""
global vExpT
vExpT=""
global vISO
vISO =""
global vGPSLat
vGPSLat = ""
global vGPSLon
vGPSLon=""
global vDateT
vDateT = ""
global vLatRef
vLatRef = ""
global vLonRef
vLonRef =""
global vAlt
vAlt = ""

adate = datetime.datetime.now()
cdate = adate.strftime("%Y%m%d%H%M")

# Open a dialog box to select a file
Tk().withdraw()
directory = askdirectory()
vHTML = ""
numimg = 0
header = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"><html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>report.htm</title></head><body><a target="_blank" href="coverage.html"><span style="font-family: Courier New,Courier,monospace;">Coverage Map</span></a><br><table style="text-align: left; width: 100%;" border="1" cellpadding="2" cellspacing="2"><tbody><tr><td style="font-family: Courier New,Courier,monospace;"><h5>Filename</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>Date &amp; Time</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>Grade</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>F-Stop</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>Exposure</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>Shutter Speed</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>Coordinates</h5></td><td style="font-family: Courier New,Courier,monospace;"><h5>Altitude</h5></td></tr><tr>'

# Pull up the directory and interate through all .JPG files
file = open(directory + "/" + "quick-report.html", "w")
for filename in os.listdir(directory):
    if filename.endswith(".JPG"):
        fName = os.path.join(directory, filename)
        sName = filename
        # Load exif dictionary for our image
        exif_dict = piexif.load(fName)
        numimg = numimg + 1
        for ifd in ("0th", "Exif", "1st", "GPS"):
            for tag in exif_dict[ifd]:
                if (piexif.TAGS[ifd][tag]["name"]) == "FNumber":
                    vFnum = str(float(exif_dict[ifd][tag][0]) / float(exif_dict[ifd][tag][1]))
                if (piexif.TAGS[ifd][tag]["name"]) == "ExposureTime":
                    vExpT = str(exif_dict[ifd][tag][0]) + "/" + str(exif_dict[ifd][tag][1])
                if (piexif.TAGS[ifd][tag]["name"]) == "ISOSpeedRatings":
                    vISO = (exif_dict[ifd][tag])
                if (piexif.TAGS[ifd][tag]["name"]) == "ExposureBiasValue":
                    vExpB = str(exif_dict[ifd][tag][0]) + "/" + str(exif_dict[ifd][tag][1])
                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLatitudeRef":
                    vLatRef = exif_dict[ifd][tag][0]
                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLongitudeRef":
                    vLonRef = exif_dict[ifd][tag][0]
                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLatitude":
                    vGPSLat = float(exif_dict[ifd][tag][0][0]) + (float(exif_dict[ifd][tag][1][0]) / 600) / 1000
                if (piexif.TAGS[ifd][tag]["name"]) == "GPSLongitude":
                    vGPSLon = float(exif_dict[ifd][tag][0][0]) + (float(exif_dict[ifd][tag][1][0]) / 600) / 1000
                if (piexif.TAGS[ifd][tag]["name"]) == "GPSAltitude":
                    vAlt = str(exif_dict[ifd][tag][0]/10)
                if (piexif.TAGS[ifd][tag]["name"]) == "DateTime":
                    vDateT = exif_dict[ifd][tag]
        print numimg

        if vLatRef != "":
            if vLatRef == "S":
                vGPSLat = vGPSLat * -1
            if vLonRef == "W":
                vGPSLon = vGPSLon * -1

        vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace;"><a href="' + sName + '">' + sName + '</a></td>'

        vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace;">' + vDateT +'</td>'



        vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace; color: red; font-weight: bold;"></td>'

        vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace;">' + str(vFnum) + '</td>'

        if int(vISO) < 1000:
            vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace;">' + str(vISO) +'</td>'
        else:
            vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace; color: red; font-weight: bold;">' + str(vISO) + '</td>'

        if vExpT <> "1/2000":
            vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace; color: red; font-weight: bold;">' + str(vExpT) + '</td>'
        else:
            vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace; ">' + str(vExpT) + '</td>'

        vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace;"><a href="https://www.google.com/maps/@' + str(vGPSLat) + ',' + str(vGPSLon) +',15z">'+ str(vGPSLat) + ',' + str(vGPSLon) + '</td>'

        vHTML = vHTML + '<td style="font-family: Courier New,Courier,monospace;">' + str(vAlt) +'</td></tr>'

        vFnum = ""
        vExpT = ""
        vISO = ""
        vGPSLat = ""
        vGPSLon = ""
        vDateT = ""
        vLatRef = ""
        vLonRef = ""
        vAlt = ""

vHTML = header + vHTML

file.write(vHTML)
file.close()
print str(numimg) + " images processed in " + str(datetime.datetime.now() - adate)
