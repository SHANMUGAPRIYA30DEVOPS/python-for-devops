import os

folders = input("please give the list of folders with spaces in between").split()
print(folders)

for folder in folders:
    
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print('please provide a valid folder name as file does not exist')
        continue
    except PermissionError:
        print('No access to this folder')
        continue

    print("-----" + folder + "-----------")
    print("list of files in the folder : " + folder)
    #print(files)
    for file in files:
        print(file)
    
