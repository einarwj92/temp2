
"""
går gjennom src, printer alle filnavn som ikke matchet noen av patternsa i IMG_PATTERNS
"""

def pattern_in_name(pattern, filename):
    """
    Regex wrapper
    True if match found,
    Else False
    """
    match = re.search(pattern, filename)
    if match:
        return True
    else:
        return False

import os
import re

IMG_PATTERNS = {
"^IMG_MIRROR_\d{8}_\d{6}\.jpg$" : 0,                #01  : -
"^IMG_\d{8}_\d{6}_\d_\(\(F9n3\)\)\.jpg$" : 0,       #02  : -
"^IMG_\d{8}_\d{6}_\d_\(\(F9n3\)\)\.png$" : 0,       #03  :
"^IMG_\d{8}_\d{6}_\d{3}_\d_\(\(F9n3\)\)\.jpg$" : 0, #04  : -
"^IMG_\d{8}_\d{6}_\d\.jpg$" : 0,                    #05  : -
"^IMG_\d{8}_\d{6}\.jpg$" : 0,                       #06  : -
"^IMG_\d{8}_\d{6}\.png$" : 0,                       #07  :     # date omvendt, år først
"^edited_IMG_MIRROR_\d{8}_\d{6}\.jpg$" : 0,         #08  :
"^IMG_\d{4}\.JPG\.jpg$" : 0,                        #09  :
"^IMG_\d{4}\.JPG$" : 0,                             #10  :
"^IMG_\d{8}_\d{6}_edit_\d{15}\.jpg$" : 0,           #11  :
"^IMG_\d{8}_\d{6}_\(\d_\)\.jpg$" : 0,               #12  : -
"^IMG_\d{8}_\d{6}_\d{3}\.jpg$" : 0,                 #13  : -
"^IMG_\d{8}_\d{6}_BURST\d{3}\.jpg$" : 0,            #14  :
"^IMG_\d{8}_\d{6}_BURST\d{3}_COVER\.jpg$" : 0,      #15  :
"^FB_IMG_\d{17}\.jpg$" : 0,                         #16  :
"^FB_IMG_\d{13}\.jpg$" : 0,                         #17  :
"^FB_IMG_\d{13}_\d_\(\(F9n3\)\)\.jpg$" : 0,         #18  :
"^IMG_\d{8}\.png$" : 0,                             #20  :
"^IMG_\d{8}\.jpg$" : 0,                             #21  :
"^IMG_\d{8}_\d{6}-\d\d-\d{2}\.jpeg$" : 0,           #22  : -
"^IMG_\d{8}_\d{6}_\d{2}_\d_\(\(F9n3\)\)\.jpg$" : 0, #23  : -
"^IMG_\d{8}_\d{6}_\d{2}\.jpg$" : 0,                 #24  : -
"^IMG_\d{8}_\d{6}_\d_\d_\(\(F9n3\)\)\.jpg$" : 0,    #25  : -
"^IMG_\d{8}_\d{6}-\d{2}\.jpeg$" : 0                 #26  : -
}

src = "E:\\media\\bilder\\s"

img_filenames = []  # alle filenames
img_count = 0
for dirpath, dirnames, filenames in os.walk(src):
    for filename in filenames:
        if "IMG" in filename:
            img_count += 1
            found = False
            for pattern in IMG_PATTERNS:
                if pattern_in_name(pattern, filename):
                    found = True
                    IMG_PATTERNS[pattern] += 1
                    break # ikke testet
            if not found:
                img_filenames.append(filename)
                print(filename)

"""
sorted_list = sorted(img_filenames) # alle filenames sortert. nødvendig??
for n in sorted_list:
    print(n)
"""
sorted_list = sorted(IMG_PATTERNS.items(), key=lambda x:x[1], reverse=True)
for n in sorted_list:
    if not n[1] == 0:
        print(n)
print(img_count)