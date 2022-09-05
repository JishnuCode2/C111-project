#Importing the packages
import os
import shutil
import time

#Determining path
from_dir = input('Enter directory to take files from >>')
  #from_dir = "C:/Users/JISHNU D/Downloads"
to_dir = input("Enter folder to move files to >> ")
  #to_dir ="C:/Users/JISHNU D/Desktop/Ordered_Files"

#Making folders at destination
os.mkdir(f"{to_dir}/Document_Files")
os.mkdir(f"{to_dir}/Image_Files")
os.mkdir(f"{to_dir}/Folders")



#Getting the list of files in the path
list_of_files = os.listdir(from_dir)
repitition = 0
print('Moving -->')

#for-in loop
for file in list_of_files:
    path = f"{from_dir}/{file}"
    root_ext=os.path.splitext(file)
    type = root_ext[1]
    
    #To determine which folder the document should be sent to
    if(type == '.txt'):
        doc_type = "Document_Files" 
    elif(type == '.png'):
        doc_type = "Image_Files"
    elif(type == '.jpg' or type == '.jpeg'):
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
    else:
       print('Unknown data type')
       break
    dest = f"{to_dir}/{doc_type}"
    print(file,dest)
    path = shutil.move(path,dest)
    repitition += 1
    print(repitition,"/",len(list_of_files),end="\r")
    time.sleep(1)

print('Moved All Files')

