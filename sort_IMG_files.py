import os
import util

"""
Går gjennom alle IMG-filer i media\\bilder, gir de nytt navn og flytter de til dst.
De som finnes i dst flttes til destrueringsfolder med postfix
"""

src = "E:\\media\\bilder\\s1"


for dirpath, dirnames, filenames in os.walk(src):
    for filename in filenames:
        if util.IMG_file(filename):
            # flytt

            date = get_date_taken(srcfile)


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