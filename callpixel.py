import sys
import time
import pixelfunc


if __name__ == "__main__":
    args = sys.argv
    n = len(args)

    if n > 1:
        cmd = int(args[1])
        #print(cmd)

        pixelObj = pixelfunc.PixelFuncClass()
        
        if cmd == 0:
            pixelObj.rainbow_cycle(0.001)
            pixelObj.clear_pixel()

        elif cmd == 1:
            pixelObj.rightToLeft_cycle(0.05,0,255,0)
            time.sleep(0.6)
            pixelObj.clear_pixel()

        elif cmd == 2:
            #print("leftToRight_cycle")
            pixelObj.leftToRight_cycle(0.05,50,255,0)
            time.sleep(0.6)
            pixelObj.clear_pixel()

        elif cmd == 3:
            pixelObj.edgeToCenter_cycle(0.08,0,50,255)
            time.sleep(0.6)
            pixelObj.clear_pixel()

        elif cmd == 4:
            pixelObj.centerToEdge_cycle(0.08,0,150,255)
            time.sleep(0.6)
            pixelObj.clear_pixel()

        elif cmd == 5:
            pixelObj.clear_pixel()
            
        elif cmd == 6:
            pixelObj.fill_cycle(0.08,0,0,255)
            time.sleep(0.6)
            pixelObj.clear_pixel()
                
