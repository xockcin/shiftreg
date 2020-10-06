#!/usr/bin/env python3

################################
#
# Title: shiftreg.py 
#
# Author: OxKin
#
# Description: A library of functions
# for using a 74HC595 shift register
# IC with a Raspberry Pi. 
#
#

import RPi.GPIO as GPIO
from time import sleep
from psutil import cpu_percent

GPIO.setmode(GPIO.BCM)
PIN_DATA  = 22
PIN_LATCH = 27
PIN_CLOCK = 17

# Run this first
def setup():
    GPIO.setup(PIN_DATA,  GPIO.OUT)
    GPIO.setup(PIN_LATCH, GPIO.OUT)
    GPIO.setup(PIN_CLOCK, GPIO.OUT)

# Displays given byte
def shiftout(byte):
    GPIO.output(PIN_LATCH, 0)
    for x in range(8):
        GPIO.output(PIN_DATA, (byte >> x) & 1)
        GPIO.output(PIN_CLOCK, 1)
        GPIO.output(PIN_CLOCK, 0)
    GPIO.output(PIN_LATCH, 1)

# Indicates CPU usage
def indicator():
    bars = [((1<<i) - 1) for i in range(9)]
    while True:
        percent = cpu_percent()
        number = int(percent / 12.5)
        shiftout(bars[number])
        sleep(.2)

# Implements a "Larson scanner"
def scanner():
    lights = [1<<i for i in range(8)]
    while True:
        for light in lights:
            shiftout(light)
            sleep(.05)
        for light in reversed(lights):
            shiftout(light)
            sleep(.05)

setup()
indicator()
#scanner()
