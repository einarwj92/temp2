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
import re
def IMAG_file_regex(filename):
    # IMAG1427.jpg
    pattern = "^IMAG\d{4}.jpg$" # ^og $ er anker, funker men ikke helt hvordan
    match = re.search(pattern, filename)
    return match


if __name__ == "__main__":
    tests = {
        "": False,  # tom streng
        "IMAG19345.j": False,  # Filnavn lengde
        "IMAG123.j": False,  # Kort
        "IMAG12345.j": False,  # Langt
        "0IMAG1234.j": False,  # Navn
        "IMAG55f43.jpg": False,  # Tall
        "IMAG0000.jpg": True,  # --
        "IMAG0909.jpg": True,  # --
        "IMAG9999.j": True,  # --
        "IMAG-4000.jpg": False,  # Filnavn
        "H.IMAG4456.jpg": False  # '.'
    }

    print("filename                  match  fasit")
    for test in tests:
        match = IMAG_file_regex(test)
        if match:
            match = True
        else:
            match = False


        print("{:30}{:>}  {:>}".format(test, match, tests[test]))
