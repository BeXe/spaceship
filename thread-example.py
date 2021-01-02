#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
import threading
from threading import Thread

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
