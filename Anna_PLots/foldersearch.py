import os
from collections import OrderedDict


folders = []
filenames = OrderedDict()

for root, subfolders, files in os.walk(r'C:\Users\annawi\Desktop\Projects\Propene oxidation\Experiments\201905_PdAufoams\EC data'):
    if len(files)==0: continue
    #folders.append(root[-8:])
    # if 'KERAS' in root:
    # if 'DTU800' in root:
    #     continue
        # print("FOUND")
    folders.append(root[root.rfind("\\")+1:])
    files_this_folder = []
    for filename in files:
        if filename.endswith(".mpt"):  #usually ".mpt"
            files_this_folder.append(filename)
            print(root)
    filenames[root[root.rfind("\\")+1:]] = files_this_folder
    # filenames[root[-15:]] = files_this_folder


print(folders)

print(filenames)
