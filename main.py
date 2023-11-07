import os

folderpath = "C:/Users/DELL/PycharmProjects/DFP40203_MK10_Selasa/file"

files = os.listdir(folderpath)

for file in files:
    print(file)

old = input("Enter the old file path: ")
new = input("Enter the new file path: ")

if os.path.exists(old):
    os.rename(old, new)
    print(f"{old} has been renamed to {new}.")
else:
    print(f"The file '{old}' does not exist, so it cannot be renamed.")
