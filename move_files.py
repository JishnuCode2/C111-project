#Importing the packages
import os
import shutil
import time

#Determining path
from_dir = "C:/Users/JISHNU D/Downloads"

to_dir ="C:/Users/JISHNU D/Desktop/Ordered_Files"



#Getting the list of files in the path
list_of_files = os.listdir(from_dir)
print(list_of_files)
repitition = 0
print('Moving -->')
for file in list_of_files:
    path = f"{from_dir}/{file}"
    root_ext=os.path.splitext(file)
    type = root_ext[1]

    if(type == '.txt'):
        doc_type = "Document_Files" 
    elif(type == '.png'):
        doc_type = "Image_Files"
    elif(type == '.jpg'):
        doc_type = "Image_Files"
    elif(type == '.pdf'):
        doc_type = "Document_Files"
    elif(type == '.zip'):
        doc_type = "Document_Files" 
    elif(type == '.jpg'):
        doc_type = "Image_Files"
    elif(type == ''): 
        doc_type = "Folders"
    elif(type == '.apk'):
        doc_type = "Document_Files"
    elif(type == '.exe'):
        doc_type = "Document_Files"
    elif(type == '.ipynb'):
        doc_type = "Document_Files"
    
    dest = f"{to_dir}/{doc_type}"
    print(file,dest)
    path = shutil.move(path,dest)
    repitition += 1
    print(repitition,"/",len(list_of_files),end="/r")
    time.sleep(1)

print('Moved All Files')

