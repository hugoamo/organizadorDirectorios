import os
import shutil
import pathlib

new_path = os.getcwd()
os.chdir(new_path)


for root, dirs, files in os.walk(new_path):
    print(f'En {root} tenemos  {len(files)} files:')
    for file in files:
        extension = os.path.splitext(file)
        try:
            if not os.path.isdir(extension[1]):
                current_dir = os.getcwd()
                os.mkdir(extension[1])
                pathFile = f"{current_dir}/{extension[1]}"
                shutil.move(file, pathFile)
            else:
                print("Existe")
                current_dir = os.getcwd()
                pathFile = f"{current_dir}/{extension[1]}"
                shutil.move(file, pathFile)
        except:
            if not os.path.isdir("otros"):
                os.mkdir("otros")
                pathFile = f"{current_dir}/otros"
                shutil.move(file, pathFile)
            else:
                urrent_dir = os.getcwd()
                pathFile = f"{current_dir}/otros"
                shutil.move(file, pathFile)

