# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all 
# the way till n.png where n is the number of png files in that folder. 
# Do the same for other file formats. For example:
# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png
import os

def rename_files():
    folder_path=input("Enter the path: ")
    file_type = input("Enter File Type: ")
    files = os.listdir(folder_path)
    n=int(input("Number of Files You Want To Rename: "))
    for i in range(0,n):
        file_name = files[i]
        old_path = os.path.join(folder_path,file_name)
        new_name =  f"{i+1}.{file_type}"
        new_path = os.path.join(folder_path,new_name)
        os.rename(old_path,new_path)
        print(f"Renamed: {file_name} to {new_name}")
    
rename_files()