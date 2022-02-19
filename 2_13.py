import os

def check_file(path):
    fileLocation = path
    isFile = os.path.isfile(fileLocation)

    while isFile == False: 
        fileLocation = input("Please provide correct file location: ")
        isFile = os.path.isfile(fileLocation)
    else:
        print("File path is correct, I start processing... ")
        
    return  fileLocation
      
def parse_file(fileLocation):
    with open(fileLocation,encoding="utf-8") as file:
        content = file.read()
        parsed_content = content.split()
        print(parsed_content)
        print('Total number of elements: ', len(parsed_content))
    return len(parsed_content)

   
path = input("Please provide correct file location: ")
file_path = check_file(path)
parse_file(file_path)
