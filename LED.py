from machine import Pin
import time
import utime
import brianna as b
#import tb6612



pin = Pin(25, Pin.OUT)

def on():
    pin.value(1)

def off():
    pin.value(0)

