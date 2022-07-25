# -*- coding: utf-8 -*-
import sys
import glob
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark(post_name):
    if post_name == 'all':
        post_name = '*'
    dir_name = '/Users/zhangkanqi/myblog/public/articleImages/' + post_name + '/*'
    for files in glob.glob(dir_name):
        im = Image.open(files)
        if len(im.getbands()) < 3:
            im = im.convert('RGB')
            print(files)
        font = ImageFont.truetype('STSong.ttf',  int(im.size[1] / 20))
        draw = ImageDraw.Draw(im)
        mywatermask = '@kkqq'
        draw.text((im.size[0]-font.size*0.6*len(mywatermask), im.size[1]-font.size*1.5),
                  mywatermask, fill=(255, 255, 255), font=font)
        im.save(files)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        watermark(sys.argv[1])
    else:
        print('[usage] <input>')

