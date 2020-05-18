#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# sudo apt-get install python3-rpi.gpio
import RPi.GPIO as GPIO
import time

led1 = 3
led2 = 5
led3 = 7
led4 = 8
led5 = 10
led6 = 12

led7 = 11
led8 = 13
led9 = 15
led10 = 19
led11 = 21
led12 = 23
led13 = 33
led14 = 35
led15 = 37


GPIO.setwarnings(False)   # Ignore Warnings
GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering

for i in range(1,16):
    GPIO.setup(eval("led"+str(i)), GPIO.OUT, initial=GPIO.LOW)

#defining digit1 method
def digit1(num):
    for i in range(1,7):
        GPIO.output(eval("led"+str(i)), GPIO.LOW)
    for i in range(1,num+1):
        GPIO.output(eval("led"+str(i)), GPIO.HIGH)

#defining digit2 method
def digit2(num):
    for i in range(7,16):
        GPIO.output(eval("led"+str(i)), GPIO.LOW)
    for i in range(7,num+6+1):
        GPIO.output(eval("led"+str(i)), GPIO.HIGH)
        
while True:
    sec = time.ctime(time.time())[-7:-5]
    print(sec)
    digit1(int(sec[0]))
    digit2(int(sec[1]))
    time.sleep(1)


# In[ ]:




