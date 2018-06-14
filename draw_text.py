#!/usr/bin/env python

import eink
import ImageFont
import ImageDraw
import sys

def parse(text):
    s = ['', '']
    i = 0
    for c in text:
        if c == '*':
            i = 1 - i
        else:
            s[i] += c
            if c.isspace():
                s[1-i] += c
            else:
                s[1-i] += ' '
    return s[0], s[1]

def draw_text(text, size=12):
    ink = eink.Eink()
    font = ImageFont.truetype('DejaVuSansMono.ttf', size)

    # generate images
    img = ink.new()

    d = ImageDraw.ImageDraw(img)
    text_black, text_red = parse(text)
    width, height = d.multiline_textsize(text_black, font)
    pos = (img.width - width)/2, (img.height - height)/2
    d.multiline_text(pos, text_black, eink.BLACK, font)
    d.multiline_text(pos, text_red, eink.RED, font)

    # display images
    ink.display(img)

def main():
    draw_text(sys.argv[2], int(sys.argv[1]))

if __name__ == '__main__':
    main()
