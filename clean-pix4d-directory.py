import datetime
import os
import shutil
from shutil import copyfile

# save .p4d file
# move report pdf to root
# move ortho, prj, tfw to root
# move dsm, prj, tfw to root

adate = datetime.datetime.now()
cdate = adate.strftime("%Y%m%d%H%M")

# Open a dialog box to select a file
#Tk().withdraw()
#directory = askdirectory()
#print directory + "/"

path = 'C:/Users/josh/Desktop/1383_20190613-2015/1383_20190613-2015'
rootpath = os.path.dirname(path)

try:
    # start with moving the report pdf
    pdfdir = path + '/1_initial/report/'
    for filename in os.listdir(pdfdir):
        if filename.endswith(".pdf"):
            fName = os.path.join(pdfdir, filename)
            print fName
            copyfile(fName, rootpath + '/' + filename)
except:
    print "The 1_initial directory may already have been deleted"


# remove all jpgs
filelist = [f for f in os.listdir(rootpath) if f.endswith(".JPG")]
for f in filelist:
    os.remove(os.path.join(rootpath, f))


# Remove the first directory
try:
    shutil.rmtree(path + '/1_initial/')
except:
    print "1_initial does not exist"

try:
    shutil.rmtree(path + '/2_densification/')
except:
    print "3_densification does not exist"

try:
    shutil.rmtree(path + '/temp/')
except:
    print "temp does not exist"

try:
    shutil.rmtree(path + '/3_dsm_ortho/1_dsm/tiles/')
except:
    print "/3_dsm_ortho/1_dsm/tiles/ does not exist"

try:
    shutil.rmtree(path + '/3_dsm_ortho/2_ortho/tiles/')
except:
    print "ortho tiles directory does not exist"

try:
    shutil.rmtree(path + '/3_dsm_ortho/project_data/')
except:
    print "project_data does not exist"

try:
    shutil.rmtree(path + '/temp/')
except:
    print "temp directory not found"


'''
numimg = 0

for filename in os.listdir(directory):
    if filename.endswith(".JPG"):
        fName = os.path.join(directory, filename)
        sName = filename
        print sName
        numimg = numimg + 1


filelist = glob.glob(directory + "/*.jpg")
for jpg in filelist:
    os.remove(jpg)

for root, dirs, files in os.walk(directory, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))'''