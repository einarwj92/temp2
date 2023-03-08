def IMG_file(filename):

    if not "IMG" in filename:
        return False

    splittet = filename.split('_')
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
        0 <= hour < 60,
         0 <= minute < 60,
         0 <= sec < 60
    ]

    if not all(tests):
        return False
    return True

import re
def IMG_file_regex(filename):
    # IMG_20160722_165544.jpg
    year = "20(0[0-9]|1[0-9]|2[0-9])"
    month = "(0[1-9]|1[0-2])"
    day = "(0[1-9]|1[0-9]|2[0-9]|3[01])"

    hour = "([01]\d|2[0-3])"
    minute = "[0-5]\d"
    second = "[0-5]\d"

    pattern = "^IMG_" + year + month + day + '_' + hour + minute + second + "\.jpg$"  # . er wildcard så må escapes. ankres for exakt match

    match = re.search(pattern, filename)
    return match


if __name__ == "__main__":

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
        "IMG_00722.255544.jpg": False,    # Alt
        "aaIMG_20160722_225544.jpg": False   # filename
    }
    print("filename                  match  fasit")
    for test in tests:
        match = IMG_file_regex(test)
        if match:
            match = True
        else:
            match = False

        print("{:30}{:>}  {:>}".format(test, match, tests[test]))
