#Importing the packages
import os
import shutil
import time

#Determining path
path_i = input('Enter path from which files should be taken (To move the files given in the project, enter path of Given_Files as in your device) >> ')

if(path_i == ''):
    from_dir = "C:/Users/JISHNU D/Downloads/C111-Project/Given_Files"
else:
  if(os.path.exists(path_i)):
    from_dir = path_i
  else:
    print('This path does not exist.')

path_o = input('Enter path of Downloaded_Files of C111-Project of your device >>')

isExists = os.path.exists(path_o)

if(path_o == ''):
  to_dir ="C:/Users/JISHNU D/Downloads/C111-Project/Downloaded_Files"
else:
  if(isExists == False):
   print("path does not exist")
  elif(isExists == True):
   to_dir = path_o



#Getting the list of files in the path
list_of_files = os.listdir(from_dir)
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
    path = shutil.move(path,dest)
    repitition += 1

    print(repitition,"/",len(list_of_files),end="\r")
    time.sleep(1)

print('Moved All Files')

