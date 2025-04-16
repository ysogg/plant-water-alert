import serial
from time import sleep
import sys


COM = 'COM6'
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout=.1)

print('Waiting for device')
sleep(3)
print(ser.name)

# check args
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

        
    if (num > 6):
        print("GOT")

