import serial
from time import sleep
import sys
import os
from dotenv import load_dotenv
import random
from playaudio import playaudio

COM = 'COM6'
BAUD = 9600

load_dotenv()

ser = serial.Serial(COM, BAUD, timeout=.1)

print('Waiting for device')
sleep(3)
print(ser.name)

# check args #run with py monitor.py --monitor
if ("-m" in sys.argv or "--monitor" in sys.argv):
    monitor = True
else:
    quit()

try:
    while True:
        rand = random.randint(1, 3)
        # Capture serial output as a decoded string
        val = str(ser.readline().decode().strip('\r\n'))
        
        #parse int value
        if (val[-2:]):
            num = int(val[-2:])

        if (monitor == True):
            # print(val, end="\r", flush=True) #full output
            print(num, end="\r", flush=True)

        #will need to tweak for osil
        if (num > 6):
            playaudio(os.getenv("ABS_PATH") + "audio" + str(rand) + ".mp3")
        
except KeyboardInterrupt:
    quit()

