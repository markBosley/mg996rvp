from machine import Pin
import time
import utime

pin = Pin(25, Pin.OUT)

x=0

while x<6:
    pin.toggle()
    time.sleep_ms(1500)
    x=x+1

print("hello. Robot is starting up")