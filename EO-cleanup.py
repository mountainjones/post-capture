import datetime
import io
import os
import sys

print (sys.version)


from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

fileDataname = askopenfilename(initialdir = "E:\GPS\PosPac-Projects", title = "Select EO file",filetypes=[("TXT files","*.txt")])
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
    #print (line[0:17])
    #print (line [6:12])
    #print(line[16:18])
    #print(line[17:17])
    if line[6:8].isdigit():
        print(line[0:17])
        #sys.stdout.write(line[0:17])
        #name = (line[0:17])
        #os.system(name)
        if line.find(" ") == 13:
            fileField.append(line[0:12].strip() + '.jpg')
            lonField.append(line[112:124].strip())
            latField.append(line[99:111].strip())
            altField.append(str(float(line[58:67].strip())))  # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[69:77].strip())
            phiField.append(line[80:89].strip())
            kapField.append(line[90:99].strip())
        elif line.find(" ") == 14:
            fileField.append(line[0:13].strip() + '.jpg')
            lonField.append(line[113:125].strip())
            latField.append(line[100:113].strip())
            altField.append(str(float(line[59:68].strip())))  # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[70:78].strip())
            phiField.append(line[81:90].strip())
            kapField.append(line[91:100].strip())
        elif line.find(" ") == 15:
            fileField.append(line[0:14].strip() + '.jpg')
            lonField.append(line[114:126].strip())
            latField.append(line[101:114].strip())
            altField.append(str(float(line[61:69].strip())))  # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[71:79].strip())
            phiField.append(line[82:91].strip())
            kapField.append(line[92:101].strip())
        elif line.find(" ") == 16:
            fileField.append(line[0:15].strip() + '.jpg')
            lonField.append(line[115:127].strip())
            latField.append(line[102:115].strip())
            altField.append(str(float(line[61:70].strip())))  # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[72:80].strip())
            phiField.append(line[83:92].strip())
            kapField.append(line[93:102].strip())
        else:
            fileField.append(line[0:16].strip() + '.jpg')
            lonField.append(line[116:128].strip())
            latField.append(line[103:116].strip())
            altField.append(str(float(line[62:71].strip())))  # for 5 digits, 57:66 for 6 digits 58:67
            omeField.append(line[73:81].strip())
            phiField.append(line[84:93].strip())
            kapField.append(line[94:103].strip())



fileExport = directory + '/'+ dateStream + '_gps-imu-data.csv'
file = io.open(fileExport, "w+", newline="\n")
file.write("Filename, Longitude, Latitude, Altitude, Omega, Phi, Kappa, HorAcc, VertAcc\n")

for b in range(len(fileField)):
    file.write(fileField[b] + ',' + lonField[b] + ',' + latField[b] + ',' + altField[b] + ',' + omeField[b] + ',' + phiField[b] + ',' + kapField[b] + ',0.1,0.3\n')
file.close()

print("File Created")
