tests = {
    "IMG_20160722_165544": False,  # Ext -
    "IMG_20160722_165544.jpg": True,  # --
    "IMG_20160722_16554.jpg": False,  # time -
    "IMG_2016072_165544.jpg": False,  # date -
    "IMG_20160722_165564.jpg": False,  # sec > 60
    "IMG_20160722_240013.jpg": False,  # hour > 23
    "IMG_20160722_255544.jpg": False,  # hour > 23
    "IMG_20160735_165544.jpg": False,  # day > 32
    "IMG_20161322_165544.jpg": False,  # month > 12
    "IMG_20160722165544.jpg": False,  # Filename -
    "InG_20160722_255544.jpg": False,  # Tag
    "IMG_F0160722_255544.jpg": False,  # $
    "IMG_20160722_25P544.jpg": False,  # $
    "IMG_20160722.215544.jpg": False,  # Filnavn
    "_20160722.255544.jpg": False,  # Tag
    "IMG_20160722_000012_jpg": False,  # Filnavn
    "IMG_201690722.255544.jpg": False,  # Date +
    "IMG_00722.255544.jpg": False  # Alt
}

import re

# search for the pattern:
# IMG_20160722_165544.jpg
# pattern:
"""
'img_20
(0[0-9]|1[0-9]|2[0-9]) # 20 00-09, 10-19, 20-29  dekker altså årene *2000-2029*
(0[1-9]|1[0-2])        # 01-09, 10-12 dekker altså månedene *01-12*
(0[1-9]|1[0-9]|2[0-9]|3[01])' 01-09, 10-19, 20-29, 30, 31
_
([01]\d|2[0-3]) # 0 eller 1 sammen med siffer gir 00-09, 10-19 eller 20-23
[0-5]\d # 0-5 også siffer gir 0-9, 10-19, ..., 50-59
[0-5]\d # 0-5 også siffer gir 0-9, 10-19, ..., 50-59
"""

year = "20(0[0-9]|1[0-9]|2[0-9])"
month = "(0[1-9]|1[0-2])"
day = "(0[1-9]|1[0-9]|2[0-9]|3[01])"

hour = "([01]\d|2[0-3])"
minute = "[0-5]\d"
second = "[0-5]\d"

pattern = "IMG_" + year + month + day + '_' + hour + minute + second + "\.jpg" # . er wildcard så må escapes
print(pattern)

for test in tests:
    match = re.search(pattern, test)
    if match:
        match = True
    else:
        match = False
    print("{:30}{}{}".format(test, match, tests[test]))

"""
tests = range(1999,2040)
for test in tests:
    match = re.search(year, str(test))
    if match:
        match = True
    else:
        match = False
    print("{:30}{}".format(test, match))

tests = range(0,15)
for test in tests:
    test = str(test).zfill(2)
    match = re.search(month, test)
    if match:
        match = True
    else:
        match = False
    print("{:3}{}".format(test, match))

tests = range(0,34)
for test in tests:
    test = str(test).zfill(2)
    match = re.search(day, test)
    if match:
        match = True
    else:
        match = False
    print("{:3}{}".format(test, match))

tests = range(0,26)
for test in tests:
    test = str(test).zfill(2)
    match = re.search(hour, test)
    if match:
        match = True
    else:
        match = False
    print("{:3}{}".format(test, match))

tests = range(0,63)
for test in tests:
    test = str(test).zfill(2)
    match = re.search(minute, test)
    if match:
        match = True
    else:
        match = False
    print("{:3}{}".format(test, match))


tests = range(0,63)
for test in tests:
    test = str(test).zfill(2)
    match = re.search(second, test)
    if match:
        match = True
    else:
        match = False
    print("{:3}{}".format(test, match))
"""