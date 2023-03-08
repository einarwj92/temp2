IMG_PATTERNS = [
"^IMG_MIRROR_\d{8}_\d{6}\.jpg$",                #01  : 9) 192, 96 dst, 96 dup
"^IMG_\d{8}_\d{6}_\d_\(\(F9n3\)\)\.jpg$",       #02  : 6) 1092, 0 dst, 1092 trash
"^IMG_\d{8}_\d{6}_\d_\(\(F9n3\)\)\.png$",       #03  :
"^IMG_\d{8}_\d{6}_\d{3}_\d_\(\(F9n3\)\)\.jpg$", #04  : 7) 13, 0 dst, 13 dup
"^IMG_\d{8}_\d{6}_\d\.jpg$",                    #05  : 2) 62, 24 dst, 38 dup -
"^IMG_\d{8}_\d{6}\.jpg$",                       #06  : 1) 10559, 6375 dst, 4184 dup ('main.py')
"^IMG_\d{8}_\d{6}\.png$",                       #07  : 10) 72, 36 dst, 36 dup !!!( noen som ikke ble med her, de hadde date omvendt)
"^edited_IMG_MIRROR_\d{8}_\d{6}\.jpg$",         #08  :
"^IMG_\d{4}\.JPG\.jpg$",                        #09  :
"^IMG_\d{4}\.JPG$",                             #10  :
"^IMG_\d{8}_\d{6}_edit_\d{15}\.jpg$",           #11  :
"^IMG_\d{8}_\d{6}_\(\d_\)\.jpg$",               #12  : 3) 19, 2 dst, 17 dup
"^IMG_\d{8}_\d{6}_\d{3}\.jpg$",                 #13  : 5) 51, 2 dst, 49 dup
"^IMG_\d{8}_\d{6}_BURST\d{3}\.jpg$",            #14  : 8) 31, 27 dst, 4 dup
"^IMG_\d{8}_\d{6}_BURST\d{3}_COVER\.jpg$",      #15  :
"^FB_IMG_\d{17}\.jpg$",                         #16  :
"^FB_IMG_\d{13}\.jpg$",                         #17  :
"^FB_IMG_\d{13}_\d_\(\(F9n3\)\)\.jpg$",         #18  :
#"^IMG_\d{8}_\d{6}_\(\d_\)\.jpg$",               #19  : !duplikat m 12!
"^IMG_\d{8}\.png$",                             #20  :
"^IMG_\d{8}\.jpg$",                             #21  :
"^IMG_\d{8}_\d{6}-\d\d-\d{2}\.jpeg$",           #22  : 14) 3, 2 dst, 1 dup
"^IMG_\d{8}_\d{6}_\d{2}_\d_\(\(F9n3\)\)\.jpg$", #23  : 11) 5, 0 dst, 5 dup
"^IMG_\d{8}_\d{6}_\d{2}\.jpg$",                 #24  : 4) 17, 0 dst. 17 dup
"^IMG_\d{8}_\d{6}_\d_\d_\(\(F9n3\)\)\.jpg$",    #25  : 12) 3, 0 dst, 3 dup
"^IMG_\d{8}_\d{6}-\d{2}\.jpeg$"                 #26  : 13) 3, 0 dst, 3 dup
]


"""
"^IMG_MIRROR_\d{8}_\d{6}\.jpg$",                #01  :
"^IMG_\d{8}_\d{6}_\d_\(\(F9n3\)\)\.jpg$",       #02  :
"^IMG_\d{8}_\d{6}_\d_\(\(F9n3\)\)\.png$",       #03  :
"^IMG_\d{8}_\d{6}_\d{3}_\d_\(\(F9n3\)\)\.jpg$", #04  :
"^IMG_\d{8}_\d{6}_\d\.jpg$",                    #05  :
"^IMG_\d{8}_\d{6}\.jpg$",                       #06  : 10559, 6375 dst, 4184 dup ('main.py')
"^IMG_\d{8}_\d{6}\.png$",                       #07  :
"^edited_IMG_MIRROR_\d{8}_\d{6}\.jpg$",         #08  :
"^IMG_\d{4}\.JPG\.jpg$",                        #09  :
"^IMG_\d{4}\.JPG$",                             #10  :
"^IMG_\d{8}_\d{6}_edit_\d{15}\.jpg$",           #11  :
"^IMG_\d{8}_\d{6}_(\d_)\.jpg$",                 #12  :
"^IMG_\d{8}_\d{6}_\d{3}\.jpg$",                 #13  :
"^IMG_\d{8}_\d{6}_BURST\d{3}\.jpg$",            #14  :
"^IMG_\d{8}_\d{6}_BURST\d{3}_COVER\.jpg$",      #15  :
"^FB_IMG_\d{17}\.jpg$",                         #16  :
"^FB_IMG_\d{13}\.jpg$",                         #17  :
"^FB_IMG_\d{13}_\d_\(\(F9n3\)\)\.jpg$",         #18  :
"^IMG_\d{8}_\d{6}_\(\d_\)\.jpg$",               #19  :
"^IMG_\d{8}\.png$",                             #20  :
"^IMG_\d{8}\.jpg$",                             #21  :
"^IMG_\d{8}_\d{6}-\d\d-\d{2}\.jpeg$",           #22  :
"^IMG_\d{8}_\d{6}_\d{2}_\d_\(\(F9n3\)\)\.jpg$", #23  :
"^IMG_\d{8}_\d{6}_\d{2}\.jpg$",                 #24  :
"^IMG_\d{8}_\d{6}_\d_\d_\(\(F9n3\)\)\.jpg$",    #25  :
"^IMG_\d{8}_\d{6}-\d{2}\.jpeg$"                 #26  :
"""