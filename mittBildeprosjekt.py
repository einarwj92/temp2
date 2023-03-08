import os
import util
import shutil

dst = "D:\\sortering230223\\unike bilder"
src = "D:\\dobbeltsjekk\\uten snaps\\batch1"

IMAGE_EXT = ["jpg", "png", "jpeg", "JPG", "gif", "tif"]
VIDEO_EXT = ["mp4"]
MEDIA_EXT = IMAGE_EXT + VIDEO_EXT

counter_files = 0
counter_accepted = 0
counter_new_name = 0

counter_unique = 0
counter_same_name = 0
counter_duplikat = 0
counter_postfix = 0
counter_wo_postfix_exists_ondst = 0
counter_wo_postfix_exists_andeqlsize = 0
counter_moved = 0

scan_src = True
main = True
move = False

if scan_src:
    types = util.get_list_of_types(src)
    for t in types:
        print(t)

if main:
    for dirpath, dirs, filenames in os.walk(src):

        # Gå gjennom src
        for filename in filenames:

            counter_files += 1

            # == not accepted ==
            splittet = filename.split('.')
            if len(splittet) < 2:
                continue

            ext = splittet[-1]
            if not ext in IMAGE_EXT:
                continue

            if "Snapchat" in filename:
                continue

            if "Screenshot" in filename:
                continue
            # ====================

            counter_accepted += 1

            # no postfix removed
            file_in_src = os.path.join(dirpath, filename) # file in src
            file_in_dst = os.path.join(dst, filename)     # corresponding file in dst

            # postfix removed
            filename_pfix_rmd = util.ends_with_postfix(filename) # evt postfix removed from src filename
            file_in_dst_pfix_rmd = os.path.join(dst, filename_pfix_rmd)

            postfix_in_name = filename_pfix_rmd



            if postfix_in_name:
                counter_postfix += 1
                #print(filename, util.ends_with_postfix(filename))

                if os.path.isfile(file_in_dst_pfix_rmd):
                    counter_wo_postfix_exists_ondst += 1

                    if util.equal_size(file_in_src, file_in_dst_pfix_rmd):
                        counter_wo_postfix_exists_andeqlsize += 1
                        print("*** same size", filename, util.ends_with_postfix(filename))
                    else:
                        print("not same size", filename, util.ends_with_postfix(filename))

            else:
                continue

            src_image = os.path.join(dirpath, filename)
            dst_image = os.path.join(dst, filename)

            # unique - move
            if not os.path.isfile(dst_image):
                print(dst_image)
                if move:
                    shutil.move(src_image, dst_image)
                counter_unique += 1
                counter_moved += 1

            # same name - check size
            else:
                counter_same_name += 1
                # same name and size - ignore file
                if util.equal_size(src_image, dst_image):
                    counter_duplikat += 1
                    continue

                # different size - give new name and move
                else:
                    #find new name
                    nn = util.find_new_name(dst_image)
                    #print(f"old name: {dst_image}\tnew name: {nn}")
                    if move:
                        shutil.move(src_image, nn)
                    counter_new_name += 1
                    counter_moved += 1

    print(f"total files: {counter_files}")
    print(f"ends with postfix: {counter_postfix}")
    print(f"without postfix exists on dst: {counter_wo_postfix_exists_ondst}")
    print(f"- and {counter_wo_postfix_exists_andeqlsize} had same size too")
    print(f"accepted files: {counter_accepted}\n")
    print(f"unique name: {counter_unique}")
    print(f"not unique name: {counter_same_name}")
    print(f"- same name, same size (duplikat): {counter_duplikat}")
    print(f"- same name different size: {counter_new_name}\n")
    print(f"moved: {counter_moved}")

"""
        if postfix:
            print(filename)
            filer_med_postfix += 1
        else:
            filer_uten_postfix += 1
"""
"""
            # Sjekk om filen allerede finnes uten postfix.
            file_without_postfix = os.path.join(dirpath, filename_without_postfix)
            file_with_postfix = os.path.join(dirpath, filename)
            exists = os.path.isfile(file_without_postfix)

            if not exists:
                # rename til uten postfix
                print(filename, filename_without_postfix)
                if action:
                    os.rename(file_with_postfix, file_without_postfix)
                    pass
                renames += 1


            else:
                # Sjekk om samme størrelse
                with_postfix_size = os.path.getsize(file_with_postfix)
                without_postfix_size = os.path.getsize(file_without_postfix)
                orig_exists += 1
                # Samme størrelse - Filen med postfix og uten postfix har samme størrelse
                if without_postfix_size == with_postfix_size:
                    if action:
                        dstfile = os.path.join("D:\\sortering230223\\hm2", filename)
                        shutil.move(file_with_postfix, dstfile)
                        #os.remove(file_with_postfix)
                    removes += 1
                # Forskjellig størrelse - unik, la den beholde postfix
                
                else:
                    print("flyttes")
                    #passes += 1
                    if action:

                        shutil.move(file_with_postfix, file_without_postfix)
                    flyttes += 1
"""

#print(f"Totalt antall filer: {totalt_antall_filer}")
#print(f"Filer uten postfix:                 {filer_uten_postfix}")
#print(f"Filer med postfix (kan være unike): {filer_med_postfix}")
#if (filer_med_postfix + filer_uten_postfix) != totalt_antall_filer:
#    print("Error i telling")
#print("renames:",renames)
#print(f"\nFiler med postfix, uten tilsvarende original - flyttes med nytt navn: {flyttes_nyttnavn}")
#print(f"Filer med postfix -med tilsvarende original: {orig_exists}")
#print(f"\t\t\tDe hadde samme størrelse - remove(): {removes}")
#print(f"\t\t\tDe hadde ulik størrelse - pass {passes}")
#print("flyttende filer", flyttes)