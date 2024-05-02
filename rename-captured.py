import datetime
import os
import random

import piexif
from Tkinter import Tk
from tkFileDialog import askdirectory

inputs = 0
keeps = 0
nogps = 0

adate = datetime.datetime.now()
cdate = adate.strftime("%Y%m%d%H%M")

# Open a dialog box to select a file
Tk().withdraw()
directory = askdirectory()

def getimageprops(imagepath):
    exif_dict = piexif.load(imagepath)
    for tag in exif_dict["GPS"]:
        if (piexif.TAGS["GPS"][tag]["name"]) == "GPSLatitudeRef":
            a = exif_dict["GPS"][tag][0]
        if (piexif.TAGS["GPS"][tag]["name"]) == "GPSLongitudeRef":
            b = exif_dict["GPS"][tag][0]
        if (piexif.TAGS["GPS"][tag]["name"]) == "GPSLatitude":
            c = ("{0:.4f}".format(float(exif_dict["GPS"][tag][0][0]) + (float(exif_dict["GPS"][tag][1][0]) / 600) / 1000))
        if (piexif.TAGS["GPS"][tag]["name"]) == "GPSLongitude":
            d = ("{0:.4f}".format(float(exif_dict["GPS"][tag][0][0]) + (float(exif_dict["GPS"][tag][1][0]) / 600) / 1000))
    for tag in exif_dict["Exif"]:
        if (piexif.TAGS["Exif"][tag]["name"]) == "DateTimeDigitized":
            e = exif_dict["Exif"][tag][2:4]  + exif_dict["Exif"][tag][5:7] + exif_dict["Exif"][tag][8:10] + exif_dict["Exif"][tag][11:13] + exif_dict["Exif"][tag][14:16] + exif_dict["Exif"][tag][17:19]

    try:
        a
    except NameError:
        a = ""

    try:
        b
    except NameError:
        b = ""

    try:
        c
    except NameError:
        c = ""

    try:
        d
    except NameError:
        d = ""

    try:
        e
    except NameError:
        e = ""

    return a,b,c,d,e   # Lat Ref, Long Ref, Latitude, Longitude, Date/Time


def mvimage(curloc, futloc):

    try:
        os.rename(curloc, futloc)

    except:
        dupdir = str(directory) + "/DUPLICATES/"
        if not os.path.exists(dupdir):
            os.makedirs(dupdir)

        duploc = dupdir + os.path.splitext(os.path.basename(futloc))[0]+ str(random.randint(100000,999999)) + '.JPG'
        os.rename(curloc, duploc)

        print("Duplicate File: " + duploc)


for root, dirs, files in os.walk(directory):
    for file in files:
        ext = [".JPG", ".jpg"]
        if file.endswith(tuple(ext)):
            laR, loR, Lat, Lon, DT = getimageprops(root + "/" + file)
            inputs = inputs + 1
            if Lat != "":
                # MOVE GOOD FILES TO ROOT HERE
                vGPSData = str(Lat).replace('.', '').zfill(7) + str(laR) + str(Lon).replace('.', '').zfill(7) + str(loR)
#                mvimage(root + '/' + file, directory + '/' + vGPSData + DT + '.JPG')
                mvimage(root + '/' + file, directory + '/' + DT + '_' + vGPSData + '.JPG')
                keeps = keeps + 1
                #print str(file)
            else:
                # THESE FILES ARE GOING TO THE NO-GPS FOLDER
                # WE'LL USE A SEPARATE FUNCTION SO IT CAN HANDLE DUPLICATES
                noGPSDir = str(directory) + "/NO-GPS/"
                if not os.path.exists(noGPSDir):
                    os.makedirs(noGPSDir)
                nogps = nogps + 1
                mvimage(root + '/' + file, noGPSDir + DT + '_NO-GPS_.JPG')

print str(inputs) + ' Input Files  | ' + str(keeps) + ' Good Files  | ' + str(nogps) + ' Bad GPS Files  ' + 'processed in ' + str(datetime.datetime.now() - adate)