import sys
from PIL import Image
import os

# Folder Paths
input_img_folder = sys.argv[1]
output_img_folder = sys.argv[2]


# Functions
def abort():
    print("\nConversion Aborted")


def success():
    print(
        f'\nSucessful conversion! Converted images can be found here: "{output_img_folder}"'
    )


def ask_to_proceed(message):
    while True:
        cont = input(message)
        if cont.upper() == "Y" or cont.upper() == "YES":
            break
        elif cont.upper() == "N" or cont.upper() == "NO":
            abort()
            quit()
        else:
            print('\nPlease enter a valid answer: Yes("y"/"Y") or  No("n"/"N")')
            continue


def create_out_folder(dir_name):
    os.mkdir(dir_name)

def ask_filetype():
    return input("\nDefault output type is to png, leave blank to stick with this format. However, if you would like a different format enter it here (ex. \"jpeg\", \"bmp\", etc.): ")

def convert(file, desired):
    if desired == '':
        desired = 'png'
    if desired.__contains__('.'):
        desired = desired[1:]
    jpg = Image.open(f"{input_img_folder}/{file}")
    jpg.save(f'{output_img_folder}/{file.split(".")[0]}.{desired}', desired)


# Format folder paths
if input_img_folder[-1] == "/":
    input_img_folder = input_img_folder[:-1]

if output_img_folder[-1] == "/":
    output_img_folder = output_img_folder[:-1]

# Check if input folder exists
if not os.path.exists(input_img_folder):
    print(
        f'\nThe input folder you provided at"{input_img_folder}" does not exsist. Check for typos and rerun.'
    )
    abort()
    quit()

# check if output folder exists, then ask to continue
if not os.path.exists(output_img_folder):
    create_out_folder(output_img_folder)
    print(f"\nNew folder created at {output_img_folder}\n")
else:
    ask_to_proceed(
        "\nWarning: The output folder you have supplied already exists. If you proceed you may overwrite any files with matching filenames. Would you like to continue? [Y/N]: "
    )


# loop through folder and convert each file
filetype = ask_filetype()
print("\nConverting...")
for file in os.listdir(input_img_folder):
    convert(file, filetype)
print("\nDone.")
success()
