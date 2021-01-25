import numpy as np
import pandas as pd
import os
import re
from PIL import Image
import imagehash

"""
根据path文件夹生成一个video.jpg 的list
"""
def creat_img_list(path):
    path_list = []
    for (root, dirs, files) in os.walk(path, topdown=True):
        for file in files:
            if re.match('(.*)\.jpg', file):
                path_list.append(file)
    return path_list

"""
返回path下每个jpg文件的imagehash值
"""
def get_imagehash(series):
    path = r'H:\eh\~Temp2\H-anime\other\Short source filmmaker\temp\sfm\sound\wow'
    return imagehash.phash(Image.open(os.path.join(path, series['jpg'])))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


"""
根据path中jpg图片比较相似imagehash的值，将相近hash值的jpg做成一个dataframe，然后将这些个dataframe放到一个list中
"""
if __name__ == '__main__':
    path = r'H:\eh\~Temp2\H-anime\other\Short source filmmaker\temp\sfm\sound\wow'
    jpg_list = creat_img_list(path)
    # print(jpg_list)
    df = pd.DataFrame(data=jpg_list, columns=['jpg'])
    df['hash'] = df.apply(get_imagehash, axis=1)

    # black = imagehash.phash(Image.open(r'C:\pyworkplace\dup_video\black.jpg'))

    print(df)

    similar_list = []

    while not df.empty:

        b = []
        d = []
        base = df['hash'].iloc[0]

        # print(base)

        for index, row in df.iterrows():
            # print(row)
            if base == row['hash']:
                b.append(row)
                # print(b)
            else:
                d.append(row)

        b_df = pd.DataFrame(b)
        df = pd.DataFrame(d)

        if len(b_df) > 1:
            similar_list.append(b_df)

    print(similar_list)
    print(len(similar_list))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
