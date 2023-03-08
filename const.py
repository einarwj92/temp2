year = "20(0[0-9]|1[0-9]|2[0-9])"
month = "(0[1-9]|1[0-2])"
day = "(0[1-9]|1[0-9]|2[0-9]|3[01])"

hour = "([01]\d|2[0-3])"
minute = "[0-5]\d"
second = "[0-5]\d"

orig_img_pattern06 = "IMG_" + year + month + day + '_' + hour + minute + second + "\.jpg"
orig_img_pattern05 = "IMG_" + year + month + day + '_' + hour + minute + second + "_\d\.jpg"
orig_img_pattern12 = "IMG_" + year + month + day + '_' + hour + minute + second + "_\(\d_\)\.jpg"
orig_img_pattern24 = "IMG_" + year + month + day + '_' + hour + minute + second + "_\d{2}\.jpg"
orig_img_pattern13 = "IMG_" + year + month + day + '_' + hour + minute + second + "_\d{3}\.jpg"
orig_img_pattern02 = "IMG_" + year + month + day + '_' + hour + minute + second + "_\d_\(\(F9n3\)\)\.jpg"
orig_img_pattern04 = "IMG_" + year + month + day + '_' + hour + minute + second + "_\d{3}_\d_\(\(F9n3\)\)\.jpg"
orig_img_pattern14 = "IMG_" + year + month + day + '_' + hour + minute + second + "_BURST\d{3}\.jpg"
orig_img_pattern01 = "^IMG_MIRROR_" + year + month + day + '_' + hour + minute + second + "\.jpg$"    # slice fra ny index pga dato. glemte å legge til ^$ på de øvrige!! matched evt wider, tror det ikke skal ha matchet for mye rart
orig_img_pattern23 = "^IMG_" + year + month + day + '_' + hour + minute + second + "_\d{2}_\d_\(\(F9n3\)\)\.jpg$"
orig_img_pattern25 = "^IMG_" + year + month + day + '_' + hour + minute + second + "_\d_\d_\(\(F9n3\)\)\.jpg$"


orig_img_pattern26 = "^IMG_" + year + month + day + '_' + hour + minute + second + "-\d{2}\.jpeg$"
orig_img_pattern22 = "^IMG_" + year + month + day + '_' + hour + minute + second + "-\d{2}-\d{2}\.jpeg$"


orig_img_pattern07 = "^IMG_" + year + month + day + '_' + hour + minute + second + "\.png$"
