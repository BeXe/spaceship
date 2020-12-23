from time import sleep     # Import sleep Library
import RPi.GPIO as GPIO    # Import GPIO Library 
#GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
GPIO.setmode(GPIO.BCM)

button1=9                 # Button 1 is connected to physical pin 16
button2=11                 # Button 2 is connected to physical pin 12
button3=19
button4=26
button5=19
button6=2
button7=19
button8=26
button9=19
button10=26
button11=19
button12=26

LED1=24                    # LED 1 is connected to physical pin 22
LED2=23                    # LED 2 is connected to physical pin 18
LED3=18
LED4=15
LED5=14
LED6=18
LED7=15
LED8=14
LED9=18
LED10=15
LED11=14
LED11=12

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
GPIO.setup(LED11,GPIO.OUT,) # Make LED 11 an Output
GPIO.setup(LED12,GPIO.OUT)  # Make LED 12 an Output

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
BS12=False                  # Set Flag BS4 to indicate LED is initially off

while(1):                  # Create an infinite Loop
        if GPIO.input(button1)==0:            # Look for button 1 press
                print ("Button 1 Was Pressed:")
                if BS1==False:                # If the LED is off
                        GPIO.output(LED1,True) # turn it on
                        BS1=True              # Set Flag to show LED1 is now On 
                        sleep(.5)             # Delay
                else:                         # If the LED is on
                        GPIO.output(LED1,False) # Turn LED off
                        BS1=False               # Set Flag to show LED1 is now Off
                        sleep(.5)
        if GPIO.input(button2)==0: #Repeat above for LED 2 and button 2
                print ("Button 2 Was Pressed:")
                if BS2==False:
                        GPIO.output(LED2,True)
                        BS2=True
                        sleep(.5)
                else:
                        GPIO.output(LED2,False)
                        BS2=False
                        sleep(.5)
        if GPIO.input(button3)==0: #Repeat above for LED 3 and button 3
                print ("Button 3 Was Pressed:")
                if BS3==False:
                        GPIO.output(LED3,True)
                        BS3=True
                        sleep(.5)
                else:
                        GPIO.output(LED3,False)
                        BS3=False
                        sleep(.5)
        if GPIO.input(button4)==0: #Repeat above for LED 4 and button 4
                print ("Button 4 Was Pressed:")
                if BS4==False:
                        GPIO.output(LED4,True)
                        BS4=True
                        sleep(.5)
                else:
                        GPIO.output(LED4,False)
                        BS4=False
                        sleep(.5)


