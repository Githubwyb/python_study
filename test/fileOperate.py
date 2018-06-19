import os
import os.path
import shutil
import time,  datetime

path = '.\\'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        if file.find('_H') != -1:
            os.remove(os.path.join(path, file))
        if file.find('_N') != -1:
            newname = file[:-2] + '_H'
            shutil.copyfile(os.path.join(path, file), os.path.join(path, newname))
        print(file, 'ok')