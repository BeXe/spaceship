#import RPi.GPIO
#import time


import RPi.GPIO as GPIO
import time
import threading
from time import sleep 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinLED = 24
pinButton = 9

#GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(pinLED, GPIO.OUT)

working = False
#t.join()
def flash(pinLED, flashing):
    status = threading.local()
    status.LED = False
    while flashing.is_set():
        status.LED = not status.LED
        GPIO.output(pinLED, int(status.LED))
        time.sleep(0.5)

    GPIO.output(pinLED, 0)

if __name__ == '__main__':	
    def main_thread():
        flashing = threading.Event()
        flashing.clear()

        try:
            while True:
                time.sleep(0.02)  
                if GPIO.input(pinButton) == 0:
                    t = threading.Thread(target=flash, args=(pinLED, flashing,))
                    flashing.set()
                    t.start()

                    time.sleep(2)  # work would be here

                    flashing.clear()
                    t.join()
        except Exception as e:
            print(e.message)
        finally:
            GPIO.cleanup()
