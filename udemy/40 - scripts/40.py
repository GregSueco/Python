import os.path

files_to_process = [
    r"C:\Users\Z6GSZ\Desktop\Python-udemy\udemy\40 - scripts\script_1.py",
    r"C:\Users\Z6GSZ\Desktop\Python-udemy\udemy\40 - scripts\script_2.py"
    ]

for file in files_to_process:
    basename = os.path.basename(file)
    print(basename)
    with open(file, 'r') as source:
        code = source.read()
        exec(code)
    


