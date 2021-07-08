# testing Analalogue to Digitl converter voltage divider
# using 
import machine
potentiometer= machine.ADC(26)

led = machine.PWM(machine.Pin(19))
led.freq(1000)
    

def ReadVoltage():
    while True:
        print(str(potentiometer.read_u16()))
        #led.duty_u16(potentiometer.read_u16())