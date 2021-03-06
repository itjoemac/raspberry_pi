#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

ledPinY = 18    # Yellow LED
ledPinR = 11    # Red LED
ledPinG = 32    # Green LED

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPinY, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinY, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(ledPinR, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinR, GPIO.LOW)  # make ledPin output LOW level
    GPIO.setup(ledPinG, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPinG, GPIO.LOW) # make ledPin output LOW level

choice = 0

while choice != 'Q':
    print("Which LED Would you like to turn on?\n")
    print("Press 'R' for red, 'G' for green, 'Y' for yellow.\nPress 'Q' to quit.\n")
    choice = input("Your selection?\nColor: ")
    choice = choice.upper()
    setup()
    if choice == 'G':
        GPIO.output(ledPinG, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(ledPinG, GPIO.LOW)
        continue
    elif choice == 'R':
        GPIO.output(ledPinR, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(ledPinR, GPIO.LOW)
        continue
    elif choice == 'Y':
        GPIO.output(ledPinY, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(ledPinY, GPIO.LOW)
        continue
    else:
        print("Goodbye")
        break

