import os
import sys

from init.make_folder import make_folder
app_name = "cppt"


def create_file(base_path, data):
    app_folder_path = base_path + "/.{}".format(app_name)
    make_folder(base_path, 1)

    file_name_without_ext = ""
    last = 0
    for ch in data["name"]:
        if ch.isalnum():
            file_name_without_ext += ch
            last = 0
        else:
            if last != 1:
                file_name_without_ext += '_'
                last = 1

    file_name_without_ext = file_name_without_ext.lower()

    task_folder = app_folder_path + \
        "/{}".format(file_name_without_ext)
    tc_folder = task_folder + "/tc"
    last_run_folder = task_folder + "/last_run"

    extension = ".cpp"
    file_name = file_name_without_ext + extension
    file_path = base_path + "/{}".format(file_name)

    if os.path.exists(task_folder):
        print("Folder already exists!")
        print(
            "Do you want to overwrite it? y/n [your code (if any) will be overwritten if you choose yes]")
        choice = input()
        if choice == 'y' or choice == 'Y':
            print("The folder has been overwritten")
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
    elif os.path.exists(file_path):
        print("File already exists!")
        print(
            "Do you want to overwrite it? y/n [your code (if any) will be overwritten if you choose yes]")
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
        source_file = open(file_path, 'w')

        if "url" in data:
            source_file.write('// ' + data["url"])

        source_file.close()
        generate_testcases(tc_folder, data)

    except OSError:
        print('Failed creating the file')
    else:
        print('File created')


def generate_testcases(tc_folder, data):
    os.chdir(tc_folder)
    problem_element = "tests"
    testcase_number = 0

    if problem_element in data:
        for individual_testcase in data[problem_element]:
            is_input_file = 1
            for testcase_element in individual_testcase:
                prefix = "ans"
                if is_input_file:
                    prefix = "in"
                file = open(prefix + str(testcase_number) + ".txt", "w")
                file.writelines(individual_testcase[testcase_element])
                file.close()
                is_input_file = is_input_file ^ 1
            testcase_number += 1

    for i in range(testcase_number, 10):
        filename = 'in' + str(i) + '.txt'
        if(os.path.isfile(filename)):
            os.remove(filename)
        filename = 'ans' + str(i) + '.txt'
        if(os.path.isfile(filename)):
            os.remove(filename)