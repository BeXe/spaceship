#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO
import subprocess
import time
import thread

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

def welcome_loop():
    while True:
            global playProcess
            x = 1
            print ("LOOPING")
            time.sleep(.5)
            playProcess=subprocess.Popen(['omxplayer','-b','Desktop/videos/loop/loop.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
            time.sleep(10)
            playProcess.stdin.write('q')
            x += 1

def videos():
    while True:
            if GPIO.input(9):
                    print ("STOP LOOP")
                    time.sleep(.5)
                    playProcess.stdin.write('q')
                    time.sleep(.5)
                    print "Play Sippycup"
                    sippycup_video=subprocess.Popen(['omxplayer','-b','Desktop/videos/sippycup.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
                    time.sleep(10)
                    sippycup_video.stdin.write('q')
                    time.sleep(.5)
                    welcome_loop()

            if GPIO.input(10):
                    print ("STOP LOOP")
                    time.sleep(.5)
                    playProcess.stdin.write('q')
                    time.sleep(.5)
                    print "Play Dodgeballs"
                    dodgeballs_video=subprocess.Popen(['omxplayer','-b','Desktop/videos/dodgeballs.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
                    time.sleep(10)
                    dodgeballs_video.stdin.write('q')
                    time.sleep(.5)
                    welcome_loop()

            if GPIO.input(11):
                    print ("STOP LOOP")
                    time.sleep(.5)
                    playProcess.stdin.write('q')
                    time.sleep(.5)
                    print "Play Shoppingcart"
                    shoppingcart_video=subprocess.Popen(['omxplayer','-b','Desktop/videos/shoppingcart.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
                    time.sleep(10)
                    shoppingcart_video.stdin.write('q')
                    time.sleep(.5)
                    welcome_loop()

thread.start_new_thread( videos, () )
thread.start_new_thread( welcome_loop, () )

while True:
    pass

GPIO.cleanup()
