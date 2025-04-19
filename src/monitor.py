import serial
from time import sleep
import sys
import os
from dotenv import load_dotenv

import simpleaudio as sa

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
    monitor = False

while True:
    # Capture serial output as a decoded string
    val = str(ser.readline().decode().strip('\r\n'))

    #parse int value
    if (val[-2:]):
        num = int(val[-2:])

    if (monitor == True):
        # print(val, end="\r", flush=True) #full output
        print(num, end="\r", flush=True)

    #will need to tweak    
    if (num > 6):
        print("GOT")
        wave_obj = sa.WaveObject.from_wave_file(os.getenv("ABS_PATH")) #set absolute path to audio file here
        play_obj = wave_obj.play()
        play_obj.wait_done()