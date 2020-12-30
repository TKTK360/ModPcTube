import sys
import adbfunc


if __name__ == "__main__":
    args = sys.argv
    n = len(args)

    adbObj = adbfunc.ADBFuncClass()

    if n > 1:
        ip = args[1]
        adbObj.setIpAddress(ip)

    adbObj.mainLoop()
