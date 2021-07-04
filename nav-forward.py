from machine import Pin,PWM
import utime

MID = 1400000
MIN = 1000000
MAX = 1800000

pwm = PWM(Pin(16))

pwm.duty_u16(9000)

pwm.freq(50)
pwm.duty_ns(MID)