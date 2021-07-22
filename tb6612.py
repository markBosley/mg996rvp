from machine import Pin, PWM
from time import sleep


pinPWMA = PWM(Pin(19))
pinPWMA.freq(50)

pinSTBY = Pin(16, Pin.OUT)
pinAIN2 = Pin(18, Pin.OUT)
pinAIN1 = Pin(17, Pin.OUT)


def move(speed):    
    pinPWMA.duty_u16(speed)

def stop():    
    pinPWMA.duty_u16(0)

 