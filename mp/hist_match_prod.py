import io
import multiprocessing as mp
import os
from datetime import datetime
from multiprocessing import pool
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import cv2
from skimage import exposure
from skimage.exposure import match_histograms
import piexif

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

    #Open windoe to select file as source histogram
    Tk().withdraw()
    srcfileraw = askopenfilename(title='Select image to match others to.')
    print(srcfileraw)
    srcfile = str.replace(srcfileraw, "/", "\\\\")
    print(srcfile)


    # reading reference image
    img2 = cv2.imread(srcfile)

    # Open a dialog box to select dirctory of images to be matched
    Tk().withdraw()
    dirx = askdirectory()

    stTime = datetime.now()

    if not os.path.exists(dirx + '/matched'):
        os.makedirs(dirx + '/matched')

    numFiles = 0
    for root, dirs, files in os.walk(dirx, topdown=False):
        with mp.Pool(processes=finalCPU) as pool:
            for name in files:
                if name.endswith(".jpg"):
                    fnameraw = os.path.join(root, name)
                    fname = str.replace(fnameraw, "/", "\\\\")
                    print(fname)
                    filename = os.path.basename(fname)  # only the filename
                    print(filename)
                    img1 = cv2.imread(fname)
                    image = img1
                    reference = img2
                    matched = match_histograms(image, reference, channel_axis=-1)
                    ##multichannel=True)
                    numFiles = numFiles + 1
                    newname = dirx + '/matched/' + filename
                    print (matched)
                    ##image = cv2.imread(matched)
                    # clnimg = histomagic(image)
                    cv2.imwrite(newname, matched)
                    piexif.transplant(fname, newname)
                pool.close()
                pool.join()

