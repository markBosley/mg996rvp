from HC_SR04 import HCSR04
from machine import Pin
import utime



def Blink():
    pin = Pin(25, Pin.OUT)
    x=0
    while x<5:
        pin.toggle()
        utime.sleep_ms(1500)
        x=x+1

    pin.value(0)
    print("Greetings. Running Brianna script")

def Distance():
    # TRIG pin to pin 13 blue
    # ECHO pin to pin 12 purple
    print("testing distance")
    try:
        sensor = HCSR04(trigger_pin=13, echo_pin=12,echo_timeout_us=1000000)
        while True:
            distance = sensor.distance_cm()
            print(distance)           
    except KeyboardInterrupt:
            pass    

