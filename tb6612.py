from machine import Pin, PWM
from time import sleep

#orange wire gpio19 to pwma
#purple wire gpio18 to AIN2
#green wire gpio17 to AIN1
#gray wire gpio16 to stby

pinPWMA = Pin(19, Pin.OUT)
pinSTBY = Pin(16, Pin.OUT)
pinAIN2 = Pin(18, Pin.OUT)
pinAIN1 = Pin(17, Pin.OUT)

pinSTBY.on()
pinPWMA.on()
pinAIN2.on()
pinAIN1.off()

 