#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
import threading
from threading import Thread
import board
import busio
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

def firstLED():
        i=0
        blinks=5
        while (i < blinks):

                GPIO.setup (24, GPIO.OUT)
                GPIO.output (24, GPIO.HIGH)
                time.sleep(1)
                GPIO.output (24, GPIO.LOW)
                time.sleep(1)

                i=i+1
        return;

def secondLED():
        i=0
        blinks=3
        while (i < blinks):

                GPIO.setup (18, GPIO.OUT)
                GPIO.output (18, GPIO.HIGH)
                time.sleep(1)
                GPIO.output (18, GPIO.LOW)
                time.sleep(1)

                i=i+1
        return;
		
if __name__=='__main__':
    first_thread = Thread(target = firstLED)
    second_thread = Thread(target = secondLED)
    first_thread.start()
    second_thread.start()

    #DO STUFF HERE INSTEAD OF JUST WAITING?
      
    #wait for threads to finish
    first_thread.join()
    second_thread.join()

    print ("All done")
    GPIO.cleanup()
