import machine


def cutton_handler(pin):
    print("button clicked")  
    print(pin)

button=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)


button.irq(trigger=machine.Pin.IRQ_RISING,handler=cutton_handler)