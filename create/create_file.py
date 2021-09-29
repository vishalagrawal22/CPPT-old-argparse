import os
import sys

from init.make_folder import make_folder
app_name = "cppt"


def create_file(base_path, file_name, mode = 0):
    make_folder(base_path, 1)
    file_name_without_ext = file_name[:file_name.find(".")]
    app_folder_path = base_path + "/.{}".format(app_name)
    task_folder = app_folder_path + \
        "/{}".format(file_name_without_ext)
    tc_folder = task_folder + \
        "/TC".format(app_name)
    last_run_folder = task_folder + \
        "/Last Run".format(app_name)
    file_path = base_path + "/{}".format(file_name)

    if os.path.exists(task_folder):
        print("Folder already exists!")
        if (mode == 0):
            print("Do you want to overwrite it? y/n")
            choice = input()
            if choice == 'y' or choice == 'Y':
                print("The file has been overwritten")
                for root, dirs, files in os.walk(task_folder, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
                os.rmdir(task_folder)
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                sys.exit()
        else:
            sys.exit()
    elif os.path.exists(file_path):
        print("File already exists!")
        if (mode == 0):
            print("Do you want to overwrite it? y/n")
            choice = input()
            if choice == 'y' or choice == 'Y':
                print("The file has been overwritten")
                os.remove(file_path)
            else:
                sys.exit()
        else:
            sys.exit()

    try:
        os.mkdir(task_folder)
        os.mkdir(tc_folder)
        os.mkdir(last_run_folder)
        open(file_path, 'w').close()
    except OSError:
        print(file_path)
        print('Failed creating the file')
    else:
        print('File created')
