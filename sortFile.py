import os
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))

folder_types = [
    'Images',
    'Videos',
    'Documents',
    'Applications',
    'Compressed',
    'Other'
]

item_types = {
    'jpg':'Images',
    'jpeg':'Images',
    'png':'Images',
    'gif':'Images',
    'avi':'Videos',
    'mp4':'Videos',
    'mkv':'Videos',
    'pdf':'Documents',
    'txt':'Documents',
    'exe':'Applications',
    'msi':'Applications',
    'apk':'Applications',
    'xapk':'Applications',
    'zip':'Compressed',
    'rar':'Compressed'
}

#   Check if data file exist. If does then read file for data(path)
#   If Path doesn't exist create path
#   Scan path for file types
#   Add file types to directories associated with file type

def read_data_file():
    with open('data.pydata', 'r') as doc:
        data = doc.readline()
        return data

def folder_location():
    # If has location is false user is asked to add a location.
    path = str(input('[*] Enter the location to the file: '))
    valid = os.path.exists(path)

    if valid:
        with open(f'{base_dir}/data.pydata', 'w') as doc:
            doc.write(path)
        verify_data_file()
    else:
        print('[!!] File location doesn\'t exist.')

#   Copies files if file type matches that in dictionary item_types.
def copy_file():
    operate_dir = read_data_file()
    for root, dirs, files in os.walk(operate_dir):
        for file in files:
            for file_type in item_types:
                if file.endswith(file_type):
                    try:
                        shutil.move(f'{operate_dir}/{file}', f'{operate_dir}/{item_types[file_type]}/')

                    except:
                        continue

def create_folders():
    for name in folder_types:
        try:
            os.mkdir(name)

        except:
            continue

#   If data file exist then read path and check if path is valid.
def verify_data_file():
    try:
        path = read_data_file()
        validate = os.path.exists(path)

        if validate:
            create_folders()
            copy_file()
        else:
            folder_location()

    except:
        folder_location()

if __name__ == '__main__':
    verify_data_file()