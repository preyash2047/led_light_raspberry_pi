#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# sudo apt-get install python3-rpi.gpio
import RPi.GPIO as GPIO
import time

PR1 = 3
LED1 = 5

GPIO.setwarnings(False)   # Ignore Warnings
GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering

while True:
    GPIO.setup(PR1, GPIO.OUT)
    GPIO.output(PR1, GPIO.LOW)
    GPIO.setup(PR1, GPIO.IN)
    
    #led
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.output(LED1, GPIO.LOW)
    if GPIO.input(PR1) == 0:
        GPIO.output(LED1, GPIO.HIGH)        

