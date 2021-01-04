import RPi.GPIO
import time
import threading

pinLED = 24
pinButton = 9

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(pinLED, 0)

working = False
def flash(pinLED, flashing):
    status = threading.local()
    status.LED = False
    while flashing.is_set():
        status.LED = not status.LED
        GPIO.output(pinLED, int(status.LED))
        time.sleep(0.5)

    GPIO.output(pinLED, 0)
	
def main_thread():
    flashing = threading.Event()
    flashing.clear()

    try:
        while True:
            time.sleep(0.02)  
            if GPIO.input(pinButton) == 1:
                t = threading.Thread(target=flash, args=(pinLED, flashing,))
                flashing.set()
                t.start()

                time.sleep(2)  # work would be here

                flashing.clear()
                t.join()

except Exception as e:
    print(e)
finally:
    GPIO.cleanup()	
