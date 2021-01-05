#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from time import sleep 
GPIO.setmode(GPIO.BCM)
import threading
from threading import Thread
from multiprocessing import Process
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
button2=11
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
LED1=24
LED2=23
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

# GPIO input setup
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

# GPIO output setup
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

# Set Flags to indicate LED is initially off
BS1=False
BS2=False
BS3=False
BS4=False
BS5=False
BS6=False
BS7=False
BS8=False
BS9=False
BS10=False
BS11=False
#BS12=False

# Set movie variables
movie1 = ("/home/pi/movie/aurora.mp4")

def buttonLOOP():
        global BS1
        global BS2
        global BS3
        global BS4
        global BS5
        global BS6
        global BS7
        global BS8
        global BS9
        global BS10
        global BS11
        while(1):                  # Create an infinite Loop
                if GPIO.input(button1)==0:            # Look for button 1 press
                        print ("Button 1 Was Pressed:")
                        if BS1==False:                # If the LED is off
                                GPIO.output(LED1,True) # turn it on
                                BS1=True              # Set Flag to show LED1 is now On 
                                time.sleep(.5)             # Delay

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
                
                if GPIO.input(button2)==0:            # Look for button 1 press
                        print ("Button 2 Was Pressed:")
                        if BS2==False:                # If the LED is off
                                GPIO.output(LED2,True) # turn it on
                                BS2=True              # Set Flag to show LED2 is now On 
                                time.sleep(.5)             # Delay
                                thread.run(thread1)
                               # thread.run(thread2)
                                countdown()
                               # thread2.run(thread4)
                                
                                                                
                                                        
                        else:                         # If the LED is on
                                GPIO.output(LED2,False) # Turn LED off
                                BS2=False               # Set Flag to show LED2 is now Off
                                sleep(.5)
                
                if GPIO.input(button3)==0:            # Look for button 1 press
                        print ("Button 3 Was Pressed:")
                        if BS3==False:                # If the LED is off
                                GPIO.output(LED3,True) # turn it on
                                BS3=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                                        
                        else:                         # If the LED is on
                                GPIO.output(LED3,False) # Turn LED off
                                BS3=False               # Set Flag to show LED3 is now Off
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

      
class thread(threading.Thread):  
    def __init__(self, thread_name, thread_ID):  
        threading.Thread.__init__(self)  
        self.thread_name = thread_name  
        self.thread_ID = thread_ID  
  
        # helper function to execute the threads 
    def run(self):  
        print(str(self.thread_name) +" "+ str(self.thread_ID));  
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

class countdown():  
    def __init__(self): 
        self.thread = threading.Thread(target=self.run)  
         
        # helper function to execute the threads 
    def run(self):  
        print(str(self.thread_name) +" "+ str(self.thread_ID));  
        for i in range(10, -1, -1):
              print('{num:06d}'.format(num=i))
   # print('{num:02d}'.format(num=i))
              display.fill(0)
              display.print(':')
   # display.print(i)
              display.print('{num:06d}'.format(num=i))
              time.sleep(1)
        return;

        
def secondLED():
       for i in range(10, -1, -1):
              print('{num:06d}'.format(num=i))
   # print('{num:02d}'.format(num=i))
              display.fill(0)
              display.print(':')
   # display.print(i)
              display.print('{num:06d}'.format(num=i))
              time.sleep(1)#        return;

def thirdLED():
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie1])

if __name__=='__main__':
    #d = Blink()
    #d.start()
    thread1 = thread("GFG", 1000)  
    thread2 = thread("GeeksforGeeks", 2000);
    thread3 = Thread(target = countdown) 
         
    thread1.start()  
    thread2.start()
    thread3.start()  
    

    thread1.join()
    thread2.join()
    thread3.join()
     
    
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
    button_thread.join()
    first_thread.join()
    second_thread.join()
    third_thread.join()

    print ("All done")
    GPIO.cleanup()
