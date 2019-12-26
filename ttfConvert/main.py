# -*- coding: cp949 -*-
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont  # pillow
from text_reader import get_2350
import colorsys


font_path = "font/"  # ��Ʈ ���� ���
fonts = os.listdir(font_path)  # ���� ��ο��ִ� ttf ���� ������ str

co = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
# start = "AC00"
# end = "D7A3"
start = "1100"
end = "11FF"
lst_2350 = get_2350()  # �ѱ� 2350�� ����Ʈ�� �����´�

co = co.split(" ")

Hangul_Syllables = [a+b+c+d
                    for a in co
                    for b in co
                    for c in co
                    for d in co]

Hangul_Syllables = np.array(Hangul_Syllables)

s = np.where(start == Hangul_Syllables)[0][0]
e = np.where(end == Hangul_Syllables)[0][0]

Hangul_Syllables = Hangul_Syllables[s : e + 1]

print(Hangul_Syllables)
print(len(Hangul_Syllables))
print(chr(int('AC00', 16)), chr(int("D7A3", 16)))

unicodeChars = chr(int(Hangul_Syllables[245], 16))
print(unicodeChars)

plt.figure(figsize=(15, 15))

"""
matplotlib�� ����ش� Test
"""
for idx, ttf in enumerate(fonts):  # idx = �ε���, ttf = ���ϸ�
    font = ImageFont.truetype(font=font_path + ttf, size=100)
    x, y = font.getsize(unicodeChars)

    theImage = Image.new('RGB', (x + 3, y + 3), color='white')

    theDrawPad = ImageDraw.Draw(theImage)

    theDrawPad.text((0, 0), unicodeChars[0], font=font, fill='black')
    #  ���⼭ font �� 2530�� �����ϴ��� �˻� ����?

    plt.subplot("24{}".format(str(idx + 1)))

    plt.title(str(ttf))

    plt.imshow(theImage)

plt.show()

"""
matplotlib�� ����ذ� png���Ϸ� ��ȯ
"""
# for uni in Hangul_Syllables:
#     unicodeChars = chr(int(uni, 16))
#
#     path = "./Hangul_Syllables/" + unicodeChars
#
#     os.makedirs(path, exist_ok=True)
#
#     for ttf in fonts:
#         font = ImageFont.truetype(font=font_path + ttf, size=100)
#
#         x, y = font.getsize(unicodeChars)
#
#         theImage = Image.new('RGB', (x + 3, y + 3), color='white')
#
#         theDrawPad = ImageDraw.Draw(theImage)
#
#         theDrawPad.text((0.0, 0.0), unicodeChars[0], font=font, fill='black')
#
#         msg = path + "/" + ttf[:-4] + "_" + unicodeChars
#
#         theImage.save('{}.png'.format(msg))



