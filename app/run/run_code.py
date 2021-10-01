import os

from .compiler import get_flags

app_name = "cppt"

def check():
    pass


def run(base_path, file_name):
    check()
    file_name_without_ext = file_name[:file_name.rfind(".")]
    app_folder_path = base_path + "/.{}".format(app_name)
    task_folder = app_folder_path + \
        "/{}".format(file_name_without_ext)
    tc_folder = task_folder + "/tc"
    last_run_folder = task_folder + "/last_run"
    os.chdir(last_run_folder)
    compilation_command = f"g++-11 {get_flags()} ../../../{file_name} -o {file_name_without_ext}"
    os.system(compilation_command)
    print(compilation_command)
    for tc in os.listdir("../tc"):
        if (tc.startswith("in")):
            num = tc[2:][:-4]
            if os.path.isfile(f"../tc/ans{num}.txt"):
                print(f"Running TC #{int(num)}")
                run_command = f"./{file_name_without_ext} < ../tc/in{num}.txt 2> error{num}.txt > output{num}.txt"
                print(run_command)
                os.system(run_command)
                diff_command = f"diff ./output{num}.txt ../tc/ans{num}.txt > diff{num}.txt"
                os.system(diff_command)
                if (os.path.getsize(f"diff{num}.txt") == 0):
                    print(f"Accepted #{int(num)}")
                    if (os.path.getsize(f"error{num}.txt") != 0):
                        print("Standard Error: ")
                        os.system(f"cat error{num}.txt")
                else:
                    print(f"Wrong Answer #{num}")
                    print("Test Case: ")
                    os.system(f"cat ../tc/in{num}.txt")
                    print("Correct Answer: ")
                    os.system(f"cat ../tc/ans{num}.txt")
                    print("Standard Output: ")
                    os.system(f"cat output{num}.txt")
                    if (os.path.getsize(f"error{num}.txt") != 0):
                        print("Standard Error: ")
                        os.system(f"cat error{num}.txt")
                    print("Diff: ")
                    os.system(f"cat diff{num}.txt")


    

