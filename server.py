import os, signal
from flask import Flask, jsonify, request, Response
app = Flask(__name__) 

def gen_samples(data):
    for problem_element in data:
        if problem_element == 'name':
            filename = data[problem_element].replace(' ', '')
            filename = filename.replace('.', '-')
            filename += '.cpp'
            file = open(filename, 'w')
            file.write('link to problem: // ' + data['url'])
            file.close()

        if problem_element == 'tests':
            testcase_number = 0
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

@app.route('/', methods=['POST'])
def get_data():
    gen_samples(request.json)
    print("Server is shutting down...")
    os.kill(os.getpid(), signal.SIGINT)
    return Response(status = 200)  

if __name__ == '__main__':
    app.run(port=10043)