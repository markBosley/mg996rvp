# Next Tasks 
* add Voltage Regulator 3 pin Sockets. 2.54mm?

implement thread in robot

https://www.electrosoftcloud.com/en/multithreaded-script-on-raspberry-pi-pico-and-micropython/

internal_led = machine.Pin(25, machine.Pin.OUT)
# Function that will block the thread with a while loop
# which will simply display a message every second
def second_thread():
    while True:
        print("Hello, I'm here in the second thread writting every second")
        utime.sleep(1)
# Function that initializes execution in the second core
# The second argument is a list or dictionary with the arguments
# that will be passed to the function.
_thread.start_new_thread(second_thread, ())



git remote add origin
https://gist.github.com/mindplace/b4b094157d7a3be6afd2c96370d39fad