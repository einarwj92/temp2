def pattern_in_name(pattern, filename):
    """
    Regex wrapper
    True if match found,
    Else False
    """
    match = re.search(pattern, filename)
    if match:
        return True
    else:
        return False
def build_new_filename(filename, date, img_tag):

    if not img_tag:
        img_tag = 'na'

    year =  str(date.year)[2:].zfill(2)
    month = str(date.month).zfill(2)
    day =   str(date.day).zfill(2)

    hour =   str(date.hour).zfill(2)
    minute = str(date.minute).zfill(2)
    second = str(date.second).zfill(2)

    # Exclude files >= 100mb
    size = str(os.path.getsize(srcfile))
    if len(size) > MAX_FILE_SIZE:
        return ''

    # Build new filename
    name, ext = os.path.splitext(filename)
    new_filename = year + month + day + "_" \
                   + hour + minute + second + "-" \
                   + size + "_" + img_tag + ext

    return new_filename
def add_postfix(filename):
    name, ext = os.path.splitext(filename)
    splittet = name.split('_')
    if splittet[-1] == "((F9n3))":
        splittet[-2] = str(int(splittet[-2]) + 1)
        #print("incr, ny splittet:",splittet)
        name = "_".join(splittet)
    else:
        name = name + "_1_((F9n3))"
    return name + ext
def find_new_name(file):
    if not os.path.isfile(file):
        return file
    base, filename = os.path.split(file)
    while os.path.isfile(file):
        #print("finnes:", file)
        filename = add_postfix(filename)
        file = os.path.join(base, filename)
    return file

FORMATCODE_IMG = "%Y%m%d_%H%M%S"
MAX_FILE_SIZE = 8 # len(filesize) < 8

import os
import re
import const
import shutil
from datetime import datetime

src = "E:\\media\\bilder\\s"
dst = "E:\\media sortering\\bilder"
trash_dir = "E:\\media duplikater\\bilder"

move = False
_moved_dst = 0
_moved_tsh = 0
_no_date = 0
_file_cnt = 0
_accepted = 0

for dirpath, dirnames, filenames in os.walk(src):
    for filename in filenames:

        if _file_cnt%4000 == 0:
            print(_file_cnt)
        _file_cnt += 1

        if pattern_in_name(const.orig_img_pattern22, filename):
            _accepted += 1
            # Filnavn har formatet:


            # Nåværende filpeker:
            srcfile = os.path.join(dirpath, filename)


            # Hent ut dato fra navn
            if pattern_in_name(const.orig_img_pattern01, filename):
                #"IMG_MIRROR
                img_date = filename[11:26]
            else:
                img_date = filename[4:19]

            try:
                date = datetime.strptime(img_date, FORMATCODE_IMG)
            except Exception as e:
                print("\terror1: ",filename,e)
                _no_date += 1
                continue


            # Bygger nytt filnavn etter oppskriften: date_hour-size_tag.ext
            img_tag = 'mg'
            new_filename = build_new_filename(filename, date, img_tag)
            print(filename, " -> ",new_filename)

            # Landingsfolder
            final_dst = os.path.join(dst, "kamera")
            if not os.path.exists(final_dst):
                os.makedirs(final_dst)


            # Ny filpeker
            newfile = os.path.join(final_dst, new_filename)


            # Sjekk om ny peker er oppptatt
            if not os.path.isfile(newfile):
                # ikke tatt
                if move:
                    shutil.move(srcfile, newfile)
                    _moved_dst += 1
                    print("\tdst")
            else:
                # tatt (duplikat da!?) flytt til annen folder og evt nytt navn
                # add postfix!?
                if move:
                    newfile = os.path.join(trash_dir, new_filename)
                    newfile = find_new_name(newfile)
                    shutil.move(srcfile, newfile)
                    _moved_tsh += 1
                    print("\ttrash")




print("file count :",_file_cnt)
print("accepted: ",_accepted)
print("files without a date: ",_no_date)
print("moved to dst: ",_moved_dst,"moved to trash", _moved_tsh)
