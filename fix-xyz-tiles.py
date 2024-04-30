import os
from pathlib import Path

directory = 'C:/w/glen-rose-slippy'

for root, dirs, files in os.walk(directory):
    for f in files:
        if f.endswith('.kml'):
            os.remove(root + '/' + f)

        p = Path(root)
        try:
            #print(p.parts[3])
            if 10<= int(p.parts[3]) <= 25:

                #print(p.parts[5], f,pow(2,int(p.parts[5])) - int(os.path.splitext(f)[0])-1)
                #print(f, str(pow(2,int(p.parts[5])) - int(os.path.splitext(f)[0])-1) + '.png')

                #print(p.parts[3])
                os.rename(root + '/' + f, root + '/' + str(pow(2,int(p.parts[3])) - int(os.path.splitext(f)[0])-1) + '.png')
        except:
            print("error")