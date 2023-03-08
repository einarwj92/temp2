"""
merk bilder: im, sc, ss ...

start med kun å behandle IMG-filer. Disse kjenner jeg godt, er flest av, og bør være rett frem å behandle.


om kun IMG included, og jeg ser fra scan det skal være X filer i src,
men så behandles ingen så kan det være litt klønete å se/forstå skyldes at de hadde
riktig format på navn, men ble excluded pga ext. 'wrong ext' samler alle excluded pga ext,
så det vil mest sannsynlig ikke synes på denne countern hva som skjedde med img filene


" ser ut til å fungere-
testet på
-------------------------
IMG
IMAG
DSC
----------------------
3500 skipped, not accepted, 600 wrong ext, hva med resten skipped?

1500 files moved- hva slags files?

"after scan" viser ikke riktig typer, 0 på alt, men riktig total??

2 filer i IMG ble ikke flyttet pga duplikat.
bortsett fra det ser IMG og IMAG flytt riktig ut.

fikk noe warnings om filer med 24+h tidsformat, bilder på tlf, men ser ut til å ha blitt flyttet (ikke sjekket navn)


screenshots har også date men ikketime i navn. + hvor/hvordan de ble tatt, android, chrome, instagram, linkedin, snap

flytt duplikater til egen mappe for å dobbeltsjekke de senere ved bruk av direkte bildesammenligning? binary

2262 screens vil ikke acceptes eller flyttes? 1208 finnes fra før i dst

after run bugger seg om ikke main kjøres pga new_dst ikke har blitt deklarert

30 snaps fantes fra før ellers ok

sjekke om dir eksisterer først, evt opprettre?

kun 332 av 357 received som ble accepted? ext?? png

når ingen files acceptes så kjærsjer det pga new dst ikke er deklarert (print after)

Screenshot_2018-12-14-05-38-47.png inneholder også date og time?!

screens: de 1216 som allerede finnes, var jpgs.. og ville aldri flyttes uansett
men var noen tusen som hadde .png ext som trengte at png ble inkludert.
Sjekket bare først og beste, så den var jpg og skjlnte ike, dmen det var da en av duplikatene. de var jpgs

totalt 1248 som finnes i dst.

med png inkludert i formater, virker den å sortere alt riktig nå av de filene som har switch.
kamera, snap,rcvd og screens.

ser at postfix ligger igjen blant annet

neste:
sorterer: se src og dst.

på dst ligger nå kamera, snap, screens, og recvd av det som lot seg sortere med program slik det er nå.

gå gjennom src og se hva som må til for å sortere resten. kanskje lagre 2.1 da den fungerer for denne
sorteringen, lag utbedring for å sortere resten i en 2.2 versjon?!

mye av filene som er igjen: IMG med postfix og filer som allerede finnes i dst . 1216 screens ba.
04/03/2023

:
04/03/2023
lager ny, 2.2: skal fikse duplikater. men i fare for å ødelegge noe lages 2.2 da denne nå skal funke greit på
received, snaps, screens, img, imag, dsc
"""

import os
from util import IMG_file, IMAG_file, DSC_file
import sys
import time
import shutil
import exifread
from datetime import datetime

def print2(string):
    """Print wrapper to controll prints with a switch"""
    global live_info_print
    if live_info_print:
        print(string)
def process_invalid_date_format(date, file):
    """
    date has the form YYYY:MM:DD HH:MM:SS
    for when the HH is set wrong at midnight.
    For file with date format 2017:08:10 24:30:39
    :return: returns correct format (would be 00:30:39 for the example)
    """
    #check format

    try:
        splittet = date.split()
        year, month, day = splittet[0].split(":")
        hour, minute, second = splittet[1].split(":")

        # unknown date
        if year == "0000":
            print2(f"{date} Cant formate date in file: {file}\n")
            return

        # wrong formating. Assume rest is correct
        if hour == "24":
            #print2(f"{year}:{month}:{day} 00:{minute}:{second}")
            return f"{year}:{month}:{day} 00:{minute}:{second}"

    except IndexError as i:
        print2(f"{date} ::: {i} in file: {file}\n")
        return

    except SyntaxError as s:
        print2(f"{date} ::: {s} in file {file}\n")
        return

    except ValueError as v:
        print2(f"{date} ::: {v} in file: {file}\n")
        return
# ==============================================

