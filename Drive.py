from machine import Pin,PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 1800000

def Right():
    print("Turning Right")
    pwm = PWM(Pin(16))

    pwm.duty_u16(9000)

    pwm.freq(50)
    pwm.duty_ns(MAX)

def Left():
    pwm = PWM(Pin(16))

    pwm.duty_u16(9000)

    pwm.freq(50)
    pwm.duty_ns(MIN)

def Center():
    pwm = PWM(Pin(16))

    pwm.duty_u16(9000)

    pwm.freq(50)
    pwm.duty_ns(MID)
