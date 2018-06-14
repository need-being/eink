import epd2in13b
import Image

WHITE = 0
BLACK = 1
RED = 2

class Eink:
    def __init__(self):
        self.epd = epd2in13b.EPD()
        self.epd.init()

    def new(self):
        img = Image.new("P", (self.epd.height, self.epd.width))
        img.putpalette([255,255,255,0,0,0,255,0,0])
        return img

    @staticmethod
    def extract(img, color):
        img = img.copy()
        px = img.load()
        for x in xrange(0, img.width):
            for y in xrange(0, img.height):
                if px[x,y] == color:
                    px[x,y] = BLACK
                else:
                    px[x,y] = WHITE
        return img.convert("1")

    def display(self, img):
        img = img.transpose(Image.ROTATE_270)
        frame_black = self.epd.get_frame_buffer(self.extract(img, BLACK))
        frame_red = self.epd.get_frame_buffer(self.extract(img, RED))
        self.epd.display_frame(frame_black, frame_red)
