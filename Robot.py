import machine
# purple is pin 14 stop

def stop_button_handler(pin):
    print("stop button clicked")  
    #print(pin)

def start_button_handler(pin):
    print("start button clicked")  
    #print(pin)

stop_button=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
start_button=machine.Pin(13,machine.Pin.IN,machine.Pin.PULL_DOWN)


stop_button.irq(trigger=machine.Pin.IRQ_RISING,handler=stop_button_handler)
start_button.irq(trigger=machine.Pin.IRQ_RISING,handler=start_button_handler)