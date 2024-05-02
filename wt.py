#python3
import os
import requests
import sys
from datetime import datetime


def left(s, amount):
    return s[:amount]
def right(s, amount):
    return s[-amount:]
def mid(s, offset, amount):
    return s[offset:offset+amount]

def logwriter(project):
    print(project)

    url = "https://aptus-oms.priusintelli.com/logz/"

    data = {
    "computer": 'dell-anchor',
    "process": 'WMS tiling',
    "project": project,
    "status": 'Success',
    "starting": str(stTime),
    "ending": str(endTime),
    "location": str(project),
    "message": 'wms tiled and uploaded to staged folder on geoserver',
    "sendEmail": "true",
    "emailAddress": "monitoring@priusintelli.com",
    }

    #print(json.dumps(data))


    try:
        x = requests.post(url, data=data)
        if x.status_code == 200:
            print('Success Logging to OMS db')
        else:
            print('Data was sent, but an error occured on the server')
    except:
         print('endpoint offline')



stTime = datetime.now()


path = sys.argv[1]
obj = os.scandir(path)

logfilepath = path + 'tile.log'

log = open(logfilepath, "a")

stTime = datetime.now()

# Grab a timestamp start up here
start = datetime.now()
files = []
prefixes = []
uploads = []

# Get files and prefixes for tifs in the directory path provided
for entry in obj :
    if entry.is_dir() or entry.is_file():
        if entry.name.endswith('.tif'):
            files.append(str(entry.name))
            prefixes.append(left(entry.name,len(entry.name)-4))


i = 0
# Use the prefixes to create directories
# Then use the filenames and the prefixes to generate the gdal command string and run it
for prefix in prefixes:
    if not os.path.exists(path + prefix):

         d = datetime.now().strftime("%m/%d/%Y %H:%M:%S")            # Get current datetime stamp

         log.write(str(d) +","+ 'mkdir ' + path + prefix + '\n')     # make a log entry for creating the directory (chage to try)
         os.makedirs(path + prefix)                                  # make the directory (change to try)
         # build the tile command
         tilecmd = str('gdal_retile.py -v -r bilinear -levels 8 -ps 1024 1024 -co "COMPRESS=LZW" -co "TILED=YES" -targetDir ' + str(path) + str(prefix) + ' ' + str(path) + str(files[i]) + ' -tileIndex 0.shp -useDirForEachRow')
         os.system(tilecmd)
         log.write(d + ', ' + tilecmd + '\n')
         zipcmd = str('cd ' + str(path) +' && ' + 'zip -r ' + str(path) + str(prefix) + '.zip ' + './' + str(prefix) + ' && cd -')

         newziploc = str(path) + str(prefix) + '.zip'
         uploads.append(newziploc)


         log.write(d + ', ' + zipcmd + '\n')
         os.system(zipcmd)
         i=i+1


for upload in uploads:
    os.system(
        'scp ' + upload + ' azroot@pigeoserver.southcentralus.cloudapp.azure.com:/data_dir/workspaces_data/staged')


endTime = datetime.now()
logwriter(path)