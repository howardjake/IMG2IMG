import sys
from PIL import Image
import os

# Folder Paths
input_img_folder = sys.argv[1]
output_img_folder = sys.argv[2]


# Functions
def abort():
    print("Conversion Aborted")


def success():
    print(
        f'Sucessful conversion! Converted images can be found here: "{output_img_folder}"'
    )


def ask_to_proceed(message):
    while True:
        cont = input(message)
        if cont == "Y" or cont == "y":
            break
        elif cont == "N" or cont == "n":
            abort()
            quit()
        else:
            print('Please enter a valid resonse: "y"/"Y", "n"/"N"')
            continue


def create_out_folder(dir_name):
    os.mkdir(dir_name)


def convert(file):
    jpg = Image.open(f"{input_img_folder}/{file}")
    jpg.save(f'{output_img_folder}/{file.split(".")[0]}.png', "png")


# Format folder paths
if input_img_folder[-1] == "/":
    input_img_folder = input_img_folder[:-1]

if output_img_folder[-1] == "/":
    output_img_folder = output_img_folder[:-1]

# Check if input folder exists
if not os.path.exists(input_img_folder):
    print(
        f'The input folder you provided at"{input_img_folder}" does not exsist. Check for typos and rerun.'
    )
    abort()
    quit()

# check if output folder exists, then ask to continue
if not os.path.exists(output_img_folder):
    create_out_folder(output_img_folder)
    ask_to_proceed(
        f"New folder created at {output_img_folder}. Would you like to continue? [Y/N]: "
    )
else:
    ask_to_proceed(
        "The output folder you have supplied already exists. If you proceed you may overwrite files with conflicting names. Would you like to continue? [Y/N]: "
    )


# loop through folder and convert each file
print("Converting...")
for file in os.listdir(input_img_folder):
    convert(file)
print("Done.")
success()
