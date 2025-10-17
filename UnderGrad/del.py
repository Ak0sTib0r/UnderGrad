import sys
import os

fileName = sys.argv[1]

toRemove = [f"{fileName}.pdf", f"{fileName}.synctex.gz", f"{fileName}.tex"]

os.chdir(f'C:\\Users\\akosh\\OneDrive\\Asztali gép\\Notes\\{fileName}')

for file in toRemove:
    os.remove(file)

os.chdir('C:\\Users\\akosh\\OneDrive\\Asztali gép\\Notes')

print("\n**********All FILES DELETED**********")