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
button12=12

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
LED12=10

LEDdemo=True
LEDdemo2=True
start1=True

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
GPIO.setup(button12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button 12 an input, Activate Pull Up Resistor

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
GPIO.setup(LED12,GPIO.OUT)  # Make LED 12 an Output

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
BS12=False

# Set movie variables
movie1 = ("/home/pi/movie/aurora.mp4")
movie2 = ("/home/pi/movie/launch.mp4")
movie3 = ("/home/pi/movie/landing1.mp4")
movie4 = ("/home/pi/movie/landing22.mp4")
movie5 = ("/home/pi/movie/moonwalk.mp4")

sound1 = ("/home/pi/sounds/junk.mp3")
sound2 = ("/home/pi/sounds/whoosh.mp3")
sound3 = ("/home/pi/sounds/alarm.mp3")
sound4 = ("/home/pi/sounds/laser.mp3")
sound5 = ("/home/pi/sounds/move.mp3")

def ledLOOP():
       global LEDdemo
       global start1
       while(1):
              if LEDdemo == True:          
                     GPIO.output(LED1,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED3,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED4,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED5,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED6,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED7,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED8,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED9,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED10,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED11,True) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED12,True) # turn it on
                     time.sleep(2)
                     
                     GPIO.output(LED12,False) # turn it on
                     time.sleep(1)   
                     GPIO.output(LED11,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED10,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED9,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED8,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED7,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED6,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED5,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED4,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED4,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED3,False) # turn it on
                     time.sleep(.1)
                     GPIO.output(LED1,False) # turn it on
                     time.sleep(1)
                  
              if start1 == True:          
                     #GPIO.output(LED1,True) # turn it on
                     os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")
                     start1 = False   
                     
def LEDblink():
       global LEDdemo2
       while(1):
              if LEDdemo == True:
                     GPIO.output(LED1,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED1,False) #tun it off
                     time.sleep(.5) 
                     GPIO.output(LED3,True) # turn it on
                     time.sleep(.5)
                     GPIO.output(LED3,False) #tun it off       
                     time.sleep(.5)
                     GPIO.output(LED4,True) # turn it on
                     time.sleep(.5)
                     GPIO.output(LED4,False) #tun it off
                     time.sleep(.5)       
                     GPIO.output(LED5,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED5,False) #tun it off
                     time.sleep(.5)
                     GPIO.output(LED6,True) # turn it on
                     time.sleep(.5)
                     PIO.output(LED6,False) #tun it off       
                     time.sleep(.5)
                     GPIO.output(LED7,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED7,False) #tun it off 
                     time.sleep(.5)
                     GPIO.output(LED8,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED8,False) #tun it off
                     time.sleep(.5)
                     GPIO.output(LED9,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED9,False) #tun it off
                     time.sleep(.5)
                     GPIO.output(LED10,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED10,False) #tun it off
                     time.sleep(.5)
                     GPIO.output(LED11,True) # turn it on
                     time.sleep(.5) 
                     GPIO.output(LED11,False) #tun it off       
                     time.sleep(.5)
                                 
def movie11():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie1])
       #os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a -t 10 *.png")
       #os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a -t 10 *.png")
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")
       
def movie22():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie2])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")
     # sudo fbi -d /dev/fb0 -T 10 -t 10 *.png (werkt vanaf console)

def movie33():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie3])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")
       
def movie44():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie4])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")

def movie55():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', movie5])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")

def sound11():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', sound1])
       #os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a -t 10 *.png")
       #os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a -t 10 *.png")
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")
       
def sound22():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', sound2])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")
     # sudo fbi -d /dev/fb0 -T 10 -t 10 *.png (werkt vanaf console)

def sound33():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', sound3])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")      

def sound44():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', sound4])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")

