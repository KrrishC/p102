import os 
import shutil

source = "C:/Users/FiercePC/Downloads/abc"
destination = "C:/Users/FiercePC/Desktop"

files = os.listdir(source)
for i in files:
    name , ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in [".ppt",".txt","pdf",".docx"]:
        path1 = source + "/" + i
        path2 = destination + "/" + "document_files"
        path3 = destination + "/" + "document_files" + "/" + i
        if os.path.exists(path2):
            print("folder already exists and moving the files ... ")
            shutil.move(path1, path3)
        else :
            os.makedirs(path2)
            print("creating the folder and moving the files ...")
            shutil.move(path1,path3)
       



   
