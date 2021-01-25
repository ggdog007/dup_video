import numpy as np
import os
import re
from PIL import Image
import imagehash


def creat_imgharsh_list(path):
    path_list = []
    for (root, dirs, files) in os.walk(path, topdown=True):
        for file in files:
            if re.match('(.*)\.jpg', file):
                path_list.append(file)

    return path_list


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = r'H:\eh\~Temp2\H-anime\other\Short source filmmaker\temp\sfm\sound\wow'
    jpg_list = creat_imgharsh_list(path)

    for jpg in jpg_list:



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
