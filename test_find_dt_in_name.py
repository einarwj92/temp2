import re
import const
date = const.year + const.month + const.day
def find_pattern_in_name(pattern, filename):
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


print(find_pattern_in_name(date, "abc20160911hei"), True)
print(find_pattern_in_name(date, "abc10160911hei"), False)
print(find_pattern_in_name(date, "20161511hei"), False)
print(find_pattern_in_name(date, "abc20160931"), True)
print(find_pattern_in_name(date, "abc2016091hei"), False)