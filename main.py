#!/usr/bin/env python

#========================================================
# Python script to convert from NEF to JPG file format
# Created by FOD ISE/Eduardo Fonseca
# Created on 06/04/2024
#========================================================

#========================================================
# How to use script:
#  1. Drop NEF files in the same folder as script
#  2. Script lists all files in folder
#  3. Files with .NEF or .nef extension are processed
#  4. Files with .jpg extension are generated as output
#========================================================





# TODO: Define required libraries
# Import required libraries
import os
import datetime
import time
import platform
from PIL import Image


# TODO: Create folder structure if not existent
directory = 'output'
if not os.path.exists(directory):
    os.makedirs(directory)

# TODO: Drop NEF files

# TODO: Run the script with starting date as argument
# assigned regular string date
date_time = datetime.datetime(2024, 6, 6, 3, 47, tzinfo=datetime.timezone.utc)
print(date_time)

# TODO: Convert date to Unix time

# TODO: Open all files
# TODO: Compare created dates in Unix vs. starting date
# TODO: If file is new, convert to JPG and save in folder






def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
test = creation_date('blackbird.nef')
print(test)






# print regular python date&time
print("date_time =>", date_time)

# displaying unix timestamp after conversion
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))

# Unix Time = 1212282612
# Output    = 1212282612.0

# Unix Time = 1717645620
# Output    = 1717663620.0
# compare to https://www.andrews.edu/~tzs/timeconv/timeconvert.php?
'''
# For-loop to look at all files in directory
for filename in os.listdir("."):
    if filename.endswith(".nef") or filename.endswith(".NEF"):
        im = Image.open(filename)
        rgb_im = im.convert('RGB')
        rgb_im.save(filename[:-4] + '.jpg')
        raw = Nef(filename=filename)
        print(raw)

        exif_dict = im.info.get("exif")
        exif_data = piexif.load(im.info["exif"])
        print(exif_dict)
# can also save to a specific folder, such as "output"
# create the folder and replace the last line of code with:
# rgb_im.save('output/' + filename[:-4] + '.jpg')


'''

