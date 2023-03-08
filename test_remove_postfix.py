def remove_postfix(filename):

    # antar filnavn(tall).ext   len(tall) = 6/5
    #     "IMG_20210114_153946(613824).jpg"

    if "IMG" in filename:
        if len(filename) == 31:
            left = filename[:19]
            right = filename[27:]
            return left + right

        elif len(filename) == 30:
            left = filename[:19]
            right = filename[26:]
            return left + right

    return ""


if __name__ == "__main__":
    tests = {
        "IMG_20210114_153946(123456).jpg" : "IMG_20210114_153946.jpg",
        "IMG_20210114_153946(12345).jpg": "IMG_20210114_153946.jpg"
    }

    for t in tests:
        #print(ends_with_postfix(t) == tests[t])
        print(ends_with_postfix(t))