import io, os, string, datetime
from datetime import date
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()

fileDataname = askopenfilename(initialdir = "C:/Users/pi/Documents/POSPac MMS/",title = "Select EO file",filetypes=[("TXT files","*.txt")])

currentDate = datetime.datetime.now()

dateStream = str(currentDate.year) + str(currentDate.month) + str(currentDate.day) + str(currentDate.hour) + str(currentDate.minute) + str(currentDate.second)

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
    if line[0:4].isdigit():
        #print(line[96:108].strip(),line[108:122].strip(),line[54:63].strip(), line[63:75].strip(), line[75:85].strip(),line[85:95].strip())

        #print(line[0:10].strip()+'.tif')

        #print(line[96:108], line[109:122],line[54:63],line[63:75], line[75:85], line[85:95])

        # KEEP fileField.append(line[0:10].strip()+'.jpg')
        fileField.append(line[0:6].strip() + '.jpg') #TEMP

        # KEEP latField.append(line[96:108].strip())
        latField.append(line[93:105].strip()) # TEMP

        #KEEP lonField.append(line[108:122].strip())
        lonField.append(line[105:119].strip()) #TEMP

        #KEEP altField.append(str(float(line[54:63].strip())))
        altField.append(str(float(line[51:59].strip())))

        #KEEP omeField.append(line[63:75].strip())
        #KEEP phiField.append(line[75:85].strip())
        #KEEP kapField.append(line[85:95].strip())

        omeField.append(line[60:72].strip())
        phiField.append(line[72:82].strip())
        kapField.append(line[83:92].strip())

fileExport = directory + '/'+ dateStream + '_gps-imu-data.csv'
file = io.open(fileExport, "w+", newline="\n")
file.write("Filename, Latitude, Longitude, Altitude, Omega, Phi, Kappa, HorAcc, VertAcc\n")

for b in range(len(fileField)):
    file.write(fileField[b] + ',' + latField[b] + ',' + lonField[b] + ',' + altField[b] + ',' + omeField[b] + ',' + phiField[b] + ',' + kapField[b] + ',0.1,0.3\n')
file.close()

print("File Created")
