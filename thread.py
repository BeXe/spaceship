from time import sleep     # Import sleep Library
import threading
import RPi.GPIO as GPIO    # Import GPIO Library 
#GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
GPIO.setmode(GPIO.BCM)



# FOR 7 Segment display
import time
import board
import busio
from adafruit_ht16k33 import segments

# FOR VIDEO
import os
import sys
from subprocess import Popen

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)


# Button Variables connected to which GPIO pin.
button1=9                 # Button 1 is connected to physical pin 16
button2=11                 # Button 2 is connected to physical pin 12
button3=19
button4=26
button5=25
button6=8
button7=7
button8=1
button9=20
button10=16
button11=21
#button12=

# Led variables, connected tot which GPIO pin
LED1=24                    # LED 1 is connected to physical pin 22
LED2=23                    # LED 2 is connected to physical pin 18
LED3=18
LED4=15
LED5=14
LED6=22
LED7=27
LED8=17
LED9=13
LED10=6
LED11=5
#LED12=

# Movie Variables (set where movie lives)
movie1 = ("/home/pi/movie/aurora.mp4")
movie2 = ("/home/pi/Videos/movie2.mp4")

m1=False

# last state variable
# last_state1 = True
# last_state2 = True

# 
# input_state1 = True
# input_state2 = True
# quit_video = True

# player = False

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1 an input, Activate Pull UP Resistor
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 2 an input, Activate Pull Up Resistor
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 3 an input, Activate Pull UP Resistor
GPIO.setup(button4,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 4 an input, Activate Pull Up Resistor
GPIO.setup(button5,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 5an input, Activate Pull UP Resistor
GPIO.setup(button6,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 6 an input, Activate Pull Up Resistor
GPIO.setup(button7,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 7 an input, Activate Pull UP Resistor
GPIO.setup(button8,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 8 an input, Activate Pull Up Resistor
GPIO.setup(button9,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 9 an input, Activate Pull UP Resistor
GPIO.setup(button10,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 10 an input, Activate Pull Up Resistor
GPIO.setup(button11,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 11 an input, Activate Pull UP Resistor
#GPIO.setup(button12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 12 an input, Activate Pull Up Resistor

GPIO.setup(LED1,GPIO.OUT,) # Make LED 1 an Output
GPIO.setup(LED2,GPIO.OUT,)  # Make LED 2 an Output
GPIO.setup(LED3,GPIO.OUT,) # Make LED 3 an Output
GPIO.setup(LED4,GPIO.OUT,)  # Make LED 4 an Output
GPIO.setup(LED5,GPIO.OUT,) # Make LED 5 an Output
GPIO.setup(LED6,GPIO.OUT,)  # Make LED 6 an Output
GPIO.setup(LED7,GPIO.OUT,) # Make LED 7 an Output
GPIO.setup(LED8,GPIO.OUT,)  # Make LED 8 an Output
GPIO.setup(LED9,GPIO.OUT,) # Make LED 9 an Output
GPIO.setup(LED10,GPIO.OUT,)  # Make LED 10 an Output
GPIO.setup(LED11,GPIO.OUT) # Make LED 11 an Output
#GPIO.setup(LED12,GPIO.OUT)  # Make LED 12 an Output

BS1=False                  # Set Flag BS1 to indicate LED is initially off
BS2=False                  # Set Flag BS2 to indicate LED is initially off
BS3=False                  # Set Flag BS3 to indicate LED is initially off
BS4=False                  # Set Flag BS4 to indicate LED is initially off
BS5=False                  # Set Flag BS1 to indicate LED is initially off
BS6=False                  # Set Flag BS2 to indicate LED is initially off
BS7=False                  # Set Flag BS3 to indicate LED is initially off
BS8=False                  # Set Flag BS4 to indicate LED is initially off
BS9=False                  # Set Flag BS1 to indicate LED is initially off
BS10=False                  # Set Flag BS2 to indicate LED is initially off
BS11=False                  # Set Flag BS3 to indicate LED is initially off
#BS12=False                  # Set Flag BS4 to indicate LED is initially off


def countdown():
#        global my_timer
#        my_timer = 10
#        for x in range(10):
#                my_timer = my_timer -1
#                sleep(1)

    for i in range(10, -1, -1):
                           print('{num:06d}'.format(num=i))
                           display.fill(0)
                           display.print(':')
                           display.print('{num:06d}'.format(num=i))
                           time.sleep(1)              

countdown_thread = threading.Thread(target = countdown)
                               
                                
while(1):                  # Create an infinite Loop
        if GPIO.input(button1)==0:            # Look for button 1 press
                print ("Button 1 Was Pressed:")
                if BS1==False:                # If the LED is off
                        GPIO.output(LED1,True) # turn it on
                        countdown_thread.start
                        BS1=True              # Set Flag to show LED1 is now On 
                        m1=True
                        sleep(.5)             # Delay
                        time.sleep(2)

                                   
                else:                         # If the LED is on
                        GPIO.output(LED1,False) # Turn LED off
                        BS1=False               # Set Flag to show LED1 is now Off
                        m1=False
                        sleep(.5)
       
