import os

base_dir = os.path.dirname(os.path.abspath(__file__))

#   Check if data file exist. If does then read file for data(path)
#   If Path doesn't exist create path
#   Scan path for file types
#   Add file types to directories associated with file type

def folder_location():
    
    # If has location is false user is asked to add a location.
    location = str(input('[*] Enter the location to the file: '))
    validate = os.path.exists(location)

    if validate:
        with open(f'{base_dir}/data.txt', 'w') as doc:
            doc.write(location)
    else:
        print('[!!] File location doesn\'t exist.')

#   If data file exist then read path and check if path is valid.
def verify_data_file():
    try:
        with open(f'{base_dir}\data.txt', 'r') as doc:
            data = doc.readline()
            validate = os.path.exists(data)

            if validate:
                pass
            else:
                folder_location()
    except:
        folder_location()

if __name__ == '__main__':
    verify_data_file()