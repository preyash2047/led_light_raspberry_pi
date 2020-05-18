#!/usr/bin/env python
# coding: utf-8

# In[2]:


# sudo apt-get install python3-rpi.gpio
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)   # Ignore Warnings
GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering
LED1 = 3
LED2 = 5
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
counter = 0

while True:
    if counter % 2 == 0:
        led1 = LED1
        led2 = LED2
    else:
        led1 = LED2
        led2 = LED1

    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.LOW)
    sleep(1)
    counter = counter + 1


# In[ ]:




