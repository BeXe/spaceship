#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)
import threading
from threading import Thread
import board
import busio
from adafruit_ht16k33 import segments
import os
import sys
from subprocess import Popen

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

# Button Variables connected to which GPIO pin.
button1=9

# Led variables, connected tot which GPIO pin
LED1=24

# GPIO input setup
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1 an input, Activate Pull UP Resistor

# GPIO output setup
GPIO.setup(LED1,GPIO.OUT,) # Make LED 1 an Output

# set led off at start
BS1=False                  # Set Flag BS1 to indicate LED is initially off

movie1 = ("/home/pi/movie/aurora.mp4")

def buttonLOOP():
        while(1):                  # Create an infinite Loop
                if GPIO.input(button1)==0:            # Look for button 1 press
                        print ("Button 1 Was Pressed:")
                        if BS1==False:                # If the LED is off
                                GPIO.output(LED1,True) # turn it on
                                BS1=True              # Set Flag to show LED1 is now On 
                                sleep(.5)             # Delay
                                time.sleep(2)

                                for i in range(10, -1, -1):
                                   print('{num:06d}'.format(num=i))
                                   display.fill(0)
                                   display.print(':')
                                   display.print('{num:06d}'.format(num=i))
                                   time.sleep(1)                         
                        else:                         # If the LED is on
                                GPIO.output(LED1,False) # Turn LED off
                                BS1=False               # Set Flag to show LED1 is now Off
                                sleep(.5)

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
       for i in range(10, -1, -1):
                print('{num:06d}'.format(num=i))
   # print('{num:02d}'.format(num=i))
                display.fill(0)
                display.print(':')
   # display.print(i)
                display.print('{num:06d}'.format(num=i))
                time.sleep(1)
#        return;

def thirdLED():
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie1])

if __name__=='__main__':
    button_thread = Thread(target = buttonLOOP)
    first_thread = Thread(target = firstLED)
    second_thread = Thread(target = secondLED)
    third_thread = Thread(target = thirdLED)
    
    button_thread.start()    
    first_thread.start()
    second_thread.start()
    third_thread.start()

    #DO STUFF HERE INSTEAD OF JUST WAITING?
      
    #wait for threads to finish
    first_thread.join()
    second_thread.join()
    third_thread.join()

    print ("All done")
    GPIO.cleanup()
