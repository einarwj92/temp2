"""
Brukt for å flytte alle mediailer fra en mappe for å samle de på en dst
"""
def get_list_of_types(title, folder, print_result = False, filetypes_of_intr = [], filenames_of_intr = []):
    """ returnerer liste med tupler ('x', y) der x er descriptor og y er antall.
        Sjekker om summen av talte exts er lik totalen.
    """
    # ----------
    #   setup
    # ----------

    types = {}
    names = {}
    no_ext = 0
    total = 0

    for name in filenames_of_intr:
        names[name] = 0

    # ----------
    #   scan
    # ----------
    print("\nscanning folder: ",folder,"...")
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:

            total += 1

            splittet = filename.split('.')
            if not len(splittet) > 1:
                no_ext += 1
                continue    # SKIP

            for name in filenames_of_intr:
                if name in filename:
                    names[name] += 1



            ext = splittet[-1]
            # visual inspection
            #if ext == 'bmp':
            #    print(os.path.join(dirpath, filename))

            if not ext in types:
                types[ext] = 1
            else:
                types[ext] += 1

    sorted_list = sorted(types.items(), key=lambda x:x[1], reverse=True)
    sorted_list.insert(0, ("No ext", no_ext))

    sorted_list_names = sorted(names.items(), key=lambda x: x[1], reverse=True)

    # -----------
    #  check sum
    # -----------

    c = 0
    for s in sorted_list:
        c += s[1]

    sorted_list.insert(0, ("Files in folder", total))
    if total != c:
        sorted_list.insert(0, (f"Error, exts dont sum up to total: {total} != sum: {c}", "\n"))

    # -------------------
    #     print all
    # -------------------

    if print_result:
        if title:
            print("\n{}".format(title))

        print("SCAN: ",folder)
        print("_________________  start  _________________")
        print("  All files in folder and types")
        for t in sorted_list:
            if len(t) == 2:
                #
                descriptor = t[0]
                number = t[1]
                print("{:>17}: {}".format(descriptor, number))

    # ----------------------
    #  print types of interest
    # ----------------------

        if filetypes_of_intr:
            l = []
            to = 0
            print("")
            print("\ntypes of interest:",filetypes_of_intr)
            for t in sorted_list:
                if t[0] in filetypes_of_intr:
                    l.append(t)
                    to += t[1]
            for itn in l:
                print("{:>17}: {}".format(itn[0], itn[1]))
            print("{:>17}: {}".format("total: ",to))

        print("\nnames of interest:", filetypes_of_intr)
        to = 0
        if filenames_of_intr:
            for n in sorted_list_names:
                descriptor = n[0]
                number = n[1]
                to += number
                print("{:>17}: {}".format(descriptor, number))
            print("{:>17}: {}".format("total: ", to))

        print("_________________  stop  _________________\n")



    return sorted_list
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
    base, filename = os.path.split(file)
    while os.path.isfile(file):
        #print("finnes:", file)
        filename = add_postfix(filename)
        file = os.path.join(base, filename)
    return file
def accepted(filename, types):
    splittet = filename.split('.')
    ext = splittet[-1]


    if not ext in types:
        return False
    else:
        return True


import os
import sys
import shutil


moved = 0
only_scan = False
move = False
main = True
count = 0
break_loop = 0
accepted_files = 0

src = "E:\\test sortering 030323\\src"
dst = "E:\\media\\bilder\\s4"


IMAGE_EXT = ['jpg', 'JPG', 'jpeg', 'png', 'PNG', 'gif', 'tif'] # svg? bmp?tibia dib?
VIDEO_EXT = ['mp4', '3gp'] # 3gp?
SOUND_EXT = ['m4a', 'mp3']
FILES_OF_INTEREST = IMAGE_EXT
NAMES_OF_INTEREST = ["Snapchat", "Screenshot", "received", "IMG", "IMAG", "DSC"]

get_list_of_types("Before processing",
                  src,
                  filetypes_of_intr= FILES_OF_INTEREST,
                  filenames_of_intr=NAMES_OF_INTEREST,
                  print_result=True)

if only_scan:
    sys.exit()

print("\n================== PROCESSING ======================")
if main:
    for dirpath, dirnames, filenames in os.walk(src):
        if break_loop:
            break
        for filename in filenames:

            if accepted_files == 5000:
                break_loop = True
                break


            if not accepted(filename, FILES_OF_INTEREST):
                continue
            else:
                accepted_files += 1

            srcfile = os.path.join(dirpath, filename)
            dstfile = os.path.join(dst, filename)

            if os.path.isfile(dstfile):
                dstfile = find_new_name(dstfile)
                #print("new name: ",dstfile)

            if move:
                shutil.move(srcfile, dstfile)
                moved += 1

print("accepted files: ", accepted_files)
print("files moved: ",moved)


get_list_of_types("After processing",
                  dst,
                  filetypes_of_intr=FILES_OF_INTEREST,
                  filenames_of_intr=NAMES_OF_INTEREST,
                  print_result= True)

