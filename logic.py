import os
import sys

app_name = "cppt"


def make_folder(base_path):
    app_folder_path = base_path + "/.{}".format(app_name)
    if not os.path.isdir(base_path):
        print('The path specified does not exist')
        sys.exit()
    elif os.path.exists(app_folder_path):
        print("Folder already exists!")
    else:
        print("Created folder: " + app_folder_path)
        os.mkdir(app_folder_path)
