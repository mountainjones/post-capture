from multiprocessing import Pool
import multiprocessing as mp
import os,io
from tkinter import Tk
from tkinter.filedialog import askdirectory
from datetime import datetime
import requests, platform

def worker(inputstring):
    os.system(inputstring)
    #print(inputstring)
    return

if __name__ == '__main__':
    # Check for max cores
    # print(mp.cpu_count())
    finalCPU = 0
    cpuCount = mp.cpu_count()
    if cpuCount >= 60 :
        finalCPU = 60
    else:
        finalCPU = cpuCount

    if cpuCount != finalCPU:
        print('Capping cores at ' + str(finalCPU) )
    else:
        print('Utilizing all ' + str(finalCPU) + ' cores')


    # Open a dialog box to select a file
    Tk().withdraw()
    dirx = askdirectory()

##################
    stTime = datetime.now()

    if not os.path.exists(dirx + '/hist'):
        os.makedirs(dirx + '/hist')

    cmdlist = []
    pool = Pool(processes=finalCPU)

    numFiles = 0
    for root, dirs, files in os.walk(dirx, topdown=False):
        for name in files:
            if name.endswith(".jpg"):
                fname = os.path.join(root, name)
                cmdlist.append("python.exe C:/dev/true-capture/post-capture/mp/contrast-impv-cmd-line.py " + str('"' + fname + '"'))
                numFiles = numFiles +1

    pool.map(worker, cmdlist)
    pool.close()
    pool.join()

    endTime = datetime.now()
    duration = endTime - stTime
    payload = str(stTime) + ', ' + str(endTime) + ', ' + str(duration) + ', ' + str(dirx)+ ', ' + str(numFiles)

    url = "https://aptus-oms.priusintelli.com/logz/"
    import json

    data = {
        "computer": str(platform.node()),
        "process": 'Contrast',
        "project": "",
        "status": 'Success',
        "starting": str(stTime),
        "ending": str(endTime),
        "location": str(dirx),
        "message": str(numFiles) + ' files processed',
        "sendEmail": "true",
        "emailAddress": "monitoring@priusintelli.com",
    }

    print(json.dumps(data))


    try:
        x = requests.post(url, data=data)
        if x.status_code == 200:
            print('Success Logging to OMS db')
        else:
            print('Data was sent, but an error occured on the server')
    except:
        print('endpoint offline')

    try:
        if not os.path.exists('C:/storage'):
            os.makedirs(dirx + 'C:/storage')

        file = io.open("C:/storage/contrast-log.csv", "a+", encoding="utf-8", newline="\n")
        file.write("{}\n".format(payload))
        file.close()
        print('Success logging to local csv file')

    except:
        print('C:\storage\contrast-log.csv does not exist or is corrupted.')
