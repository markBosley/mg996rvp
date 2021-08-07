import machine
from machine import Pin, PWM
import utime
import tb6612 as t
from HC_SR04 import HCSR04

# HC-SR04
#blue ttrigger pin 16
#orange echo pin 17

# mg996r servo
# pin 18 for control signal
servoPin = PWM(Pin(18))
servoPin.freq(50)

#motor dirver active
#purple

def stop_button_handler(pin):
    print("stop button clicked")  
    t.stop()    
    #print(pin)

def start_button_handler(pin):
    print("start button clicked") 
    t.move(20000) 
    #print(pin)

stop_button=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
start_button=machine.Pin(13,machine.Pin.IN,machine.Pin.PULL_DOWN)


stop_button.irq(trigger=machine.Pin.IRQ_RISING,handler=stop_button_handler)
start_button.irq(trigger=machine.Pin.IRQ_RISING,handler=start_button_handler)

def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=9000
    minDuty=1000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))

def steer():
    for degree in range(0,180,1):
        servo(degree)
        utime.sleep(0.001)
        print("increasing -- "+str(degree))

    for degree in range(180, 0, -1):
        servo(degree)
        utime.sleep(0.001)
        print("decreasing -- "+str(degree))

def distance():
    sensor = HCSR04(trigger_pin=16, echo_pin=17,echo_timeout_us=1000000)
    abort = False
    while not abort:
        distance = sensor.distance_cm()
        print(distance)
        if distance<10:
            abort = True
        utime.sleep(1)

def go():
    t.move(20000)
    while True:
        sensor = HCSR04(trigger_pin=16, echo_pin=17,echo_timeout_us=1000000)
        distance = sensor.distance_cm()
        if distance<10:
            print(distance)
        utime.sleep(1)
        

def stop():
    t.stop()
