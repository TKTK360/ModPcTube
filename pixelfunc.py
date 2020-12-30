import time
import board
import neopixel


class PixelFuncClass:
    pixel_pin = board.D21

    # The number of NeoPixels
    num_pixels = 8

    # The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
    # For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
    ORDER = neopixel.GRB

    def __init__(self):
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False,
                                   pixel_order=self.ORDER)

    def wheel(self,pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos*3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos*3)
            g = 0
            b = int(pos*3)
        else:
            pos -= 170
            r = 0
            g = int(pos*3)
            b = int(255 - pos*3)
        return (r, g, b) if self.ORDER == neopixel.RGB or self.ORDER == neopixel.GRB else (r, g, b, 0)


    def rainbow_cycle(self,wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
                
            self.pixels.show()
            time.sleep(wait)


    def clear_pixel(self):
        self.pixels.fill((0, 0, 0))
        # Uncomment this line if you have RGBW/GRBW NeoPixels
        # pixels.fill((255, 0, 0, 0))
        self.pixels.show()

    def rightToLeft_cycle(self,wait,r,g,b):
        self.clear_pixel()
        
        for i in range(self.num_pixels):
            self.pixels[i] = (r, g, b)
            self.pixels.show()
            time.sleep(wait)

    def leftToRight_cycle(self,wait,r,g,b):
        self.clear_pixel()
        len = self.num_pixels
        for i in range(len):
            self.pixels[len - 1 - i] = (r, g, b)
            self.pixels.show()
            time.sleep(wait)

    def edgeToCenter_cycle(self,wait,r,g,b):
        self.clear_pixel()
        len = self.num_pixels
        halfLen = int(len / 2)
        
        for i in range(halfLen):
            self.pixels[i] = (r, g, b)
            self.pixels[len - 1 - i] = (r, g, b)
            
            self.pixels.show()
            time.sleep(wait)

    def centerToEdge_cycle(self,wait,r,g,b):
        self.clear_pixel()
        len = self.num_pixels
        halfLen = int(len / 2)
        
        for i in range(halfLen):
            self.pixels[halfLen - 2 - i] = (r, g, b)
            self.pixels[halfLen - 1 + i] = (r, g, b)
            
            self.pixels.show()
            time.sleep(wait)

    def fill_cycle(self,wait,r,g,b):
        self.clear_pixel()
        self.pixels.fill((r,g,b))
        self.pixels.show()
        time.sleep(wait)
