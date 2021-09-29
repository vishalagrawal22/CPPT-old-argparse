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


def create_file(base_path, file_name):
    file_name_without_ext = file_name[:file_name.rfind(".")]
    app_folder_path = base_path + "/.{}".format(app_name)
    task_folder = app_folder_path + \
        "/{}".format(file_name_without_ext)
    tc_folder = task_folder + \
        "/tc".format(app_name)
    last_run_folder = task_folder + \
        "/last_run".format(app_name)
    file_path = base_path + "/{}".format(file_name)

    if os.path.exists(task_folder):
        print("Folder already exists!")
        print("Do you want to overwrite it? y/n")
        choice = input()
        if choice == 'y' or choice == 'Y':
            print("The file has been overwritten")
            os.rmdir(task_folder)
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            sys.exit()
    elif os.path.exists(file_path):
        print("Do you want to overwrite it? y/n")
        choice = input()
        if choice == 'y' or choice == 'Y':
            print("The file has been overwritten")
            os.remove(file_path)
        else:
            sys.exit()

    try:
        os.mkdir(task_folder)
        os.mkdir(tc_folder)
        os.mkdir(last_run_folder)
        open(file_path, 'w').close()
    except OSError:
        print('Failed creating the file')
    else:
        print('File created')
