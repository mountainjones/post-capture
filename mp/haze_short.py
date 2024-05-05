import cv2
import image_dehazer

# import io
# import multiprocessing as mp
# import os
# from datetime import datetime
# from multiprocessing import Pool
# from tkinter import Tk
# from tkinter.filedialog import askdirectory
#
# import platform
# import requests


# def worker(inputstring):
#     os.system(inputstring)
#     #print(inputstring)
#     return

# def worker (HazeImg):

    # if __name__ == "__main__":
HazeImg = cv2.imread("E:\\stage\MM012166\\muenster-4804-12166\muenster-10\\4804-hst\\cap-1217_cal_clip.jpg")  # read input image -- (**must be a color image**)
HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, C1=200, boundaryConstraint_windowSze=70, showHazeTransmissionMap=False)  # Remove Haze

        ##cv2.imshow('haze_map', haze_map);						# display the original hazy image
        ##cv2.imshow('enhanced_image', HazeCorrectedImg);			# display the result
        ##cv2.waitKey(0)

cv2.imwrite("E:\\stage\MM012166\\muenster-4804-12166\muenster-10\\4804-hst\\cap-1217_cal_dh.jpg", HazeCorrectedImg)
    # return


# if __name__ == '__main__':
#     # Check for max cores
#     # print(mp.cpu_count())
#     finalCPU = 0
#     cpuCount = mp.cpu_count()
#     if cpuCount >= 60 :
#         finalCPU = 60
#     else:
#         finalCPU = cpuCount
#
#     if cpuCount != finalCPU:
#         print('Capping cores at ' + str(finalCPU) )
#     else:
#         print('Utilizing all ' + str(finalCPU) + ' cores')
#
#     pool = Pool(processes=finalCPU)
#
#     pool.map(worker, "G:\\data\\muenster-10\\4804-hst\cap-1217_cal.jpg")
#     pool.close()
#     pool.join()



    # # Open a dialog box to select a file
    # Tk().withdraw()
    # dirx = askdirectory()

# ##################
#     stTime = datetime.now()
#
#     if not os.path.exists(dirx + '/hist'):
#         os.makedirs(dirx + '/hist')
#
#     cmdlist = []


    # numFiles = 0
    # for root, dirs, files in os.walk(dirx, topdown=False):
    #     for name in files:
    #         if name.endswith(".jpg"):
    #             fname = os.path.join(root, name)
    #             cmdlist.append("python.exe C:/dev/true-capture/post-capture/mp/contrast-impv-cmd-line.py " + str('"' + fname + '"'))
    #             numFiles = numFiles +1
