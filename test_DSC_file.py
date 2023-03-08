import os

def DSC_file(filename):
    # DSC01849
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

import re
def DSC_file_regex(filename):
    # DSC01849
    pattern = "^DSC\d{5}.JPG$"
    match = re.search(pattern, filename)
    return match

if __name__ == "__main__":
    """
    tests = [
        "DSC123", "DSC12345", "0DSC1234", "DSC55f43.jpg",
        "DSC00000.jpg", "DSC34188.jpg", "DSC341885.jpg", "DsC34188.jpg",
        "DSC-4000.jpg"
    ]

    for t in tests:
        print("{:13}{:6}".format(t, DSC_file(t)))
    """
    tests = {
        "DSC123.JPG": False,  # Tall -
        "DSC123451.JPG": False,  # Tall +
        "0DSC12347.JPG": False,  # Tag
        "DSC55f43.JPG": False,  # Tall $
        "DSC00000.JPG": True,  # --
        "DSC01010.JPG": True,  # --
        "DSC99999.JPG": True,  # --
        "DSC12312": False,  # Ext -
        "DsC34188.JPG": False,  # Tag
        "DSC-4000.JPG": False  # Filnavn $
    }

    print("filename                  match  fasit")
    for test in tests:
        # print("{:13}{:6}".format(t, DSC_file(t)))
        match = DSC_file_regex(test)
        if match:
            match = True
        else:
            match = False


        print("{:30}{:>}  {:>}".format(test, match, tests[test]))
