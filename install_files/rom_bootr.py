# Including the dependencies
import os
from os import listdir
from os.path import isfile, join
import json

# Declaring the file directorys
file_dir = "/boot/ROMS/"
conf_dir = file_dir + "_config/lib_cores.json"

# Used to actually load the roms
def load_rom(rom_name):
    # Getting the file extension so we can identify the console
    rom_ext = ext_extract(rom_name)

    try:
        # Loading console information
        with open(conf_dir) as data_file:
            data = json.load(data_file)
    except:
        print "Failed to load lib_cores file"

    # Getting the command we need to launch the game
    try:
        if rom_ext in data['consoles'][0]:
            os.system(data['consoles'][0][rom_ext]["command"].replace("%ROM%", '"' + file_dir + rom_name + '"'))
        else:
            print "That file type is not currently supported. Please edit " + conf_dir
    except:
        print "Something went wrong whilst trying to load the ROM"

# Used to extract the file extension to aid the loading of the game
def ext_extract(file_name):
    # Getting the first index of the reversed name where "." occurs
    file_name = file_name[::-1].partition(".")[0]
    return file_name[::-1]

# Printing some ASCII graphics :P
print "-------------------------------"
print "  FROOPLE'S CUSTOM ROM BOOTER  "
print "-------------------------------"

# Loading the ROMS folder
try:
    rom_files = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
except:
    print "Something went wrong, does the folder: " + file_dir + " exist?"

if len(rom_files) > 0:
    if len(rom_files) > 1:

            i = 0

            print  str(len(rom_files)) + " files found"
            print "-------------------------------"

            for file in rom_files:
                s = "(" + str(i) + ") " + file
                print s
                i += 1

            print "-------------------------------"

            while True:

                rom = raw_input("Please enter the number of the ROM you want to load: ")

                if int(rom) > len(rom_files):
                    print "Invalid selection"
                else:
                    load_rom(rom_files[int(rom)])
                    break

    elif len(rom_files) == 1:
        load_rom(rom_files[0])

else:
    print "No files found in ROMS folder"
