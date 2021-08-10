import machine
from machine import Pin, PWM
import utime
import _thread
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

def start_probe():    
    sensor = HCSR04(trigger_pin=16, echo_pin=17,echo_timeout_us=1000000)
    t.move(60000)
    x=1
    while x<20:
        x=x+1
        distance = sensor.distance_cm()
        print("distance:",distance)
        if distance<10:
            x=50
        
       # print(x)        
        utime.sleep(1)
    t.stop()

def stop_button_handler(pin):
    print("stop button clicked")  
    t.stop()    
    #print(pin)

def start_button_handler(pin):
    print("start button clicked with determination") 
    start_probe()
    #print(pin)

# def configureSecodCore():
#     stop_button=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
#     stop_button.irq(trigger=machine.Pin.IRQ_RISING,handler=stop_button_handler)

# _thread.start_new_thread(configureSecodCore, ())

stop_button=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
start_button=machine.Pin(13,machine.Pin.IN,machine.Pin.PULL_DOWN)


stop_button.irq(trigger=machine.Pin.IRQ_RISING,handler=stop_button_handler)
start_button.irq(trigger=machine.Pin.IRQ_RISING,handler=start_button_handler)

# Need to Excute irq on separate thread

def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    maxDuty=9000
    minDuty=1000
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    servoPin.duty_u16(int(newDuty))

def test_steer():
    for degree in range(0,180,1):
        servo(degree)
        utime.sleep(0.001)
        print("increasing -- "+str(degree))

    for degree in range(180, 0, -1):
        servo(degree)
        utime.sleep(0.001)
        print("decreasing -- "+str(degree))

def test_distance():
    sensor = HCSR04(trigger_pin=16, echo_pin=17,echo_timeout_us=1000000)
    abort = False
    while not abort:
        distance = sensor.distance_cm()
        print(distance)
        if distance<10:
            abort = True
        utime.sleep(1)

def test_drive():
    t.move(60000)
    utime.sleep(4)
    t.stop()

def go():
    t.move(60000)
    while True:
        sensor = HCSR04(trigger_pin=16, echo_pin=17,echo_timeout_us=1000000)
        distance = sensor.distance_cm()
        if distance<10:
            print(distance)
        utime.sleep(1)

def testdrive():
     servo(90)
        

def stop():
    t.stop()
