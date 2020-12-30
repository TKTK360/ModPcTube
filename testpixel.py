import sys
import time
#import pixelfunc
import subprocess
from subprocess import call


def pixelEffect(cmd):
    print(cmd)
    subprocess.call("sudo python3 callpixel.py " + str(cmd), shell=True)

if __name__ == "__main__":
    pixelEffect(0)
    
    #pixelObj = pixelfunc.PixelFuncClass()

    #pixelObj.rainbow_cycle(0.001)
    #pixelObj.clear_pixel()
    
    #pixelObj.rightToLeft_cycle(0.05,128,128,0)
    #time.sleep(1)
    #pixelObj.clear_pixel()

    #pixelObj.leftToRight_cycle(0.05,128,128,0)
    #time.sleep(1)
    #pixelObj.clear_pixel()

    #pixelObj.edgeToCenter_cycle(0.08,0,255,0)
    #time.sleep(1)
    #pixelObj.clear_pixel()

    #pixelObj.centerToEdge_cycle(0.08,0,255,0)
    #time.sleep(1)
    #pixelObj.clear_pixel()

