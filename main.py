import os

folderpath="C:/Users/DELL/PycharmProjects/DFP40203_MK10_Selasa/file"

files=os.listdir(folderpath)

for file in files:
    print (file)

old="C:/Users/DELL/PycharmProjects/DFP40203_MK10_Selasa/file/test.txt"
new="C:/Users/DELL/PycharmProjects/DFP40203_MK10_Selasa/file/testing1.txt"

os.rename(old,new)
print(f"{old} has been renamed to{new}")
