from machine import Pin
import time
import utime

pin = Pin(25, Pin.OUT)



while True:
    pin.toggle()
    time.sleep_ms(1000)