def sound55():
       os.system("sudo killall -9 fbi")
       os.system('killall omxplayer.bin')
       omxc = Popen(['omxplayer', '-b', sound5])
       os.system("sudo fbi -d /dev/fb0 -T 10 -t 10 /home/pi/code/spaceship/*.png")       

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
        global LEDdemo
        global LEDdemo2
        global BS11
        global BS12
        global start1
        while(1):                  # Create an infinite Loop
                if GPIO.input(button1)==0:            # Look for button 1 press
                        print ("Button 1 Was Pressed:")
                        if BS1==False:                # If the LED is off
                                GPIO.output(LED2,True) # turn it on
                                BS2=True
                                movie22()
                               # LEDdemo=False
                                time.sleep(6)             # Delay
                                for i in range(10, -1, -1):
                                          print('{num:06d}'.format(num=i))
                                          display.fill(0)
                                          display.print(':')
                                          display.print('{num:06d}'.format(num=i))
                                          time.sleep(1) 
                                for i in range(0, +9999, +13):
                                          print('{num:06d}'.format(num=i))
                                          display.fill(0)
                                          display.print('{num:06d}'.format(num=i))
                                          time.sleep(.1) 
                               # LEDdemo=True
                                          
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
                                movie11()
                                                       
                                                                
                                                        
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
                                sound44()                        
                        else:                         # If the LED is on
                                GPIO.output(LED3,False) # Turn LED off
                                BS3=False               # Set Flag to show LED3 is now Off
                                sleep(.5)
                                   
                if GPIO.input(button4)==0:            # Look for button 1 press
                        print ("Button 4 Was Pressed:")
                        if BS4==False:                # If the LED is off
                                GPIO.output(LED4,True) # turn it on
                                BS4=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                sound22()                        
                        else:                         # If the LED is on
                                GPIO.output(LED4,False) # Turn LED off
                                BS4=False               # Set Flag to show LED3 is now Off
                                sleep(.5)                   
                                   
                if GPIO.input(button5)==0:            # Look for button 1 press
                        print ("Button 5 Was Pressed:")
                        if BS5==False:                # If the LED is off
                                GPIO.output(LED5,True) # turn it on
                                BS5=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                movie33()
                        else:                         # If the LED is on
                                GPIO.output(LED5,False) # Turn LED off
                                BS5=False               # Set Flag to show LED3 is now Off
                                sleep(.5)
                                   
                if GPIO.input(button6)==0:            # Look for button 1 press
                        print ("Button 6 Was Pressed:")
                        if BS6==False:                # If the LED is off
                                GPIO.output(LED6,True) # turn it on
                                BS6=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                sound33()                        
                        else:                         # If the LED is on
                                GPIO.output(LED6,False) # Turn LED off
                                BS6=False               # Set Flag to show LED3 is now Off
                                sleep(.5)                   
                                   
                if GPIO.input(button7)==0:            # Look for button 1 press
                        print ("Button 7 Was Pressed:")
                        if BS7==False:                # If the LED is off
                                GPIO.output(LED7,True) # turn it on
                                BS7=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                movie44()
                        else:                         # If the LED is on
                                GPIO.output(LED7,False) # Turn LED off
                                BS7=False               # Set Flag to show LED3 is now Off
                                sleep(.5)

                if GPIO.input(button8)==0:            # Look for button 1 press
                        print ("Button 8 Was Pressed:")
                        if BS8==False:                # If the LED is off
                                GPIO.output(LED8,True) # turn it on
                                BS8=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                sound55()
                        else:                         # If the LED is on
                                GPIO.output(LED8,False) # Turn LED off
                                BS8=False               # Set Flag to show LED3 is now Off
                                sleep(.5)
                                   
                if GPIO.input(button9)==0:            # Look for button 1 press
                        print ("Button 9 Was Pressed:")
                        if BS9==False:                # If the LED is off
                                GPIO.output(LED9,True) # turn it on
                                BS9=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                movie55()
                        else:                         # If the LED is on
                                GPIO.output(LED9,False) # Turn LED off
                                BS9=False               # Set Flag to show LED3 is now Off
                                sleep(.5)
                                   
                if GPIO.input(button12)==0:            # Look for button 1 press
                        print ("Button 12 Was Pressed:")
                        if BS12==False:                # If the LED is off
                                GPIO.output(LED12,True) # turn it on
                                BS12=True              # Set Flag to show LED3 is now On 
                                time.sleep(.5)             # Delay
                                movie55()
                        else:                         # If the LED is on
                                GPIO.output(LED12,False) # Turn LED off
                                BS9=False               # Set Flag to show LED3 is now Off
                                sleep(.5)                                  
                                
def buttonLOOP2():
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
                        
                        i=0
                        blinks=10
                        while (i < blinks):
                                GPIO.setup (24, GPIO.OUT)
                                GPIO.output (24, GPIO.HIGH)
                                time.sleep(1)
                                GPIO.output (24, GPIO.LOW)
                                time.sleep(1)
                                i=i+1	
                          
                       
if __name__=='__main__':
   
    third_thread = Thread(target = ledLOOP)
    button_thread = Thread(target = buttonLOOP)
    #first_thread = Thread(target = buttonLOOP2)
       
    third_thread.start()
    button_thread.start()    
    #first_thread.start()
     
    #DO STUFF HERE INSTEAD OF JUST WAITING?
      
    #wait for threads to finish
    third_thread.join()
    button_thread.join()
    #first_thread.join()


    print ("All done")
    GPIO.cleanup()
