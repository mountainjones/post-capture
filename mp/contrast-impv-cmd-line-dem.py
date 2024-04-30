import cv2, os, sys, piexif

# example input:
#    C:\dev\true-capture\single-use-or-testing>python contrast-impv-cmd-line.py C:\w\191103133610_0323292N1009086W.JPG

print(sys.argv[1])

filepath = str(sys.argv[1])


#print(filepath)

filename = os.path.basename(filepath) # only the filename
directory = os.path.dirname(filepath)  # only the directory

def histomagic(inputimg):
    # convert image to LAB color model
    image_lab = cv2.cvtColor(inputimg, cv2.COLOR_BGR2LAB)

    # split the image into L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(image_lab)

    # apply CLAHE to lightness channel
    #clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(10,10))          # USE FOR RGB
    clahe = cv2.createCLAHE(clipLimit=20, tileGridSize=(10,10))        # USE FOR DEM and DSM
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L channel with the original A and B channel
    merged_channels = cv2.merge((cl, a_channel, b_channel))

    # convert iamge from LAB color model back to RGB color model
    final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
    return final_image

newname = directory + '/hist/' + filename
image = cv2.imread(filepath)
clnimg = histomagic(image)
cv2.imwrite(newname,clnimg)
piexif.transplant(filepath, newname)