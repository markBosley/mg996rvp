from machine import Pin
import time

def Green():
    print("green")
    pin = Pin(19, Pin.OUT)
    pin.toggle()

def Clear():
    print("Turning off the Light")
