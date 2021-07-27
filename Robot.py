import machine
import tb6612 as t
# purple is pin 14 stop

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

def go():
    t.move(20000)

def stop():
    t.stop()
