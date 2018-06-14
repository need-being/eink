import eink
import Image
import ImageFont
import ImageDraw
import sys

def draw_text(text, size=12):
    ink = eink.Eink()
    font = ImageFont.truetype('DejaVuSerif.ttf', size)

    # generate images
    img = ink.new()

    d = ImageDraw.ImageDraw(img)
    width, height = d.multiline_textsize(text, font)
    d.multiline_text(((img.width - width)/2, (img.height - height)/2), text, eink.BLACK, font)

    # display images
    ink.display(img)

def main():
    draw_text(sys.argv[2], int(sys.argv[1]))

if __name__ == '__main__':
    main()
