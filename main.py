import os

folderpath="C:/Users/DELL/PycharmProjects/DFP40203_MK10_Selasa/file"

files=os.listdir(folderpath)

for file in files:
    print (file)