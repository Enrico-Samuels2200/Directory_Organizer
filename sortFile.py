import os

has_location = False
base_dir = os.path.dirname(os.path.abspath(__file__))

#   Check if data file exist. If does then read file for data(path)
#   If Path doesn't exist create path
#   Scan path for file types 
#

def folder_location():
    
    # If has location is false user is asked to add a location.
    if not has_location:
        location = str(input('[*] Enter the location to the file: '))
        validate = os.path.exists(location)

        if validate:
            with open(f'{base_dir}/data.txt', 'w') as doc:
                doc.write(location)
        else:
            print('[!!] File location doesn\'t exist.')