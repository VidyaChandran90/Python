import os
import shutil
import datetime
dir_src=('C:\\Users\\Admin\\Downloads')
dir_des={"jpg":"D:\Downloads\Images","pdf":"D:\Downloads\PDF","xls":"D:Downloads\Excel","docx":"D:Downloads\Documents"
         ,"zip":"D:Downloads\ZIP Files","csv":"D:Downloads\CSV Files","exe":"D:Downloads\Executables",
         "xlsx":"D:Downloads\Excel","Others":"D:Downloads\Others"}
DebugFile='D:/Downloads/DebugFiles.txt'
fileExist=False
if os.path.exists(DebugFile):
    mode='a'
else:
    mode='w'
file = open(DebugFile, mode)
file.write('Process Started at '+str(datetime.datetime.now())+'\n')
for key in dir_des:
    try:
        os.mkdir(dir_des[key])
    except FileExistsError:
        file.writelines(dir_des[key]+ ' Directory already Exists\n')
                
for key in dir_des:
    for filename in os.listdir(dir_src):
        if filename.split('.')[-1].upper() == key.upper():
            try:
                shutil.move(dir_src + '\\' + filename, dir_des[key])
            except OSError:
                fileExist=True
                file.writelines(filename + ' already Exists\n')

for filename in os.listdir(dir_src):
    try:
        if fileExist==False:
            shutil.move(dir_src + '\\' + filename, dir_des['Others'])
    except OSError:
        file.writelines(filename + ' already Exists\n')
        pass
file.write('Process Ended at '+str(datetime.datetime.now())+'\n\n')