# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:40:28 2021

@author: Administrator
"""

import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib import pyplot as plt
import random
from palettable.colorbrewer.sequential import YlGnBu_9

text = open('test.txt', 'r',encoding= 'UTF-8-sig').read()
text =' '.join(jieba.cut(text))
icon_path ='icon.png'
icon = Image.open(icon_path)
mask = Image.new("RGB" ,icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)


def color_func(word, font_size,position,orientation, random_state=None, **kwargs):
    return tuple(YlGnBu_9.colors[random.randint(0,8)])

font_path = 'SNsanafonGyou.ttf'
wc = WordCloud(font_path=font_path,background_color="black",max_words=2000,\
               mask=mask,max_font_size=300,random_state=1)
wc.generate_from_text(text)
wc.recolor(color_func=color_func,random_state=2)

output_path = 'wordcloud.png'
wc.to_file(output_path)

plt.rcParams["figure.figsize"]=(25,25)#字装游
plt.imshow(wc)
plt.axis("off")
plt.show()
