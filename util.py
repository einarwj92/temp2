import os

def IMAG_file(filename):
    name, ext = os.path.splitext(filename)

    if not ext:
        return False

    if not len(name) == 8:
        return False

    imag = name[:4]
    if not imag == "IMAG":
        return False

    number = name[4:]
    if not number.isnumeric():
        return False

    return True
def DSC_file(filename):
    name, ext = os.path.splitext(filename)

    if not ext:
        return False

    if not len(name) == 8:
        return False

    dsc = name[:3]
    if not dsc == "DSC":
        return False

    number = name[3:]
    if not number.isnumeric():
        return False

    return True
def IMG_file(filename):
    """
    IMG-formater
    originalt: IMG_20170305_130614.jpg
    """

    if not "IMG" in filename:
        return False

    splittet = filename.split('_')      # IMG_20170305_130614.jpg
    if not len(splittet) == 3:
        return False

    img = splittet[0]
    if not img == "IMG":
        return False

    date = splittet[1]
    if (not len(date) == 8) or not date.isnumeric():
        return False

    splittet = splittet[2].split('.')
    if not len(splittet) == 2:
        return False

    ext = splittet[1]
    if not ext == "jpeg":
        return False

    tid = splittet[0]
    if (not len(tid) == 6) or not tid.isnumeric():
        return False

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])


    tests = [
        2000 < year < 2030,
         0 < month < 13,
         0 < day < 33
    ]
    if not all(tests):
        return False


    hour = int(tid[:2])
    minute = int(tid[2:4])
    sec = int(tid[4:])

    tests = [
        0 <= hour < 24,
         0 <= minute < 60,
         0 <= sec < 60
    ]

    if not all(tests):
        return False

    return True
def EXT_file(filename):
    splittet = filename.split('.')
    if len(splittet) > 1 and splittet[-1]:
        return True
    else:
        return False
def find_new_name(file):
    """
    file finnes fra før, gi nytt navn
    :param file:
    :return:
    """
    base, filename = os.path.split(file)
    i = 1
    while os.path.isfile(file):
        name, ext = os.path.splitext(filename)
        file = os.path.join(base, f"{name}_({i})_(a51H9n)_{ext}")
        i += 1
    return file
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


if __name__ == "__main__":
    test_IMAG_file = False
    test_DSC_file = False
    test_IMG_file = False
    test_EXT_file = False

    if test_IMAG_file:
        # IMAGxxxx x E [0,9]   (x * 4)
        #
        #       TEST       FASIT    ÅRSAK
        #
        tests = {
            "": False,              # tom streng
            "IMAG19345.j": False,   # Filnavn lengde
            "IMAG123.j": False,     # Kort
            "IMAG12345.j": False,   # Langt
            "0IMAG1234.j": False,   # Navn
            "IMAG55f43.jpg": False, # Tall
            "IMAG0000.jpg": True,   # --
            "IMAG0909.jpg": True,   # --
            "IMAG9999.j": True,     # --
            "IMAG-4000.jpg": False, # Filnavn
            "H.IMAG4456.jpg": False # '.'
        }

        for t in tests:
            #print("{:>14}{:2}".format(t, IMAG_file(t)))
            assert IMAG_file(t) == tests[t]
        print("test IMAG finished successfully")
    if test_DSC_file:
        # DSCxxxxx  x E [0,9]  (x * 5)
        #
        #   TEST        FASIT       ÅRSAK
        #
        tests = {
            "DSC123.j" : False,     # Tall -
            "DSC123451.j" : False,  # Tall +
            "0DSC1234.j" : False,   # Tag
            "DSC55f43.jpg": False,  # Tall $
            "DSC00000.jpg": True,   # --
            "DSC01010.jpg": True,   # --
            "DSC99999.j": True,     # --
            "DSC12312": False,      # Ext -
            "DsC34188.jpg": False,  # Tag
            "DSC-4000.jpg": False   # Filnavn $
        }

        for t in tests:
            #print("{:13}{:6}".format(t, DSC_file(t)))
            assert DSC_file(t) == tests[t]
        print("test DSC finished successfully")
    if test_IMG_file:
        tests = {
            "IMG_20160722_165544": False,   # Ext -
            "IMG_20160722_165544.jpg": True,  # --
            "IMG_20160722_16554.jpg": False,  # time -
            "IMG_2016072_165544.jpg": False,  # date -
            "IMG_20160722_165564.jpg": False, # sec > 60
            "IMG_20160722_240013.jpg": False, # hour > 23
            "IMG_20160722_255544.jpg": False, # hour > 23
            "IMG_20160735_165544.jpg": False, # day > 32
            "IMG_20161322_165544.jpg": False, # month > 12
            "IMG_20160722165544.jpg": False,  # Filename -
            "InG_20160722_255544.jpg": False, # Tag
            "IMG_F0160722_255544.jpg": False, # $
            "IMG_20160722_25P544.jpg": False, # $
            "IMG_20160722.215544.jpg": False, # Filnavn
            "_20160722.255544.jpg": False,    # Tag
            "IMG_20160722_000012_jpg": False, # Filnavn
            "IMG_201690722.255544.jpg": False,# Date +
            "IMG_00722.255544.jpg": False     # Alt
        }

        #try:
        for t in tests:
            #print("{:>14}{:2}".format(t, IMG_file(t)))
            assert IMG_file(t) == tests[t]
        print("test IMG finished successfully")
        #except AssertionError as a:
        #    print(f"{a}\n\tFailed test{c}: {t}")
    if test_EXT_file:
        tests={
            "abc.j": True,
            "axg": False,
            "": False,
            " ": False,
            ".": False,
            "..": False,
            "...": False
        }
        try:
            c = 0
            for t in tests:
                c += 1
                assert EXT_file(t) == tests[t]
            print("test EXT_file finished successfully")
        except AssertionError as a:
            print(f"test EXT_file: failed test{c}: {t}")