def get_date_taken(file):
    # not reviewd
    global FORMATCODE_EXIF
    """
    input: base\\filename.ext
    Henter ut opp til 5 date-stamps tilknyttet file
    og returnerer laveste eller ''
    input:  path to image
    output: datetime object (oldest of the 5 dates)
            ""              (no dats found)
    """
    dates = []

    navn, ext = os.path.splitext(file)
    ext = ext.split(".")[-1]

    if ext in HAS_EXIF:
        try:
            # Open image in binary mode
            with open(file, 'rb') as f:

                # Try to fetch exif tags
                tags = exifread.process_file(f)
                for tag in tags.keys():

                    if tag == "EXIF DateTimeOriginal":
                        date = str(tags[tag])
                        if date:
                            dates.append(datetime.strptime(date, FORMATCODE_EXIF))

                    elif tag == "EXIF DateTimeDigitized":
                        date = str(tags[tag])
                        if date:
                            dates.append(datetime.strptime(date, FORMATCODE_EXIF))

                    elif tag == "Image DateTime":
                        date = str(tags[tag])
                        if date:
                            dates.append(datetime.strptime(date, FORMATCODE_EXIF))

        except ValueError as v:
            valid_date = process_invalid_date_format(date, file)
            print2(f"{file} :: {v}")
            if valid_date:
                dates.append(datetime.strptime(valid_date, FORMATCODE_EXIF))

        except Warning as w:
            print2(f"{file} :: {w}")

    # File system dates
    try:
        modified = os.path.getmtime(file)
        date = time.ctime(modified)
        if date:
            dates.append(datetime.strptime(date, FORMATCODE_OS))

        created = os.path.getctime(file)
        date = time.ctime(created)
        if date:
            dates.append(datetime.strptime(date, FORMATCODE_OS))

    except OSError as o:
        print2(f"File does'nt exist or inaccessible\n{file}\n{o}\n")



    if dates:
        oldest = min(dates)
        return oldest
    else:
        print(f"Found no dates\n{file}\n")
        return ""

def get_list_of_types(folder):
    typs = {}
    total = 0; snaps = 0
    screens = 0; no_ext = 0
    received = 0; img = 0
    imag = 0; dsc = 0; rcv = 0

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

            if IMG_file(filename):
                img += 1

            if IMAG_file(filename):
                imag += 1

            if DSC_file(filename):
                dsc += 1

            if not ext in typs:
                typs[ext] = 1
            else:
                typs[ext] += 1
    s = sorted(typs.items(), key=lambda x:x[1], reverse=True)
    s.append(("screens", screens))
    s.append(("snaps", snaps))
    s.append(("received", received))
    s.append(("IMG", img))
    s.append(("IMAG", imag))
    s.append(("DSC", dsc))
    s.append(("no ext", no_ext))
    s.append(("total", total))
    return s

def accepted_file(filename, accepted_formats):
    global counter_no_ext, counter_wrong_ext, counter_snaps_included, counter_screens_included
    global counter_received_included, counter_img_included, counter_imag_included, counter_dsc_included

    """
        Returnerer False for filer som skal skippes
        Returnerer True (TAG) for filer som skal inkluderes
        
        kunne først funnet tag for fil, så brukt den videre.
        om excluded, sjekk tag så count hva slags typer som ble excluded for lettere å få oversikt.
    """

    name, ext = os.path.splitext(filename)
    ext = ext.split(".")[1]

    # Skip no extention
    if not ext:
        print(filename)
        counter_no_ext += 1
        return ''

    # Skip excluded file TYPES
    if not ext in accepted_formats:
        print(filename)
        counter_wrong_ext += 1
        return ''

    # Include ..

    if include_IMG:
        if IMG_file(filename):
            counter_img_included += 1
            return 'mg'

    if include_IMAG:
        if IMAG_file(filename):
            counter_imag_included += 1
            return 'ma'

    if include_DSC:
        if DSC_file(filename):
            counter_dsc_included += 1
            return 'dc'

    if include_SNAP:
        if "Snapchat" in filename:
            counter_snaps_included += 1
            return 'sc'

    if include_SCREEN:
        if "Screenshot" in filename:
            counter_screens_included += 1
            return 'ss'

    if include_RECVD:
        if "received" in filename:
            counter_received_included += 1
            return 'rc'

    return ''

def build_new_filename(filename, date, img_tag):

    global counter_large_file

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
        counter_large_file += 1
        return ''

    # Build new filename
    name, ext = os.path.splitext(filename)
    new_filename = year + month + day + "_" \
                   + hour + minute + second + "-" \
                   + size + "_" + img_tag + ext

    return new_filename





FORMATCODE_EXIF = "%Y:%m:%d %H:%M:%S"
FORMATCODE_OS = "%a %b %d %H:%M:%S %Y"
FORMATCODE_IMG = "%Y%m%d_%H%M%S"

MAX_FILE_SIZE = 8 # size mb < 8 digits large


HAS_EXIF = ["jpg", "jpeg", "JPG"]
accepted_formats = ["jpg", "jpeg", "JPG", "png"] # kamera formats

