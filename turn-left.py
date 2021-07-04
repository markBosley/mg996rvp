from machine import Pin,PWM
import utime

MID = 1500000
MIN = 1200000
MAX = 2000000

pwm = PWM(Pin(16))

pwm.duty_u16(9000)

pwm.freq(50)
pwm.duty_ns(MIN)