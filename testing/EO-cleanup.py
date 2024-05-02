import datetime
import io
import os
from tkinter import
from tkinter.filedialog as fd

Tk().withdraw()

fileDataname = fd.askopenfilename(initialdir = "D:\GPS\PosPac-Projects", title = "Select EO file",filetypes=[("TXT files", "*.txt")])
#fileDataname = 'C:/Users/pi/Documents/POSPac MMS/2022-02-08-eagle/Mission 1/EO/event1_eo_Mission 1.txt'
#fileDataname = 'C:/Users/pi/Documents/POSPac MMS/2022-02-14-permian/Mission 1/EO/event1_eo_Mission 1.txt'

currentDate = datetime.datetime.now()

dateStream = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + '_' + str(currentDate.hour) + str(currentDate.minute) + str(currentDate.second)

print(fileDataname)
directory = os.path.dirname(fileDataname)

fileField = []
latField = []
lonField = []
altField = []
omeField = []
phiField = []
kapField = []

g = open(fileDataname, 'r')



for line in g:
# Change order of Lat/Lon on 2/19/22
    if line[3:6].isdigit():
        if line.find(" ") == 14:
            fileField.append(line[0:14].strip() + '.jpg')
            lonField.append(line[113:126].strip())
            latField.append(line[100:112].strip())
            altField.append(str(float(line[59:68].strip())))  # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[68:79].strip())
            phiField.append(line[80:89].strip())
            kapField.append(line[89:100].strip())

        else:
            fileField.append(line[0:13].strip()+'.jpg')
            lonField.append(line[112:125].strip())
            latField.append(line[99:111].strip())
            altField.append(str(float(line[58:67].strip())))    # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[67:78].strip())
            phiField.append(line[79:88].strip())
            kapField.append(line[88:99].strip())




fileExport = directory + '/'+ dateStream + '_gps-imu-data.csv'
file = io.open(fileExport, "w+", newline="\n")
file.write("Filename, Longitude, Latitude, Altitude, Omega, Phi, Kappa, HorAcc, VertAcc\n")

for b in range(len(fileField)):
    file.write(fileField[b] + ',' + lonField[b] + ',' + latField[b] + ',' + altField[b] + ',' + omeField[b] + ',' + phiField[b] + ',' + kapField[b] + ',0.1,0.3\n')
file.close()

print("File Created")
