import os

CARD = 0
DEVICE = 0

os.system('aplay -D plughw:{},{} playpause.wav'.format(CARD, DEVICE))
