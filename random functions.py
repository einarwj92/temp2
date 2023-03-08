import os.path


def ends_with_postfix(filename):
    """
    Om filnavnet ender med
    '(tall)' | '_tall', tall < 1000
    return True
    else False

    :param filename: String, filnavn
    :return: Boolean
    """

    # tests:
    # kun interessert i filene jeg har lagt til postfix på
    # det ble gjort slik filnavn + "_tall" + ".ext"
    # = filnavn_tall.ext

    # Om filnavn har formatet filnavn_tall.ext så skal vi ha..

    splittet = filename.split('_')  # ["filnavn", "tall.ext"]
    if len(splittet) > 1:           # om minst en '_' i navn
        tail = splittet[-1]         # skal da ha: tail = "tall.ext"
        tail = tail.split('.')      # skal da ha: tail = ["tall", "ext"]
        if len(tail) == 2:          # skal da ha: True
            if tail[0].isnumeric(): # skal da ha: True
                tall = tail[0]      # skal da ha "tall"
                if int(tall[0]) > 0:        # "tall" starter ikke med 0
                    if 1000 > int(tall) > 0:    # 1000 > tall > 0
                        # true
                        return "_".join(splittet[:-1]) + "." + tail[1]


    # antar filnavn(tall).ext

    splittet = filename.split('(') # [filnavn, tall).ext]
    if len(splittet) > 1:
        tail = splittet[-1]        # tall).ext
        tail = tail.split(')')     # [tall, .ext]
        if len(tail) == 2 and tail[1] != '':
            if tail[1][0] == ".":  # has extension
                if tail[0].isnumeric():
                    # true
                    return "(".join(splittet[:-1]) + tail[1]

    return ''

def equal_size(file1, file2):
    """
    Tests if two files are equal (same name and same size)
    :param file1: abs path to 1. file
    :param file2: abs path to 2. file
    :return: boolean
    """

    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    if size1 == size2:
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
    while os.path.exists(file):
        name, ext = os.path.splitext(filename)
        file = os.path.join(base, f"{name}_({i}_){ext}")
        i += 1
    return file

def get_list_of_types(folder):
    typs = {}
    total = 0; snaps = 0
    screens = 0; no_ext = 0
    received = 0; img = 0

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            total += 1
            name, ext = os.path.splitext(filename)
            if not "." in ext:
                no_ext += 1
                continue
            ext = ext.split(".")[1]

            if "Snapchat" in filename:
                snaps += 1

            if "Screenshot" in filename:
                screens += 1

            if "received" in filename:
                received += 1

            if "IMG" in filename:
                img += 1

            if not ext in typs:
                typs[ext] = 1
            else:
                typs[ext] += 1
    s = sorted(typs.items(), key=lambda x:x[1], reverse=True)
    s.append(("screens", screens))
    s.append(("snaps", snaps))
    s.append(("received", received))
    s.append(("IMG", img))
    s.append(("no ext", no_ext))
    s.append(("total", total))
    return s


def binary_equal():
    """
    read about file, open and closing
    :return:
    """
    imagepath1 = "C:\\Users\\47991\\Desktop\\New folder\\1459108816158_1.jpg"
    imagepath2 = ""

    image1 = open(imagepath1, 'rb').read()
    #image2 = open(imagepath2, 'rb').read()

    print(type(image1))
    #assert image1 == image2
    #print(image3)

test_ends_with_postfix = 1
if __name__ == "__main__":
    #img = "C:\\Users\\47991\\Desktop\\New folder\\1459108816158_1.jpg"
    #print(find_new_name(img))

    if test_ends_with_postfix:
        # antar at filen har en gyldig file extension
        # tester ikke "filnavn" "filnavn_" osv ..
        test1 = {
            "navn.jpg" : '',
            "navn_.jpg" : '',
            "__.jpg" : '',
            "navn_navn_.jpg" : '',
            "navn._.jpg" : '',
            "navn" : '',
            "_navn_" : '',
             "." : '',
            "._" : '',
            "_." : '',
            "_" : ''
        }

        test2 = {
            "navn_0.jpg" : '',
            "navn_00.jpg" : '',
            "navn_001.jpg" : '',
            "navn_200.jpg" : "navn.jpg",
            "navn_1000.jpg" : '',
            "navn_5_1001.jpg" : ''
        }

        # filnavn(tall).ext
        test3 = {
            "navn(" : '',
            "navn()" : '',
            "navn.jpg" : '',
            "navn().jpg" : '',
            "()navn.jpg" : '',
            "navn.jpg()" : '',
            "navn(1)" : '',
            "navn(01)" : '',
            "navn(25644)" : '',
            "navn123" : '',
            "navn(123).jpg" : "navn.jpg",
            "navn(12.jpg" : '',
            "navn)123(.jpg" : '',
            "navn(123(.jpg" : '',
            "navn)123).jpg" : '',
            "(navn1233).jpg" : '',
            "(navn123.jpg)" : '',
            "()n(hi)(l(12).jpg" : "()n(hi)(l.jpg",
            "Screenshot_20210418_092216_com.android.chrome_1.jpg" : "Screenshot_20210418_092216_com.android.chrome.jpg"
        }

        print("test 1")
        for t in test1:
            computed = ends_with_postfix(t)
            fasit = test1[t]

            assert computed == fasit

        print("\ntest 2")
        for t in test2:
            computed = ends_with_postfix(t)
            fasit = test2[t]

            assert computed == fasit

        print("\ntest 3")
        for t in test3:
            computed = ends_with_postfix(t)
            fasit = test3[t]

            assert computed == fasit

        print("success")