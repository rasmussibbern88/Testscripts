# -*- coding: utf-8 -*-
"""
Created on Wed Delayul 18 22:17:48 2018
"""

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Setup

pinout = [2, 3, 4, 17] #init list with pin numbers
flowrate = 230 / 60  #define flowrate of pumps

rtb = 22
b = 27
Gin = [2, 10]
# Pinnummer, Volumen i ml
Blank = [3]
Sirup = [4, 5]
Soda = [17, 30]

GINHASS = [Gin, Sirup, Soda]

Drinken = GINHASS


#Rotary encoder button press
GPIO.setup(rtb, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Standalone button note: Dosn't work
GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in pinout:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)   # loop through pins and set mode and state to 'low'

def t(V):
    return V / flowrate

counter = 0
clkLastState = GPIO.input(clk) #Initial state
ispumping = [False]*len(Drinken)
# main loop
try:
    while True:
        # #check button and rotary enconder
        # clkState = GPIO.input(clk)
        # dtState = GPIO.input(dt)
        # if clkState != clkLastState:
        #     if dtState != clkState:
        #         counter += 1
        #     else:
        #         counter -= 1
            # print(counter)
        # clkLastState = clkState

        rtbState = GPIO.input(rtb)
        if rtbState == False and all(ispumping) == False:
            print('rtb Button Pressed')



            c = time.time()
            GPIO.output(Gin[0], GPIO.LOW)
            GPIO.output(Sirup[0], GPIO.LOW)
            GPIO.output(Soda[0], GPIO.LOW)
            ispumping = [True]*len(Drinken)
        if any(ispumping) == True:
            for i, x in enumerate(Drinken): #erstatter næste udkomenterede kode
                if time.time() - c >= t(x[1]):
                    GPIO.output(x[0], GPIO.HIGH)
                    ispumping[i] = False


        #if time.time() - c >= t(Gin[1])
            #GPIO.output(Gin[0], GPIO.HIGH)
        #if time.time() - c >= t(Sirup[1])
            #GPIO.output(Sirup[0], GPIO.HIGH)
        #if time.time() - c >= t(Soda[1])
            #GPIO.output(Soda[0], GPIO.HIGH)


        bState = GPIO.input(b) #Manual all pumps for cleaning and priming
        if bState == False and any(ispumping) == True:
            print('b Button Pressed')
            for x in pinout:
                    GPIO.output(i, GPIO.HIGH)
        elif bState == False and any(ispumping) == False:
            for x in pinout:
                GPIO.output(i, GPIO.LOW)


        time.sleep(0.02)
        #Slows Down busy loop
        #checks timing


# End program cleanly with keyboard
except KeyboardInterrupt:
  print("Keyboardinterrupt")

finally:
  GPIO.cleanup()
  print("Good bye!")

# Shutdown pi using python.
#Todo Make a button, that connects raspberry and powersyupply.
# from subprocess import call
# call("sudo shutdown -h now", shell=True)
