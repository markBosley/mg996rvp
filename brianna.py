from machine import Pin
import utime




pin = Pin(25, Pin.OUT)


x=0

while x<5:
    pin.toggle()
    utime.sleep_ms(1500)
    x=x+1

print("Greetings. Running Brianna script")