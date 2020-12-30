# -*- coding: utf-8 -*-
import os
import sys
import termios
import time
import subprocess
from subprocess import call
import requests


class ADBFuncClass:
    _isAdb = False
    _isVoice = False
    CARD = 0
    DEVICE = 0
    
    RECDEV = 0
    RECCD = 1
    rec_time = 2
    rec_path = 'temp.wav'
    
    DOCOMO_API = 'XXXXXXXXXXXXXXXXXXXXX'
    URL_RECOG = 'https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY='

    def __init__(self):
        self.pixelEffect(5)
        time.sleep(0.25)        

    def playSound(self, file):
        print(file)
        os.system('aplay -D plughw:{},{} {}'.format(self.CARD, self.DEVICE, file))

    def pixelEffect(self, cmd):
        print(cmd)
        subprocess.call("sudo python3 callpixel.py " + str(cmd), shell=True)
        
        
    def leftFunction(self):
        print("Left")
        if self._isAdb:
            call(["adb","shell","input","keyevent","21"])
            
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("swipe.wav")
            
        self.pixelEffect(1)
        #self.swipeSound.play()
        #time.sleep(1.25)

    def rightFunction(self):
        print("Right")
        if self._isAdb:
            call(["adb","shell","input","keyevent","22"])

        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("swipe.wav")
            
        self.pixelEffect(2)
        #self.swipeSound.play()
        #time.sleep(1.25)

    def upFunction(self):
        print("Up")
        if self._isAdb:
            call(["adb","shell","input","keyevent","19"])

        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("swipe.wav")
            
        self.pixelEffect(3)
        #self.swipeSound.play()
        #time.sleep(1.25)

    def downFunction(self):
        print("Down")
        if self._isAdb:
            call(["adb","shell","input","keyevent","20"])
        
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("swipe.wav")
            
        self.pixelEffect(4)
        #self.swipeSound.play()
        #time.sleep(1.25)

    def selectFunction(self):
        print("Select")
        if self._isAdb:
            call(["adb","shell","input","keyevent","KEYCODE_DPAD_CENTER"])
        
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("enter.wav")
            
        self.pixelEffect(0)
        #self.enterSound.play()
        #time.sleep(1.25)
        
    def menuFunction(self):
        print("Menu")
        if self._isAdb:
            call(["adb","shell","input","keyevent","1"])
        
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("enter.wav")

        self.pixelEffect(6)
        #self.enterSound.play()
        #time.sleep(1.25)

    def playPauseFunction(self):
        print("Play / Pause")
        if self._isAdb:
            call(["adb","shell","input","keyevent","85"])
        
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("playpause.wav")
            
        self.pixelEffect(6)
        #self.playPauseSound.play()
        #time.sleep(1.25)

    def homeFunction(self):
        print("Home")
        if self._isAdb:
            call(["adb","shell","input","keyevent","3"])
        
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("enter.wav")

        self.pixelEffect(6)
        #self.enterSound.play()
        #time.sleep(1.25)

    def returnFunction(self):
        print("Return")
        if self._isAdb:
            call(["adb","shell","input","keyevent","4"])
        
        if self._isVoice:
            self.playSound("vkashi.wav")
        else:
            self.playSound("return.wav")
            
        self.pixelEffect(6)
        #self.returnSound.play()
        #time.sleep(1.25)


    def mainLoop(self):
        fd = sys.stdin.fileno()

        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)

        new[3] &= ~termios.ICANON
        new[3] &= ~termios.ECHO


        try:
            while True:
                #KeyEvent
                termios.tcsetattr(fd, termios.TCSANOW, new)
                ch = sys.stdin.read(1)
                #print(ch)
                
                if ch == '4':
                    self.leftFunction()
                elif ch == '6':
                    self.rightFunction()
                elif ch == '8':
                    self.upFunction()
                elif ch == '2':
                    self.downFunction()
                
                elif ch == '5':
                    self.selectFunction()
                elif ch == '9':
                    self.menuFunction()
                elif ch == '3':
                    self.playPauseFunction()
                elif ch == '1':
                    self.homeFunction()
                elif ch == '7':
                    self.returnFunction()
                    
                elif ch == 's':
                    self.voiceFunction()

        finally:
            termios.tcsetattr(fd, termios.TCSANOW, old)

    def setIpAddress(self,ip):
        self._isAdb = True

        print(ip)
        print("ADB ON")
        call(["adb","kill-server"])
        call(["adb","start-server"])
        call(["adb","connect", ip])

    def voiceFunction(self):
        print("Voice")
        self.pixelEffect(0)
        self.playSound("vgoyou.wav")

        a1 = 'sudo arecord -r 16000 -f S16_LE -d ' + str(self.rec_time) + ' -D plughw:{},{} '.format(self.RECCD, self.RECDEV) + self.rec_path
        subprocess.call(a1, shell=True)
        
        url = self.URL_RECOG + self.DOCOMO_API
        
        files = {"a": open(self.rec_path, 'rb'), "v": "on"}
        #files = {"a": open('vkashi.wav', 'rb'), "v": "on"}
        
        r = requests.post(url, files=files)
        print(r.text)
        
        rec = r.json()['text']
        txt = rec.encode('utf-8')
        print(txt)
        
        self._isVoice = True
        
        #Enter
        if '決定' in txt or '選択' in txt or '見' in txt:
            self.selectFunction()
            
        #Play-Pause
        elif '再生' in txt or '止' in txt or 'プレ' in txt or 'ポーズ' in txt:
            self.playPauseFunction()
        
        #Return
        elif '戻' in txt or 'キャンセル' in txt:
            self.returnFunction()
        
        #Home
        elif 'ホーム' in txt:
            self.homeFunction()
            
        else:
            print("None")
            self.playSound("vnone.wav")
            
        self._isVoice = False
            
        