X = []

counter_files_iterated = 0  # Files iterated

counter_not_accepted = 0    # Files rejected in not accepted()
counter_accepted = 0        # Files not rejected by -/-

counter_large_file = 0      # Files of size 100mb or larger
counter_error_retriving_date = 0 # Couldnt retrive date from filename (IMG file)

counter_no_ext = 0          # Files without an extention
counter_wrong_ext = 0       # Files with another extension then in the accepted list

counter_img_included = 0
counter_imag_included = 0
counter_dsc_included = 0
counter_snaps_included = 0   # Files skipped - "Snapchat" in filename
counter_screens_included = 0 # Files skipped - "Screenshot" in filename
counter_received_included = 0# Files skipped - "received" in filename

counter_already_in_dst = 0  # Files not moved because a file with similar name were found at dst
counter_moved_files = 0     # Files successfully moved

src = "D:\\src\\bilder"
dst = "D:\\full unik sortering 030323" # root

break_loop = False

# include filenames
include_RECVD = False  # ok
include_SCREEN = False   # 1216 fantes fra før
include_SNAP = False   # ok     30 fantes fra før
include_DSC = False      # ok
include_IMAG = False    # ok
include_IMG = False     # ok    2 fantes fra før

live_info_print = True
only_scan = True
main = True
move = False


# IMG= mg, IMAG=ma, DSC=dc, SNAP=sc, SCREEN=ss, RECVD=rc,
# NO TAG=na

# Scan source for types and numbers
print("\nBefore run\n")
types = get_list_of_types(src)
for t in types:
    print(t)

if main:

    for dirpath, dirs, filenames in os.walk(src):
        if break_loop:
            break

        for filename in filenames:

            if counter_accepted == 500:
                break_loop = True
                break

            counter_files_iterated += 1

            # exclude/include files
            img_tag = accepted_file(filename, accepted_formats)
            if not img_tag:
                counter_not_accepted += 1
                continue
            counter_accepted += 1


            srcfile = os.path.join(dirpath, filename)


            # Try to find date taken
            date = get_date_taken(srcfile)
            #print(filename)

            if img_tag == 'mg':
                try:
                    img_date = filename[4:19]
                    temp = datetime.strptime(img_date, FORMATCODE_IMG)
                    if date:
                        if temp < date:
                            date = temp
                    else:
                        date = temp

                except ValueError as v:
                    print(f"Error: filename:{filename}, retrived: {img_date}\nerrorcode: {v}\n")
                    counter_error_retriving_date += 1
                    if not date:
                        continue

            else:
                if not date:
                    counter_error_retriving_date += 1
                    continue


            # build new filename (based on date, time and size)
            new_filename = build_new_filename(filename, date, img_tag)
            #print(filename,  new_filename)

            # build dst path
            if img_tag == 'mg' or img_tag == 'ma' or img_tag == 'dc':
                new_dst = os.path.join(dst, "kamera")

            elif img_tag == 'ss':
                new_dst = os.path.join(dst, "screenshot")

            elif img_tag == 'sc':
                new_dst = os.path.join(dst, "snapchat")

            elif img_tag == 'rc':
                new_dst = os.path.join(dst, "received")
            else:
                print(img_tag, filename)
            # new file
            newfile = os.path.join(new_dst, new_filename)

            # move file if unique
            if not os.path.isfile(newfile):
                if move:
                    shutil.move(srcfile, newfile)
                counter_moved_files += 1
            else:
                #print("Already in dst: ",filename, new_filename)
                counter_already_in_dst += 1
                counter_accepted -= 1



    print(f"\nMOVE: {move}\n")

    print(f"files iterated: {counter_files_iterated}")
    print(f"files accepted: {counter_accepted}")
    print(f"files skipped (not accepted): {counter_not_accepted}")
    print(f"\t no ext: {counter_no_ext}")
    print(f"\t wrong ext: {counter_wrong_ext}")
    print(f"files skipped. coldnt retrive date from name: {counter_error_retriving_date}")
    print(f"files skipped (large size): {counter_large_file}\n")

    print(f"IMG included: {counter_img_included}")
    print(f"IMAG included: {counter_imag_included}")
    print(f"DSC included: {counter_dsc_included}")
    print(f"snaps included: {counter_snaps_included}")
    print(f"screens included: {counter_screens_included}")
    print(f"received included: {counter_received_included}\n")

    print(f"files moved: {counter_moved_files}")
    print(f"files already in dst: {counter_already_in_dst}")

# Scan dst for types and numbers
print("\nAfter run\n")
types = get_list_of_types(new_dst)
for t in types:
    print(t)
