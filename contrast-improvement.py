import datetime
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

import cv2
import piexif


def histomagic(inputimg):
    # convert image to LAB color model
    image_lab = cv2.cvtColor(inputimg, cv2.COLOR_BGR2LAB)

    # split the image into L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(image_lab)

    # apply CLAHE to lightness channel
    clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(10,10))
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L channel with the original A and B channel
    merged_channels = cv2.merge((cl, a_channel, b_channel))

    # convert iamge from LAB color model back to RGB color model
    final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
    return final_image


Tk().withdraw()
dirx = askdirectory()
if not os.path.exists(dirx + '/enhanced'):
    os.makedirs(dirx + '/enhanced')

id = 0
# Pull up the directory and iterate through all .JPG files
for filename in os.listdir(dirx):
    id = id + 1
    if filename.endswith(".jpg"):

        stime = datetime.datetime.now()

        lfname = dirx + '/' + filename

        #newname = dirx + '/hist/' + 'h_' + filename
        newname = dirx + '/enhanced/' + filename

        image = cv2.imread(lfname)
        clnimg = histomagic(image)
        cv2.imwrite(newname,clnimg)
        piexif.transplant(lfname, newname)
        print(str(id) + ' CLAHE --', lfname, newname, ' in ' + str(datetime.datetime.now()- stime))


