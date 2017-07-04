# coding:utf-8
# Function: Modify the file name or file postfix

import os
import shutil


def Modifile(file_name,old,new):
    currentdir =os.path.join(Path, file_name) #连接指定的路径和文件名or文件夹名字
    #if os.path.isdir(currentdir):#如果当前路径是文件夹，则跳过
        #continue
    fname = os.path.splitext(file_name)[0] #分解出当前的文件路径名字
    ftype = os.path.splitext(file_name)[1] #分解出当前的文件扩展名
    replname =fname.replace(old,new)
    newname = os.path.join(Path,replname+ftype) #文件路径与新的文件名字+原来的扩展名
    os.rename(currentdir,newname)
    #重命名

for i in range(3,13):
    Path = r'd:\voc\word\%d'%i
    all_file_list = os.listdir(Path)
    for i in range(1,len(all_file_list)+1):
        if i<=9:
            Modifile(all_file_list[i-1],str(all_file_list[i-1][6:9]),'0'+str(i)+'.')
        else:
            Modifile(all_file_list[i-1],str(all_file_list[i-1][6:9]),str(i)+'.')

    
##copy file to another dir
##for item in real_list:
##    shutil.copy(os.path.join(Path,item),r'd:\voc\word\RB')
